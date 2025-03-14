import sys
import os
import unittest
import json
import sqlite3
from unittest.mock import MagicMock, patch

# Add the core directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.voice_recognition import VoiceRecognition
from core.task_automation import TaskAutomation
from core.information_retrieval import InformationRetrieval
from core.memory_system import MemorySystem
from core.integration import JarvisCore

class TestVoiceRecognition(unittest.TestCase):
    """Test cases for the Voice Recognition module."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.voice_recognition = VoiceRecognition(wake_word="jarvis")
    
    def test_initialization(self):
        """Test that the voice recognition module initializes correctly."""
        self.assertEqual(self.voice_recognition.wake_word, "jarvis")
        self.assertEqual(self.voice_recognition.language, "en-US")
        self.assertFalse(self.voice_recognition.is_listening)
        self.assertFalse(self.voice_recognition.wake_word_detected)
    
    def test_start_stop(self):
        """Test starting and stopping the voice recognition."""
        # Test starting
        self.voice_recognition.start()
        self.assertTrue(self.voice_recognition.is_listening)
        
        # Test stopping
        self.voice_recognition.stop()
        self.assertFalse(self.voice_recognition.is_listening)
    
    def test_callbacks(self):
        """Test callback registration and triggering."""
        # Create mock callbacks
        mock_wake_word_callback = MagicMock()
        mock_speech_callback = MagicMock()
        
        # Register callbacks
        self.voice_recognition.add_callback("on_wake_word", mock_wake_word_callback)
        self.voice_recognition.add_callback("on_speech_recognized", mock_speech_callback)
        
        # Trigger callbacks
        self.voice_recognition._trigger_callbacks("on_wake_word")
        self.voice_recognition._trigger_callbacks("on_speech_recognized", "test speech")
        
        # Verify callbacks were called
        mock_wake_word_callback.assert_called_once()
        mock_speech_callback.assert_called_once_with("test speech")
    
    def test_language_setting(self):
        """Test setting the language."""
        self.voice_recognition.set_language("fr-FR")
        self.assertEqual(self.voice_recognition.language, "fr-FR")


class TestTaskAutomation(unittest.TestCase):
    """Test cases for the Task Automation module."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.task_automation = TaskAutomation()
    
    def test_initialization(self):
        """Test that the task automation module initializes correctly."""
        self.assertIsNotNone(self.task_automation.tasks)
        self.assertIsNotNone(self.task_automation.routines)
        self.assertEqual(len(self.task_automation.running_tasks), 0)
    
    def test_execute_task(self):
        """Test executing a task."""
        # Execute a task
        result = self.task_automation.execute_task("check_weather", {"location": "New York"})
        
        # Verify result
        self.assertTrue(result["success"])
        self.assertIn("task_id", result)
        
        # Wait for task to complete
        import time
        time.sleep(3)
        
        # Check task status
        status = self.task_automation.get_task_status(result["task_id"])
        self.assertEqual(status["status"], "completed")
        self.assertIn("result", status)
    
    def test_execute_routine(self):
        """Test executing a routine."""
        # Execute a routine
        result = self.task_automation.execute_routine("morning")
        
        # Verify result
        self.assertTrue(result["success"])
        self.assertIn("results", result)
        self.assertEqual(len(result["results"]), 3)  # Morning routine has 3 tasks
    
    def test_task_history(self):
        """Test task history tracking."""
        # Execute a task
        self.task_automation.execute_task("turn_on_lights", {"room": "bedroom"})
        
        # Wait for task to complete
        import time
        time.sleep(2)
        
        # Get task history
        history = self.task_automation.get_task_history()
        
        # Verify history
        self.assertGreater(len(history), 0)
        self.assertEqual(history[-1]["name"], "turn_on_lights")


