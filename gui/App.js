import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import TitleBar from './components/TitleBar';
import Dashboard from './components/Dashboard';
import ConversationPanel from './components/ConversationPanel';
import StatusBar from './components/StatusBar';

const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: ${props => props.theme.colors.primaryBg};
  color: ${props => props.theme.colors.textPrimary};
  overflow: hidden;
`;

const MainContent = styled.div`
  display: flex;
  flex: 1;
  overflow: hidden;
`;

const App = () => {
  const [currentTime, setCurrentTime] = useState(new Date().toLocaleTimeString());
  const [currentDate, setCurrentDate] = useState(new Date().toLocaleDateString());
  const [systemStatus, setSystemStatus] = useState({
    cpu: Math.floor(Math.random() * 30) + 10, // Simulated CPU usage
    memory: Math.floor(Math.random() * 40) + 20, // Simulated memory usage
    network: 'Connected',
    batteryLevel: 85
  });

  // Update time every second
  useEffect(() => {
    const timer = setInterval(() => {
      const now = new Date();
      setCurrentTime(now.toLocaleTimeString());
      setCurrentDate(now.toLocaleDateString());
    }, 1000);

    // Simulate changing system status
    const statusTimer = setInterval(() => {
      setSystemStatus(prev => ({
        ...prev,
        cpu: Math.floor(Math.random() * 30) + 10,
        memory: Math.floor(Math.random() * 40) + 20
      }));
    }, 5000);

    return () => {
      clearInterval(timer);
      clearInterval(statusTimer);
    };
  }, []);

  // Simulated weather data
  const weatherData = {
    location: 'New York',
    temperature: '72°F',
    condition: 'Sunny',
    forecast: 'Clear skies'
  };

  return (
    <AppContainer>
      <TitleBar title="Jarvis AI Assistant" />
      <MainContent>
        <Dashboard 
          time={currentTime}
          date={currentDate}
          weather={weatherData}
          systemStatus={systemStatus}
        />
        <ConversationPanel />
      </MainContent>
      <StatusBar status="Ready" />
    </AppContainer>
  );
};

export default App;
