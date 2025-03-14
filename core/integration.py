import os
import sys
import time
import threading
from core.voice_recognition import VoiceRecognition
from core.task_automation import TaskAutomation
from core.information_retrieval import InformationRetrieval
from core.memory_system import MemorySystem

class JarvisCore:
    """
    Main integration class for Jarvis AI Assistant.
    Connects all core modules and handles their interaction.
    """
    
    def __init__(self):
        """Initialize the Jarvis core system."""
        print("Initializing Jarvis Core System...")
        
        # Initialize all core modules
        self.voice_recognition = VoiceRecognition(wake_word="jarvis")
        self.task_automation = TaskAutomation()
        self.info_retrieval = InformationRetrieval()
        self.memory_system = MemorySystem()
        
        # Set up event callbacks
        self._setup_callbacks()
        
        # State variables
        self.is_running = False
        self.current_user = None
        self.current_visitor = None
        
        # Event handlers
        self.event_handlers = {
            "on_command_received": [],
            "on_task_completed": [],
            "on_visitor_detected": [],
            "on_system_status_changed": []
        }
        
        print("Jarvis Core System initialized successfully")
    
    def _setup_callbacks(self):
        """Set up callbacks between modules."""
        # Voice recognition callbacks
        self.voice_recognition.add_callback("on_wake_word", self._on_wake_word_detected)
        self.voice_recognition.add_callback("on_speech_recognized", self._on_speech_recognized)
        
        # Log initialization in memory system
        self.memory_system.log_event(
            "system_init", 
            "Jarvis Core System initialized",
            {"modules": ["voice_recognition", "task_automation", "info_retrieval", "memory_system"]}
        )
    
    def start(self):
        """Start the Jarvis system."""
        if self.is_running:
            print("Jarvis is already running")
            return
        
        self.is_running = True
        print("Starting Jarvis...")
        
        # Start voice recognition
        self.voice_recognition.start()
        
        # Log system start
        self.memory_system.log_event("system_start", "Jarvis system started")
        
        # Trigger system status change
        self._trigger_event("on_system_status_changed", "running")
        
        print("Jarvis is now running")
    
    def stop(self):
        """Stop the Jarvis system."""
        if not self.is_running:
            print("Jarvis is not running")
            return
        
        self.is_running = False
        print("Stopping Jarvis...")
        
        # Stop voice recognition
        self.voice_recognition.stop()
        
        # Log system stop
        self.memory_system.log_event("system_stop", "Jarvis system stopped")
        
        # Trigger system status change
        self._trigger_event("on_system_status_changed", "stopped")
        
        print("Jarvis has been stopped")
    
    def _on_wake_word_detected(self):
        """Handle wake word detection."""
        print("Wake word detected! Listening for command...")
        
        # Log wake word detection
        self.memory_system.log_event("wake_word_detected", "Wake word detected")
        
        # Could play a sound or visual indicator here
    
    def _on_speech_recognized(self, text):
        """
        Handle recognized speech.
        
        Args:
            text (str): Recognized speech text
        """
        print(f"Processing command: '{text}'")
        
        # Log the command
        conversation_id = self.memory_system.add_conversation_entry(
            "user", 
            text, 
            visitor_id=self.current_visitor
        )
        
        # Trigger command received event
        self._trigger_event("on_command_received", text)
        
        # Process the command
        response = self._process_command(text)
        
        # Log the response
        self.memory_system.add_conversation_entry(
            "jarvis", 
            response, 
            visitor_id=self.current_visitor
        )
        
        print(f"Response: {response}")
    
    def _process_command(self, command):
        """
        Process a user command.
        
        Args:
            command (str): The user command
            
        Returns:
            str: Response to the command
        """
        command = command.lower()
        
        # Check if it's a task command
        if any(task in command for task in ["turn on", "turn off", "set", "play"]):
            return self._handle_task_command(command)
        
        # Check if it's an information query
        elif any(query in command for query in ["what", "who", "when", "where", "how", "why"]):
            return self._handle_info_query(command)
        
        # Default response
        return "I'm not sure how to help with that. Could you please rephrase?"
    
    def _handle_task_command(self, command):
        """
        Handle a task automation command.
        
        Args:
            command (str): The task command
            
        Returns:
            str: Response to the command
        """
        # Simple task mapping (in a real implementation, this would be more sophisticated)
        if "turn on lights" in command:
            result = self.task_automation.execute_task("turn_on_lights", {"room": "living room"})
            return f"I've turned on the lights in the living room."
        
        elif "turn off lights" in command:
            result = self.task_automation.execute_task("turn_off_lights", {"room": "living room"})
            return f"I've turned off the lights in the living room."
        
        elif "set reminder" in command:
            result = self.task_automation.execute_task("set_reminder", {"message": "User reminder", "time": "18:00"})
            return f"I've set a reminder for 6:00 PM."
        
        elif "play music" in command:
            result = self.task_automation.execute_task("play_music", {"genre": "relaxing", "source": "spotify"})
            return f"Playing some relaxing music from Spotify."
        
        # If no specific task matched
        return "I'm not sure which task you want me to perform."
    
    def _handle_info_query(self, query):
        """
        Handle an information query.
        
        Args:
            query (str): The information query
            
        Returns:
            str: Response to the query
        """
        # Use the information retrieval module to get an answer
        search_result = self.info_retrieval.search(query)
        
        # Process the search results
        if "weather" in search_result["results"]:
            weather_data = search_result["results"]["weather"]
            location = weather_data.get("location", "your location")
            current = weather_data.get("current", {})
            condition = current.get("condition", "unknown")
            temperature = current.get("temperature", "unknown")
            
            return f"The weather in {location} is currently {condition} with a temperature of {temperature}."
        
        elif "time" in search_result["results"]:
            time_data = search_result["results"]["time"]
            current_time = time_data.get("current_time_12h", "unknown")
            
            return f"The current time is {current_time}."
        
        elif "date" in search_result["results"]:
            date_data = search_result["results"]["date"]
            formatted_date = date_data.get("formatted_date", "unknown")
            day_of_week = date_data.get("day_of_week", "")
            
            return f"Today is {day_of_week}, {formatted_date}."
        
        elif "calculator" in search_result["results"]:
            calc_data = search_result["results"]["calculator"]
            if calc_data.get("success", False):
                expression = calc_data.get("expression", "")
                result = calc_data.get("result", "")
                
                return f"The result of {expression} is {result}."
            else:
                return "I couldn't calculate that. Please try again."
        
        elif "web" in search_result["results"]:
            web_data = search_result["results"]["web"]
            if web_data.get("results", []):
                first_result = web_data["results"][0]
                return f"I found this on the web: {first_result['title']} - {first_result['snippet']}"
            else:
                return "I couldn't find any information about that on the web."
        
        elif "knowledge_base" in search_result["results"]:
            kb_data = search_result["results"]["knowledge_base"]
            if kb_data.get("found", False):
                return kb_data.get("content", "No information found.")
            else:
                return "I don't have that information in my knowledge base."
        
        # Default response if no specific source had results
        return "I'm searching for information on that, but I don't have a specific answer yet."
    
    def detect_visitor(self, face_encoding=None, name=None):
        """
        Detect and identify a visitor.
        
        Args:
            face_encoding: Optional face encoding data
            name: Optional visitor name
            
        Returns:
            dict: Visitor information
        """
        visitor = None
        
        # If face encoding is provided, try to find a match
        if face_encoding:
            visitor = self.memory_system.find_visitor_by_face(face_encoding)
            
            # If visitor found, update last visit
            if visitor:
                # Use the new record_visitor_visit function instead of just update_visitor
                self.memory_system.record_visitor_visit(visitor["visitor_id"])
            # If not found but name is provided, add as new visitor
            elif name:
                visitor_id = self.memory_system.add_visitor(name, face_encoding, known=True)
                visitor = self.memory_system.get_visitor(visitor_id)
            # If not found and no name, add as unknown visitor
            else:
                visitor_id = self.memory_system.add_visitor("Unknown Visitor", face_encoding)
                visitor = self.memory_system.get_visitor(visitor_id)
        
        # If only name is provided, try to find by name or add new
        elif name:
            # This is simplified; in a real implementation, we would search by name
            visitor_id = self.memory_system.add_visitor(name, known=True)
            visitor = self.memory_system.get_visitor(visitor_id)
        
        # If visitor was detected, set as current visitor and trigger event
        if visitor:
            self.current_visitor = visitor["visitor_id"]
            self._trigger_event("on_visitor_detected", visitor)
            
            # Log the visitor detection
            self.memory_system.log_event(
                "visitor_detected",
                f"Visitor detected: {visitor['name']}",
                {"visitor_id": visitor["visitor_id"], "known": visitor["known"]}
            )
            
            return visitor
        
        return None
    
    def add_event_handler(self, event_type, handler):
        """
        Add an event handler.
        
        Args:
            event_type (str): Event type
            handler (function): Handler function
        """
        if event_type in self.event_handlers:
            self.event_handlers[event_type].append(handler)
    
    def _trigger_event(self, event_type, *args):
        """
        Trigger an event.
        
        Args:
            event_type (str): Event type
            *args: Arguments to pass to handlers
        """
        if event_type in self.event_handlers:
            for handler in self.event_handlers[event_type]:
                handler(*args)
    
    def get_system_status(self):
        """
        Get the current system status.
        
        Returns:
            dict: System status information
        """
        return {
            "running": self.is_running,
            "current_visitor": self.current_visitor,
            "modules": {
                "voice_recognition": {
                    "active": self.voice_recognition.is_listening,
                    "wake_word": self.voice_recognition.wake_word
                },
                "memory_system": {
                    "known_visitors_count": len(self.memory_system.get_known_visitors()),
                    "recent_conversations_count": len(self.memory_system.get_conversation_history(limit=10))
                },
                "task_automation": {
                    "available_tasks_count": len(self.task_automation.tasks),
                    "available_routines_count": len(self.task_automation.routines)
                }
            }
        }


# Example usage
if __name__ == "__main__":
    # Create a Jarvis core instance
    jarvis = JarvisCore()
    
    # Start Jarvis
    jarvis.start()
    
    # Simulate detecting a visitor
    visitor = jarvis.detect_visitor(name="John Doe")
    
    # Simulate a wake word detection and command
    jarvis._on_wake_word_detected()
    jarvis._on_speech_recognized("What's the weather like today?")
    
    # Get system status
    status = jarvis.get_system_status()
    print(f"System status: {status}")
    
    # Keep the program running for demonstration
    try:
        print("Jarvis is running. Press Ctrl+C to stop...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping Jarvis...")
        jarvis.stop()