class TestInformationRetrieval(unittest.TestCase):
    """Test cases for the Information Retrieval module."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.info_retrieval = InformationRetrieval()
    
    def test_initialization(self):
        """Test that the information retrieval module initializes correctly."""
        self.assertIsNotNone(self.info_retrieval.sources)
        self.assertEqual(len(self.info_retrieval.search_history), 0)
    
    def test_search(self):
        """Test searching for information."""
        # Perform a search
        result = self.info_retrieval.search("what is the weather in New York")
        
        # Verify result
        self.assertEqual(result["query"], "what is the weather in New York")
        self.assertIn("results", result)
        self.assertIn("timestamp", result)
    
    def test_source_determination(self):
        """Test source determination based on query."""
        # Test weather query
        sources = self.info_retrieval._determine_sources("what's the weather like today")
        self.assertEqual(sources, ["weather"])
        
        # Test time query
        sources = self.info_retrieval._determine_sources("what time is it")
        self.assertEqual(sources, ["time"])
        
        # Test calculation query
        sources = self.info_retrieval._determine_sources("calculate 25 * 4")
        self.assertEqual(sources, ["calculator"])
        
        # Test general query
        sources = self.info_retrieval._determine_sources("who is Albert Einstein")
        self.assertEqual(sources, ["web", "knowledge_base"])
    
    def test_search_history(self):
        """Test search history tracking."""
        # Perform searches
        self.info_retrieval.search("what is the time")
        self.info_retrieval.search("what is the weather")
        
        # Get search history
        history = self.info_retrieval.get_search_history()
        
        # Verify history
        self.assertEqual(len(history), 2)
        self.assertEqual(history[-1]["query"], "what is the weather")


class TestMemorySystem(unittest.TestCase):
    """Test cases for the Memory System module."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Use a file-based database for testing to avoid in-memory database issues
        self.db_path = "/tmp/jarvis_test.db"
        
        # Remove existing test database if it exists
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        
        # Create the memory system with the test database
        self.memory_system = MemorySystem(self.db_path)
    
    def test_initialization(self):
        """Test that the memory system initializes correctly."""
        self.assertIsNotNone(self.memory_system.cache)
        self.assertEqual(len(self.memory_system.cache["user_preferences"]), 0)
        self.assertEqual(len(self.memory_system.cache["known_visitors"]), 0)
    
    def test_preferences(self):
        """Test setting and getting preferences."""
        # Set preferences
        self.memory_system.set_preference("theme", "dark", "ui")
        self.memory_system.set_preference("volume", 75, "audio")
        
        # Get preferences
        theme = self.memory_system.get_preference("theme", "ui")
        volume = self.memory_system.get_preference("volume", "audio")
        
        # Verify preferences
        self.assertEqual(theme, "dark")
        self.assertEqual(volume, 75)
        
        # Get all preferences for a category
        ui_prefs = self.memory_system.get_all_preferences("ui")
        self.assertIn("theme", ui_prefs)
    
    def test_visitors(self):
        """Test visitor management."""
        # Add a visitor
        visitor_id = self.memory_system.add_visitor("John Doe", known=True)
        
        # Get visitor
        visitor = self.memory_system.get_visitor(visitor_id)
        
        # Verify visitor
        self.assertEqual(visitor["name"], "John Doe")
        self.assertTrue(visitor["known"])
        
        # Update visitor
        self.memory_system.update_visitor(visitor_id, notes="Regular visitor")
        
        # Get updated visitor
        updated_visitor = self.memory_system.get_visitor(visitor_id)
        
        # Verify update
        self.assertEqual(updated_visitor["notes"], "Regular visitor")
        
        # Check if known
        is_known = self.memory_system.is_known_visitor(visitor_id)
        self.assertTrue(is_known)
    
    def test_conversations(self):
        """Test conversation management."""
        # Add a visitor
        visitor_id = self.memory_system.add_visitor("Jane Doe", known=True)
        
        # Add conversation entries
        self.memory_system.add_conversation_entry("Jane Doe", "Hello Jarvis!", visitor_id)
        self.memory_system.add_conversation_entry("Jarvis", "Hello Jane! How can I help you today?")
        
        # Get conversation history
        conversations = self.memory_system.get_conversation_history()
        
        # Verify conversations
        self.assertEqual(len(conversations), 2)
        self.assertEqual(conversations[0]["speaker"], "Jarvis")
        self.assertEqual(conversations[1]["speaker"], "Jane Doe")
        
        # Search conversations
        search_results = self.memory_system.search_conversations("Hello")
        self.assertEqual(len(search_results), 2)
    
    def test_events(self):
        """Test event logging."""
        # Log events
        self.memory_system.log_event("system_start", "Jarvis system started")
        self.memory_system.log_event("user_command", "User issued a command", {"command": "turn on lights"})
        
        # Get events
        events = self.memory_system.get_events()
        
        # Verify events
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["event_type"], "user_command")
        self.assertEqual(events[1]["event_type"], "system_start")


