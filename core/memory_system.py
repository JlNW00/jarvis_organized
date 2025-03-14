import os
import json
import time
import sqlite3
import threading
from datetime import datetime

class MemorySystem:
    """
    Memory System module for Jarvis AI Assistant.
    Handles storing and retrieving user preferences, conversation history, and visitor information.
    """
    
    def __init__(self, db_path=None):
        """
        Initialize the memory system module.
        
        Args:
            db_path (str): Path to the SQLite database file
        """
        if db_path is None:
            # Use a default path if none provided
            self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'jarvis_memory.db')
        else:
            self.db_path = db_path
            
        # Initialize database
        self._init_database()
        
        # Cache for frequently accessed data
        self.cache = {
            "user_preferences": {},
            "known_visitors": {},
            "recent_conversations": []
        }
        
        # Load cache from database
        self._load_cache()
        
        print(f"Memory System initialized with database at {self.db_path}")
    
    def _init_database(self):
        """Initialize the SQLite database with required tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create tables if they don't exist
        
        # User preferences table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_preferences (
            key TEXT PRIMARY KEY,
            value TEXT,
            category TEXT,
            last_updated TIMESTAMP
        )
        ''')
        
        # Visitors table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
            visitor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            face_encoding TEXT,
            first_visit TIMESTAMP,
            last_visit TIMESTAMP,
            visit_count INTEGER DEFAULT 1,
            known BOOLEAN DEFAULT 0,
            notes TEXT
        )
        ''')
        
        # Conversations table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            conversation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TIMESTAMP,
            speaker TEXT,
            message TEXT,
            visitor_id INTEGER,
            sentiment TEXT,
            FOREIGN KEY (visitor_id) REFERENCES visitors (visitor_id)
        )
        ''')
        
        # Events table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT,
            timestamp TIMESTAMP,
            description TEXT,
            metadata TEXT
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def _load_cache(self):
        """Load frequently accessed data into cache."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Initialize database tables if using in-memory database for testing
        if self.db_path == ":memory:":
            self._init_database()
        
        try:
            # Load user preferences
            cursor.execute("SELECT key, value, category FROM user_preferences")
            for row in cursor.fetchall():
                category = row['category']
                if category not in self.cache["user_preferences"]:
                    self.cache["user_preferences"][category] = {}
                self.cache["user_preferences"][category][row['key']] = json.loads(row['value'])
            
            # Load known visitors
            cursor.execute("SELECT visitor_id, name, last_visit, visit_count, known FROM visitors WHERE known = 1")
            for row in cursor.fetchall():
                self.cache["known_visitors"][row['visitor_id']] = {
                    "name": row['name'],
                    "last_visit": row['last_visit'],
                    "visit_count": row['visit_count']
                }
            
            # Load recent conversations
            cursor.execute("""
            SELECT c.conversation_id, c.timestamp, c.speaker, c.message, v.name as visitor_name
            FROM conversations c
            LEFT JOIN visitors v ON c.visitor_id = v.visitor_id
            ORDER BY c.timestamp DESC LIMIT 50
            """)
            self.cache["recent_conversations"] = [dict(row) for row in cursor.fetchall()]
        except sqlite3.OperationalError as e:
            # If tables don't exist yet, just initialize empty cache
            print(f"Note: {e} - Initializing empty cache")
        
        conn.close()
    
    # User Preferences Methods
    
    def get_preference(self, key, category="general", default=None):
        """
        Get a user preference value.
        
        Args:
            key (str): Preference key
            category (str): Preference category
            default: Default value if preference doesn't exist
            
        Returns:
            The preference value or default
        """
        if category in self.cache["user_preferences"] and key in self.cache["user_preferences"][category]:
            return self.cache["user_preferences"][category][key]
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT value FROM user_preferences WHERE key = ? AND category = ?",
            (key, category)
        )
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            value = json.loads(result[0])
            
            # Update cache
            if category not in self.cache["user_preferences"]:
                self.cache["user_preferences"][category] = {}
            self.cache["user_preferences"][category][key] = value
            
            return value
        
        return default
    
    def set_preference(self, key, value, category="general"):
        """
        Set a user preference value.
        
        Args:
            key (str): Preference key
            value: Preference value (will be JSON serialized)
            category (str): Preference category
            
        Returns:
            bool: True if successful
        """
        json_value = json.dumps(value)
        timestamp = datetime.now().isoformat()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO user_preferences (key, value, category, last_updated)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(key) DO UPDATE SET
                value = excluded.value,
                category = excluded.category,
                last_updated = excluded.last_updated
            """,
            (key, json_value, category, timestamp)
        )
        
        conn.commit()
        conn.close()
        
        # Update cache
        if category not in self.cache["user_preferences"]:
            self.cache["user_preferences"][category] = {}
        self.cache["user_preferences"][category][key] = value
        
        return True
    
    def get_all_preferences(self, category=None):
        """
        Get all user preferences, optionally filtered by category.
        
        Args:
            category (str): Optional category filter
            
        Returns:
            dict: Dictionary of preferences
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if category:
            cursor.execute(
                "SELECT key, value, last_updated FROM user_preferences WHERE category = ?",
                (category,)
            )
        else:
            cursor.execute(
                "SELECT key, value, category, last_updated FROM user_preferences"
            )
        
        results = cursor.fetchall()
        conn.close()
        
        preferences = {}
        for row in results:
            if category:
                preferences[row['key']] = {
                    "value": json.loads(row['value']),
                    "last_updated": row['last_updated']
                }
            else:
                if row['category'] not in preferences:
                    preferences[row['category']] = {}
                preferences[row['category']][row['key']] = {
                    "value": json.loads(row['value']),
                    "last_updated": row['last_updated']
                }
        
        return preferences
    
    # Visitor Management Methods
    
    def add_visitor(self, name, face_encoding=None, known=False, notes=None):
        """
        Add a new visitor to the database.
        
        Args:
            name (str): Visitor's name
            face_encoding: Face recognition encoding data
            known (bool): Whether this is a known visitor
            notes (str): Additional notes about the visitor
            
        Returns:
            int: Visitor ID
        """
        timestamp = datetime.now().isoformat()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Convert face encoding to JSON string if provided
        face_encoding_json = json.dumps(face_encoding) if face_encoding else None
        
        cursor.execute(
            """
            INSERT INTO visitors (name, face_encoding, first_visit, last_visit, known, notes)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (name, face_encoding_json, timestamp, timestamp, known, notes)
        )
        
        visitor_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # Update cache if it's a known visitor
        if known:
            self.cache["known_visitors"][visitor_id] = {
                "name": name,
                "last_visit": timestamp,
                "visit_count": 1
            }
        
        return visitor_id
    
    def update_visitor(self, visitor_id, **kwargs):
        """
        Update visitor information.
        
        Args:
            visitor_id (int): Visitor ID
            **kwargs: Fields to update (name, face_encoding, known, notes)
            
        Returns:
            bool: True if successful
        """
        if not kwargs:
            return False
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        set_clauses = []
        params = []
        
        # Process each field to update
        for key, value in kwargs.items():
            if key in ["name", "known", "notes"]:
                set_clauses.append(f"{key} = ?")
                params.append(value)
            elif key == "face_encoding":
                set_clauses.append("face_encoding = ?")
                params.append(json.dumps(value))
        
        if not set_clauses:
            conn.close()
            return False
        
        # Add visitor_id to params
        params.append(visitor_id)
        
        # Execute update
        query = f"UPDATE visitors SET {', '.join(set_clauses)} WHERE visitor_id = ?"
        cursor.execute(query, params)
        
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        
        # Update cache if needed
        if success and ('known' in kwargs and kwargs['known']) or self.is_known_visitor(visitor_id):
            visitor_info = self.get_visitor(visitor_id)
            if visitor_info:
                self.cache["known_visitors"][visitor_id] = {
                    "name": visitor_info["name"],
                    "last_visit": visitor_info["last_visit"],
                    "visit_count": visitor_info["visit_count"]
                }
        
        return success
    
    def get_visitor(self, visitor_id):
        """
        Get visitor information by ID.
        
        Args:
            visitor_id (int): Visitor ID
            
        Returns:
            dict: Visitor information or None if not found
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM visitors WHERE visitor_id = ?",
            (visitor_id,)
        )
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            visitor = dict(result)
            # Parse face encoding if it exists
            if visitor['face_encoding']:
                visitor['face_encoding'] = json.loads(visitor['face_encoding'])
            return visitor
        
        return None
    
    def find_visitor_by_face(self, face_encoding, threshold=0.6):
        """
        Find a visitor by face encoding.
        This is a simplified version; in a real implementation, 
        we would use proper face recognition comparison.
        
        Args:
            face_encoding: Face recognition encoding data
            threshold (float): Similarity threshold
            
        Returns:
            dict: Visitor information or None if not found
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM visitors WHERE face_encoding IS NOT NULL")
        visitors = cursor.fetchall()
        conn.close()
        
        # This is a placeholder for actual face recognition comparison
        # In a real implementation, we would use a proper face recognition library
        for visitor in visitors:
            visitor_encoding = json.loads(visitor['face_encoding'])
            
            # Simulate face comparison (in a real implementation, we would use proper comparison)
            # For demonstration, we'll just assume a match if the encoding is not None
            if visitor_encoding:
                # Convert to dict for easier handling
                visitor_dict = dict(visitor)
                visitor_dict['face_encoding'] = visitor_encoding
                return visitor_dict
        
        return None
    
    def get_known_visitors(self):
        """
        Get all known visitors.
        
        Returns:
            list: List of known visitors
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM visitors WHERE known = 1 ORDER BY last_visit DESC")
        
        visitors = cursor.fetchall()
        conn.close()
        
        # Parse face encodings
        for visitor in visitors:
            if visitor['face_encoding']:
                visitor['face_encoding'] = json.loads(visitor['face_encoding'])
        
        return [dict(visitor) for visitor in visitors]
    
    def is_known_visitor(self, visitor_id):
        """
        Check if a visitor is known.
        
        Args:
            visitor_id (int): Visitor ID
            
        Returns:
            bool: True if the visitor is known
        """
        # Check cache first
        if visitor_id in self.cache["known_visitors"]:
            return True
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT known FROM visitors WHERE visitor_id = ?",
            (visitor_id,)
        )
        
        result = cursor.fetchone()
        conn.close()
        
        return result and result[0]
    
    # Conversation Methods
    
    def add_conversation_entry(self, speaker, message, visitor_id=None, sentiment=None):
        """
        Add a conversation entry.
        
        Args:
            speaker (str): Speaker identifier (e.g., "user", "jarvis")
            message (str): The message content
            visitor_id (int): Optional visitor ID
            sentiment (str): Optional sentiment analysis
            
        Returns:
            int: Conversation entry ID
        """
        timestamp = datetime.now().isoformat()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO conversations (timestamp, speaker, message, visitor_id, sentiment)
            VALUES (?, ?, ?, ?, ?)
            """,
            (timestamp, speaker, message, visitor_id, sentiment)
        )
        
        conversation_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # Update cache
        visitor_name = None
        if visitor_id and visitor_id in self.cache["known_visitors"]:
            visitor_name = self.cache["known_visitors"][visitor_id]["name"]
        
        self.cache["recent_conversations"].insert(0, {
            "conversation_id": conversation_id,
            "timestamp": timestamp,
            "speaker": speaker,
            "message": message,
            "visitor_name": visitor_name
        })
        
        # Trim cache if needed
        if len(self.cache["recent_conversations"]) > 50:
            self.cache["recent_conversations"] = self.cache["recent_conversations"][:50]
        
        return conversation_id
    
    def get_conversation_history(self, limit=50, visitor_id=None):
        """
        Get conversation history.
        
        Args:
            limit (int): Maximum number of entries to return
            visitor_id (int): Optional visitor ID to filter by
            
        Returns:
            list: List of conversation entries
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if visitor_id:
            cursor.execute(
                """
                SELECT c.*, v.name as visitor_name
                FROM conversations c
                LEFT JOIN visitors v ON c.visitor_id = v.visitor_id
                WHERE c.visitor_id = ?
                ORDER BY c.timestamp DESC LIMIT ?
                """,
                (visitor_id, limit)
            )
        else:
            cursor.execute(
                """
                SELECT c.*, v.name as visitor_name
                FROM conversations c
                LEFT JOIN visitors v ON c.visitor_id = v.visitor_id
                ORDER BY c.timestamp DESC LIMIT ?
                """,
                (limit,)
            )
        
        results = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in results]
    
    # Event Logging Methods
    
    def log_event(self, event_type, description, metadata=None):
        """
        Log a system event.
        
        Args:
            event_type (str): Type of event
            description (str): Event description
            metadata (dict): Optional metadata
            
        Returns:
            int: Event ID
        """
        timestamp = datetime.now().isoformat()
        metadata_json = json.dumps(metadata) if metadata else None
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO events (event_type, timestamp, description, metadata)
            VALUES (?, ?, ?, ?)
            """,
            (event_type, timestamp, description, metadata_json)
        )
        
        event_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return event_id
    
    def get_events(self, event_type=None, limit=50):
        """
        Get system events.
        
        Args:
            event_type (str): Optional event type filter
            limit (int): Maximum number of events to return
            
        Returns:
            list: List of events
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if event_type:
            cursor.execute(
                "SELECT * FROM events WHERE event_type = ? ORDER BY timestamp DESC LIMIT ?",
                (event_type, limit)
            )
        else:
            cursor.execute(
                "SELECT * FROM events ORDER BY timestamp DESC LIMIT ?",
                (limit,)
            )
        
        results = cursor.fetchall()
        conn.close()
        
        events = []
        for row in results:
            event = dict(row)
            if event['metadata']:
                event['metadata'] = json.loads(event['metadata'])
            events.append(event)
        
        return events
    
    # Added missing functionality for recording visitor visits
    def record_visitor_visit(self, visitor_id):
        """
        Record a visit for an existing visitor, updating last_visit and incrementing visit_count.
        
        Args:
            visitor_id (int): Visitor ID
            
        Returns:
            bool: True if successful
        """
        timestamp = datetime.now().isoformat()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Update last_visit and increment visit_count
        cursor.execute(
            """
            UPDATE visitors 
            SET last_visit = ?, visit_count = visit_count + 1 
            WHERE visitor_id = ?
            """,
            (timestamp, visitor_id)
        )
        
        success = cursor.rowcount > 0
        conn.commit()
        
        # If successful, also log the visit as an event
        if success:
            visitor = self.get_visitor(visitor_id)
            visit_count = visitor["visit_count"] if visitor else 1
            
            cursor.execute(
                """
                INSERT INTO events (event_type, timestamp, description, metadata)
                VALUES (?, ?, ?, ?)
                """,
                (
                    "visitor_visit", 
                    timestamp, 
                    f"Visitor {visitor_id} visited", 
                    json.dumps({
                        "visitor_id": visitor_id,
                        "visit_count": visit_count,
                        "visitor_name": visitor["name"] if visitor else "Unknown"
                    })
                )
            )
            
            # Update cache if it's a known visitor
            if self.is_known_visitor(visitor_id):
                if visitor_id not in self.cache["known_visitors"]:
                    self.cache["known_visitors"][visitor_id] = {}
                
                self.cache["known_visitors"][visitor_id].update({
                    "last_visit": timestamp,
                    "visit_count": visit_count
                })
        
        conn.close()
        return success


# Example usage
if __name__ == "__main__":
    # Create a memory system instance
    memory = MemorySystem(":memory:")  # Use in-memory database for testing
    
    # Set a preference
    memory.set_preference("theme", "dark", category="ui")
    
    # Add a visitor
    visitor_id = memory.add_visitor("John Doe", known=True, notes="Friend")
    
    # Record a conversation
    memory.add_conversation_entry("user", "Hello Jarvis", visitor_id=visitor_id)
    memory.add_conversation_entry("jarvis", "Hello John, how can I help you today?", visitor_id=visitor_id)
    
    # Log an event
    memory.log_event("system_start", "Jarvis system started")
    
    # Record a visit
    memory.record_visitor_visit(visitor_id)
    
    # Get visitor info
    visitor = memory.get_visitor(visitor_id)
    print(f"Visitor: {visitor['name']}, Visits: {visitor['visit_count']}")
    
    # Get conversation history
    conversations = memory.get_conversation_history(visitor_id=visitor_id)
    for conv in conversations:
        print(f"{conv['speaker']}: {conv['message']}")
