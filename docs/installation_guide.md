# Jarvis AI Assistant Installation Guide

## System Requirements

Before installing Jarvis AI Assistant, ensure your system meets the following requirements:

### Hardware Requirements
- **Processor**: Intel Core i3 or equivalent (i5 or higher recommended)
- **RAM**: 4GB minimum (8GB or higher recommended)
- **Storage**: 2GB of free disk space
- **Microphone**: Required for voice recognition functionality
- **Camera**: Optional, required for face recognition functionality
- **Internet Connection**: Required for information retrieval and certain features

### Software Requirements
- **Operating System**:
  - Windows 10/11 (64-bit)
  - macOS 10.15 Catalina or newer
  - Ubuntu 20.04 LTS or newer (or other compatible Linux distributions)
- **Dependencies**:
  - Python 3.8 or newer
  - Node.js 14 or newer
  - SQLite 3.30 or newer

## Installation Instructions

### Windows Installation

1. **Download the Installer**
   - Download the Jarvis-Setup.exe file from the provided location

2. **Run the Installer**
   - Double-click the Jarvis-Setup.exe file
   - If prompted by User Account Control, click "Yes" to allow the installer to run
   - Follow the on-screen instructions in the installation wizard

3. **Complete the Installation**
   - Choose your installation directory (default is recommended)
   - Select which components to install (all are recommended)
   - Click "Install" to begin the installation process
   - Wait for the installation to complete

4. **Launch Jarvis**
   - Check "Launch Jarvis" in the final installation screen and click "Finish"
   - Alternatively, you can launch Jarvis from the Start menu or desktop shortcut

### macOS Installation

1. **Download the Installer**
   - Download the Jarvis.dmg file from the provided location

2. **Run the Installer**
   - Double-click the Jarvis.dmg file to mount it
   - Drag the Jarvis icon to the Applications folder
   - If prompted about an app from an unidentified developer, go to System Preferences > Security & Privacy and click "Open Anyway"

3. **Complete the Installation**
   - The application will be installed in your Applications folder
   - Eject the mounted DMG file

4. **Launch Jarvis**
   - Open the Applications folder and double-click the Jarvis icon
   - Grant necessary permissions when prompted (microphone, camera, etc.)

### Linux Installation

1. **Download the Installer**
   - Download the jarvis-setup.AppImage file from the provided location

2. **Make the Installer Executable**
   - Open Terminal
   - Navigate to the download directory: `cd ~/Downloads`
   - Make the file executable: `chmod +x jarvis-setup.AppImage`

3. **Run the Installer**
   - Execute the AppImage: `./jarvis-setup.AppImage`
   - Follow the on-screen instructions in the installation wizard

4. **Complete the Installation**
   - Choose your installation directory
   - Select which components to install
   - Click "Install" to begin the installation process
   - Wait for the installation to complete

5. **Launch Jarvis**
   - Run Jarvis from the application menu or using the command: `jarvis`

## Manual Installation from Source

For advanced users who prefer to install from source:

### Prerequisites

1. **Install Python 3.8+**
   - Windows: Download and install from python.org
   - macOS: Use Homebrew: `brew install python`
   - Linux: Use apt: `sudo apt install python3 python3-pip`

2. **Install Node.js 14+**
   - Windows/macOS: Download and install from nodejs.org
   - Linux: Use apt: `sudo apt install nodejs npm`

3. **Install Git**
   - Windows: Download and install from git-scm.com
   - macOS: Use Homebrew: `brew install git`
   - Linux: Use apt: `sudo apt install git`

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/jarvis-ai-assistant.git
   cd jarvis-ai-assistant
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js Dependencies**
   ```bash
   cd gui
   npm install
   ```

4. **Build the Application**
   ```bash
   npm run build
   ```

5. **Run Jarvis**
   ```bash
   cd ..
   python main.py
   ```

## Initial Setup

After installing Jarvis, you'll need to complete the initial setup:

1. **Launch Jarvis** for the first time

2. **Create Your Profile**
   - Enter your name and preferred settings
   - This information will be used to personalize your experience

3. **Configure Voice Recognition**
   - Follow the prompts to calibrate your microphone
   - Speak the sample phrases when prompted
   - This helps Jarvis recognize your voice more accurately

4. **Set Up Face Recognition (Optional)**
   - If you have a camera, you can set up face recognition
   - Follow the prompts to capture your face from different angles
   - This allows Jarvis to recognize you automatically

5. **Connect Services (Optional)**
   - Connect to weather services, calendar, email, etc.
   - Enter your credentials for each service you want to connect
   - This enables Jarvis to provide personalized information

6. **Complete Setup**
   - Review your settings and confirm
   - Jarvis is now ready to use!

## Troubleshooting

### Common Installation Issues

#### Windows

- **Issue**: "Missing DLL" error
  - **Solution**: Install the latest Visual C++ Redistributable from Microsoft's website

- **Issue**: Microphone not detected
  - **Solution**: Check microphone privacy settings in Windows Settings > Privacy > Microphone

#### macOS

- **Issue**: "App is damaged and can't be opened"
  - **Solution**: Go to System Preferences > Security & Privacy > General and click "Open Anyway"

- **Issue**: Permissions issues
  - **Solution**: Ensure Jarvis has microphone and camera permissions in System Preferences > Security & Privacy > Privacy

#### Linux

- **Issue**: Missing dependencies
  - **Solution**: Run `sudo apt install libsqlite3-dev portaudio19-dev python3-dev`

- **Issue**: AppImage won't run
  - **Solution**: Ensure you have FUSE installed: `sudo apt install fuse libfuse2`

### Installation Log

If you encounter issues during installation, check the installation log:

- **Windows**: `%APPDATA%\Jarvis\logs\install.log`
- **macOS**: `~/Library/Logs/Jarvis/install.log`
- **Linux**: `~/.local/share/jarvis/logs/install.log`

## Updating Jarvis

Jarvis will automatically check for updates. When an update is available:

1. A notification will appear in the Jarvis interface
2. Click the notification to view update details
3. Choose to install now or later

To manually check for updates:

1. Go to Help > Check for Updates
2. If an update is available, follow the prompts to install it

## Uninstalling Jarvis

### Windows

1. Go to Control Panel > Programs > Programs and Features
2. Find "Jarvis AI Assistant" in the list
3. Click "Uninstall" and follow the prompts
4. Optionally, delete the data folder at `%APPDATA%\Jarvis` to remove all user data

### macOS

1. Open the Applications folder
2. Drag the Jarvis application to the Trash
3. Optionally, delete the data folder at `~/Library/Application Support/Jarvis` to remove all user data

### Linux

1. If installed via AppImage:
   - Simply delete the AppImage file
   - Delete the data folder at `~/.local/share/jarvis`

2. If installed via package manager:
   - Use your distribution's package manager to uninstall
   - For example: `sudo apt remove jarvis-ai-assistant`

## Getting Help

If you need additional help with installation:

- Visit our support website: [support.jarvis-ai.com](https://support.jarvis-ai.com)
- Contact our support team: support@jarvis-ai.com
- Check the online documentation for updated installation instructions

## Next Steps

After successfully installing Jarvis:

1. Review the User Guide to learn how to use all features
2. Explore the customization options in Settings
3. Try out voice commands to get familiar with the system
4. Set up routines to automate common tasks

Congratulations! You've successfully installed Jarvis AI Assistant and are ready to enjoy its powerful features.