class TestJarvisIntegration(unittest.TestCase):
    """Test cases for the Jarvis integration."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Mock the core modules
        self.mock_voice_recognition = MagicMock(spec=VoiceRecognition)
        self.mock_task_automation = MagicMock(spec=TaskAutomation)
        self.mock_info_retrieval = MagicMock(spec=InformationRetrieval)
        self.mock_memory_system = MagicMock(spec=MemorySystem)
        
        # Patch the imports in the integration module
        with patch('core.integration.VoiceRecognition', return_value=self.mock_voice_recognition), \
             patch('core.integration.TaskAutomation', return_value=self.mock_task_automation), \
             patch('core.integration.InformationRetrieval', return_value=self.mock_info_retrieval), \
             patch('core.integration.MemorySystem', return_value=self.mock_memory_system):
            self.jarvis = JarvisCore()
    
    def test_initialization(self):
        """Test that the Jarvis core initializes correctly."""
        self.assertFalse(self.jarvis.is_running)
        self.assertIsNone(self.jarvis.current_user)
        self.assertIsNone(self.jarvis.current_visitor)
    
    def test_start_stop(self):
        """Test starting and stopping Jarvis."""
        # Test starting
        self.jarvis.start()
        self.assertTrue(self.jarvis.is_running)
        self.mock_voice_recognition.start.assert_called_once()
        
        # Test stopping
        self.jarvis.stop()
        self.assertFalse(self.jarvis.is_running)
        self.mock_voice_recognition.stop.assert_called_once()
    
    def test_wake_word_handling(self):
        """Test wake word detection handling."""
        # Call the wake word callback
        self.jarvis._on_wake_word_detected()
        
        # Verify memory system was called to log the event
        self.mock_memory_system.log_event.assert_called_with(
            "wake_word_detected", "Wake word detected"
        )
    
    def test_speech_recognition_handling(self):
        """Test speech recognition handling."""
        # Set up mock for info retrieval search
        self.mock_info_retrieval.search.return_value = {
            "query": "what is the weather",
            "results": {
                "weather": {
                    "location": "New York",
                    "current": {
                        "condition": "sunny",
                        "temperature": "75°F"
                    }
                }
            }
        }
        
        # Call the speech recognized callback
        self.jarvis._on_speech_recognized("what is the weather")
        
        # Verify conversation was logged
        self.mock_memory_system.add_conversation_entry.assert_called()
        
        # Verify info retrieval was called
        self.mock_info_retrieval.search.assert_called_with("what is the weather")
    
    def test_visitor_detection(self):
        """Test visitor detection."""
        # Set up mock for find_visitor_by_face
        self.mock_memory_system.find_visitor_by_face.return_value = None
        self.mock_memory_system.add_visitor.return_value = 1
        self.mock_memory_system.get_visitor.return_value = {"visitor_id": 1, "name": "John Doe"}
        
        # Detect a visitor
        visitor = self.jarvis.detect_visitor(name="John Doe")
        
        # Verify visitor was added
        self.mock_memory_system.add_visitor.assert_called_with("John Doe", known=True)
        
        # Verify visitor was returned
        self.assertEqual(visitor["name"], "John Doe")
        
        # Verify current visitor was set
        self.assertEqual(self.jarvis.current_visitor, 1)
    
    def test_event_handling(self):
        """Test event handling."""
        # Create mock event handlers
        mock_command_handler = MagicMock()
        mock_visitor_handler = MagicMock()
        
        # Register event handlers
        self.jarvis.add_event_handler("on_command_received", mock_command_handler)
        self.jarvis.add_event_handler("on_visitor_detected", mock_visitor_handler)
        
        # Trigger events
        self.jarvis._trigger_event("on_command_received", "test command")
        self.jarvis._trigger_event("on_visitor_detected", {"name": "John Doe"})
        
        # Verify handlers were called
        mock_command_handler.assert_called_once_with("test command")
        mock_visitor_handler.assert_called_once_with({"name": "John Doe"})


if __name__ == '__main__':
    unittest.main()
