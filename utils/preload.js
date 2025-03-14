const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld(
  'api', {
    // Window control functions
    minimizeWindow: () => ipcRenderer.send('minimize-window'),
    maximizeWindow: () => ipcRenderer.send('maximize-window'),
    closeWindow: () => ipcRenderer.send('close-window'),
    
    // System information
    getSystemInfo: () => {
      return {
        platform: process.platform,
        arch: process.arch,
        version: process.version,
        versions: process.versions
      };
    },
    
    // Time and date functions
    getCurrentTime: () => new Date().toLocaleTimeString(),
    getCurrentDate: () => new Date().toLocaleDateString(),
    
    // Placeholder for weather API (to be implemented)
    getWeather: (location) => {
      // This would be replaced with actual API call
      return {
        location: location || 'Unknown',
        temperature: '72°F',
        condition: 'Sunny',
        forecast: 'Clear skies'
      };
    },
    
    // Placeholder for voice recognition (to be implemented)
    startVoiceRecognition: () => console.log('Voice recognition started'),
    stopVoiceRecognition: () => console.log('Voice recognition stopped'),
    
    // Placeholder for face recognition (to be implemented)
    startFaceRecognition: () => console.log('Face recognition started'),
    stopFaceRecognition: () => console.log('Face recognition stopped'),
    
    // IPC communication
    send: (channel, data) => {
      // Whitelist channels
      const validChannels = ['toMain', 'command', 'query'];
      if (validChannels.includes(channel)) {
        ipcRenderer.send(channel, data);
      }
    },
    receive: (channel, func) => {
      // Whitelist channels
      const validChannels = ['fromMain', 'response', 'notification'];
      if (validChannels.includes(channel)) {
        // Deliberately strip event as it includes `sender` 
        ipcRenderer.on(channel, (event, ...args) => func(...args));
      }
    },
    
    // Remove all listeners for a channel
    removeAllListeners: (channel) => {
      const validChannels = ['fromMain', 'response', 'notification'];
      if (validChannels.includes(channel)) {
        ipcRenderer.removeAllListeners(channel);
      }
    }
  }
);
