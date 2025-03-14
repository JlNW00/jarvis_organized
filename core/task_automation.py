import os
import json
import time
import threading

class TaskAutomation:
    """
    Task Automation module for Jarvis AI Assistant.
    Handles execution of predefined tasks and routines.
    """
    
    def __init__(self):
        """Initialize the task automation module."""
        self.tasks = {}
        self.routines = {}
        self.running_tasks = {}
        self.task_history = []
        self.max_history = 100
        
        # Load predefined tasks and routines if available
        self._load_tasks()
        self._load_routines()
        
        print("Task Automation module initialized")
    
    def _load_tasks(self):
        """Load predefined tasks from storage."""
        # This is a placeholder for loading tasks from a file
        # In a real implementation, we would load from a database or file
        
        # Add some default tasks for demonstration
        self.tasks = {
            "turn_on_lights": {
                "name": "Turn on lights",
                "description": "Turn on the lights in a specified room",
                "parameters": ["room"],
                "function": self._simulate_turn_on_lights
            },
            "turn_off_lights": {
                "name": "Turn off lights",
                "description": "Turn off the lights in a specified room",
                "parameters": ["room"],
                "function": self._simulate_turn_off_lights
            },
            "set_reminder": {
                "name": "Set reminder",
                "description": "Set a reminder for a specific time",
                "parameters": ["message", "time"],
                "function": self._simulate_set_reminder
            },
            "check_weather": {
                "name": "Check weather",
                "description": "Check the weather for a location",
                "parameters": ["location"],
                "function": self._simulate_check_weather
            },
            "play_music": {
                "name": "Play music",
                "description": "Play music from a specified source",
                "parameters": ["genre", "source"],
                "function": self._simulate_play_music
            }
        }
        
        print(f"Loaded {len(self.tasks)} predefined tasks")
    
    def _load_routines(self):
        """Load predefined routines from storage."""
        # This is a placeholder for loading routines from a file
        # In a real implementation, we would load from a database or file
        
        # Add some default routines for demonstration
        self.routines = {
            "morning": {
                "name": "Morning Routine",
                "description": "Tasks to run in the morning",
                "tasks": [
                    {"task": "turn_on_lights", "params": {"room": "bedroom"}},
                    {"task": "check_weather", "params": {"location": "current"}},
                    {"task": "play_music", "params": {"genre": "upbeat", "source": "spotify"}}
                ]
            },
            "evening": {
                "name": "Evening Routine",
                "description": "Tasks to run in the evening",
                "tasks": [
                    {"task": "turn_on_lights", "params": {"room": "living room"}},
                    {"task": "play_music", "params": {"genre": "relaxing", "source": "spotify"}}
                ]
            },
            "bedtime": {
                "name": "Bedtime Routine",
                "description": "Tasks to run before bed",
                "tasks": [
                    {"task": "turn_off_lights", "params": {"room": "all"}},
                    {"task": "set_reminder", "params": {"message": "Wake up", "time": "08:00"}}
                ]
            }
        }
        
        print(f"Loaded {len(self.routines)} predefined routines")
    
    def execute_task(self, task_name, params=None):
        """
        Execute a specific task with the given parameters.
        
        Args:
            task_name (str): The name of the task to execute
            params (dict): Parameters for the task
            
        Returns:
            dict: Result of the task execution
        """
        if params is None:
            params = {}
            
        if task_name not in self.tasks:
            return {"success": False, "message": f"Task '{task_name}' not found"}
        
        task = self.tasks[task_name]
        
        # Check if all required parameters are provided
        for param in task["parameters"]:
            if param not in params:
                return {"success": False, "message": f"Missing required parameter: {param}"}
        
        # Execute the task
        try:
            task_id = f"{task_name}_{int(time.time())}"
            self.running_tasks[task_id] = {"name": task_name, "params": params, "status": "running"}
            
            # Start task in a separate thread
            thread = threading.Thread(
                target=self._execute_task_thread,
                args=(task_id, task["function"], params)
            )
            thread.daemon = True
            thread.start()
            
            return {"success": True, "message": f"Task '{task_name}' started", "task_id": task_id}
        except Exception as e:
            return {"success": False, "message": f"Error executing task: {str(e)}"}
    
    def _execute_task_thread(self, task_id, task_function, params):
        """Execute a task in a separate thread."""
        try:
            result = task_function(**params)
            self.running_tasks[task_id]["status"] = "completed"
            self.running_tasks[task_id]["result"] = result
            
            # Add to history
            self.task_history.append({
                "task_id": task_id,
                "name": self.running_tasks[task_id]["name"],
                "params": params,
                "result": result,
                "timestamp": time.time()
            })
            
            # Trim history if needed
            if len(self.task_history) > self.max_history:
                self.task_history = self.task_history[-self.max_history:]
                
        except Exception as e:
            self.running_tasks[task_id]["status"] = "failed"
            self.running_tasks[task_id]["error"] = str(e)
    
    def execute_routine(self, routine_name):
        """
        Execute a predefined routine.
        
        Args:
            routine_name (str): The name of the routine to execute
            
        Returns:
            dict: Result of the routine execution
        """
        if routine_name not in self.routines:
            return {"success": False, "message": f"Routine '{routine_name}' not found"}
        
        routine = self.routines[routine_name]
        results = []
        
        for task_info in routine["tasks"]:
            task_name = task_info["task"]
            params = task_info["params"]
            
            result = self.execute_task(task_name, params)
            results.append(result)
        
        return {
            "success": True,
            "message": f"Routine '{routine_name}' executed",
            "results": results
        }
    
    def get_task_status(self, task_id):
        """
        Get the status of a running or completed task.
        
        Args:
            task_id (str): The ID of the task
            
        Returns:
            dict: Status of the task
        """
        if task_id in self.running_tasks:
            return self.running_tasks[task_id]
        
        return {"success": False, "message": f"Task ID '{task_id}' not found"}
    
    def get_task_history(self, limit=10):
        """
        Get the history of executed tasks.
        
        Args:
            limit (int): Maximum number of history items to return
            
        Returns:
            list: List of task history items
        """
        return self.task_history[-limit:]
    
    def add_task(self, task_name, description, parameters, function):
        """
        Add a new task to the system.
        
        Args:
            task_name (str): The name of the task
            description (str): Description of the task
            parameters (list): List of required parameters
            function (callable): The function to execute
            
        Returns:
            bool: True if task was added successfully
        """
        if task_name in self.tasks:
            return False
        
        self.tasks[task_name] = {
            "name": task_name,
            "description": description,
            "parameters": parameters,
            "function": function
        }
        
        return True
    
    def add_routine(self, routine_name, description, tasks):
        """
        Add a new routine to the system.
        
        Args:
            routine_name (str): The name of the routine
            description (str): Description of the routine
            tasks (list): List of tasks to execute
            
        Returns:
            bool: True if routine was added successfully
        """
        if routine_name in self.routines:
            return False
        
        self.routines[routine_name] = {
            "name": routine_name,
            "description": description,
            "tasks": tasks
        }
        
        return True
    
    # Simulated task functions
    def _simulate_turn_on_lights(self, room):
        """Simulate turning on lights in a room."""
        time.sleep(1)  # Simulate task execution time
        return {"success": True, "message": f"Turned on lights in {room}"}
    
    def _simulate_turn_off_lights(self, room):
        """Simulate turning off lights in a room."""
        time.sleep(1)  # Simulate task execution time
        return {"success": True, "message": f"Turned off lights in {room}"}
    
    def _simulate_set_reminder(self, message, time):
        """Simulate setting a reminder."""
        time.sleep(1)  # Simulate task execution time
        return {"success": True, "message": f"Set reminder '{message}' for {time}"}
    
    def _simulate_check_weather(self, location):
        """Simulate checking the weather."""
        time.sleep(2)  # Simulate task execution time
        weather_conditions = ["sunny", "cloudy", "rainy", "snowy"]
        temperatures = [f"{temp}°F" for temp in range(32, 95, 5)]
        
        import random
        condition = random.choice(weather_conditions)
        temperature = random.choice(temperatures)
        
        return {
            "success": True,
            "location": location,
            "condition": condition,
            "temperature": temperature,
            "message": f"Weather in {location}: {condition}, {temperature}"
        }
    
    def _simulate_play_music(self, genre, source):
        """Simulate playing music."""
        time.sleep(1)  # Simulate task execution time
        return {"success": True, "message": f"Playing {genre} music from {source}"}


# Example usage
if __name__ == "__main__":
    # Create a task automation instance
    task_automation = TaskAutomation()
    
    # Execute a task
    result = task_automation.execute_task("check_weather", {"location": "New York"})
    print(f"Task execution result: {result}")
    
    # Wait for task to complete
    time.sleep(3)
    
    # Get task status
    if "task_id" in result:
        status = task_automation.get_task_status(result["task_id"])
        print(f"Task status: {status}")
    
    # Execute a routine
    routine_result = task_automation.execute_routine("morning")
    print(f"Routine execution result: {routine_result}")
