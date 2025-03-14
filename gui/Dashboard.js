import React from 'react';
import styled from 'styled-components';

const DashboardContainer = styled.div`
  display: flex;
  flex-direction: column;
  width: 300px;
  background-color: ${props => props.theme.colors.secondaryBg};
  border-right: 1px solid rgba(138, 43, 226, 0.3);
  padding: ${props => props.theme.spacing.md};
  overflow-y: auto;
`;

const Widget = styled.div`
  background: rgba(30, 30, 30, 0.7);
  border-radius: ${props => props.theme.borderRadius.medium};
  border: 1px solid rgba(138, 43, 226, 0.3);
  padding: ${props => props.theme.spacing.md};
  margin-bottom: ${props => props.theme.spacing.md};
  box-shadow: ${props => props.theme.shadows.small};
  
  &:hover {
    box-shadow: ${props => props.theme.shadows.glow};
    border-color: ${props => props.theme.colors.primaryAccent};
  }
`;

const WidgetTitle = styled.h3`
  font-family: ${props => props.theme.fonts.secondary};
  font-size: ${props => props.theme.fontSizes.bodyLarge};
  color: ${props => props.theme.colors.primaryAccent};
  margin-bottom: ${props => props.theme.spacing.sm};
  display: flex;
  align-items: center;
  
  svg {
    margin-right: ${props => props.theme.spacing.xs};
  }
`;

const TimeWidget = styled(Widget)`
  text-align: center;
`;

const Time = styled.div`
  font-family: ${props => props.theme.fonts.secondary};
  font-size: 32px;
  color: ${props => props.theme.colors.textPrimary};
  margin-bottom: ${props => props.theme.spacing.xs};
`;

const Date = styled.div`
  font-size: ${props => props.theme.fontSizes.body};
  color: ${props => props.theme.colors.textSecondary};
`;

const WeatherWidget = styled(Widget)``;

const WeatherInfo = styled.div`
  display: flex;
  align-items: center;
  margin-top: ${props => props.theme.spacing.sm};
`;

const WeatherIcon = styled.div`
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: ${props => props.theme.spacing.md};
  
  svg {
    width: 100%;
    height: 100%;
  }
`;

const WeatherDetails = styled.div``;

const Temperature = styled.div`
  font-size: 24px;
  font-weight: 500;
  color: ${props => props.theme.colors.textPrimary};
`;

const Condition = styled.div`
  font-size: ${props => props.theme.fontSizes.body};
  color: ${props => props.theme.colors.textSecondary};
`;

const Location = styled.div`
  font-size: ${props => props.theme.fontSizes.small};
  color: ${props => props.theme.colors.textSecondary};
  margin-top: ${props => props.theme.spacing.xs};
`;

const SystemStatusWidget = styled(Widget)``;

const StatusItem = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: ${props => props.theme.spacing.sm};
  
  &:last-child {
    margin-bottom: 0;
  }
`;

const StatusLabel = styled.div`
  font-size: ${props => props.theme.fontSizes.body};
  color: ${props => props.theme.colors.textSecondary};
`;

const StatusValue = styled.div`
  font-size: ${props => props.theme.fontSizes.body};
  color: ${props => props.theme.colors.textPrimary};
`;

const ProgressBar = styled.div`
  height: 6px;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: ${props => props.theme.borderRadius.small};
  margin-top: ${props => props.theme.spacing.xs};
  overflow: hidden;
`;

const ProgressFill = styled.div`
  height: 100%;
  width: ${props => props.value}%;
  background: ${props => {
    if (props.value > 80) return props.theme.colors.error;
    if (props.value > 60) return props.theme.colors.warning;
    return props.theme.colors.success;
  }};
  border-radius: ${props => props.theme.borderRadius.small};
  transition: width ${props => props.theme.transitions.normal};
`;

const QuickCommandsWidget = styled(Widget)``;

const CommandButton = styled.button`
  display: flex;
  align-items: center;
  width: 100%;
  padding: ${props => props.theme.spacing.sm};
  margin-bottom: ${props => props.theme.spacing.sm};
  background: rgba(138, 43, 226, 0.1);
  border-radius: ${props => props.theme.borderRadius.small};
  color: ${props => props.theme.colors.textPrimary};
  transition: all ${props => props.theme.transitions.fast};
  
  &:last-child {
    margin-bottom: 0;
  }
  
  svg {
    margin-right: ${props => props.theme.spacing.sm};
    color: ${props => props.theme.colors.primaryAccent};
  }
  
  &:hover {
    background: rgba(138, 43, 226, 0.3);
  }
`;

const Dashboard = ({ time, date, weather, systemStatus }) => {
  return (
    <DashboardContainer>
      <TimeWidget>
        <Time>{time}</Time>
        <Date>{date}</Date>
      </TimeWidget>
      
      <WeatherWidget>
        <WidgetTitle>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 3V5M5.6 5.6L7 7M3 12H5M5.6 18.4L7 17M12 19V21M17 17L18.4 18.4M19 12H21M18.4 5.6L17 7M17 12C17 14.7614 14.7614 17 12 17C9.23858 17 7 14.7614 7 12C7 9.23858 9.23858 7 12 7C14.7614 7 17 9.23858 17 12Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
          </svg>
          Weather
        </WidgetTitle>
        <WeatherInfo>
          <WeatherIcon>
            {weather.condition === 'Sunny' && (
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="5" stroke="#FFC107" strokeWidth="2"/>
                <path d="M12 3V5M5.6 5.6L7 7M3 12H5M5.6 18.4L7 17M12 19V21M17 17L18.4 18.4M19 12H21M18.4 5.6L17 7" stroke="#FFC107" strokeWidth="2" strokeLinecap="round"/>
              </svg>
            )}
          </WeatherIcon>
          <WeatherDetails>
            <Temperature>{weather.temperature}</Temperature>
            <Condition>{weather.condition}</Condition>
            <Location>{weather.location}</Location>
          </WeatherDetails>
        </WeatherInfo>
      </WeatherWidget>
      
      <SystemStatusWidget>
        <WidgetTitle>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9 2H15M12 10V14M19 10V14M5 10V14M2 6H22V18H2V6Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          System Status
        </WidgetTitle>
        <StatusItem>
          <StatusLabel>CPU Usage</StatusLabel>
          <StatusValue>{systemStatus.cpu}%</StatusValue>
        </StatusItem>
        <ProgressBar>
          <ProgressFill value={systemStatus.cpu} />
        </ProgressBar>
        
        <StatusItem>
          <StatusLabel>Memory Usage</StatusLabel>
          <StatusValue>{systemStatus.memory}%</StatusValue>
        </StatusItem>
        <ProgressBar>
          <ProgressFill value={systemStatus.memory} />
        </ProgressBar>
        
        <StatusItem>
          <StatusLabel>Network</StatusLabel>
          <StatusValue>{systemStatus.network}</StatusValue>
        </StatusItem>
        
        <StatusItem>
          <StatusLabel>Battery</StatusLabel>
          <StatusValue>{systemStatus.batteryLevel}%</StatusValue>
        </StatusItem>
        <ProgressBar>
          <ProgressFill value={systemStatus.batteryLevel} />
        </ProgressBar>
      </SystemStatusWidget>
      
      <QuickCommandsWidget>
        <WidgetTitle>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2L15 8L21 9L17 14L18 20L12 17.5L6 20L7 14L3 9L9 8L12 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          Quick Commands
        </WidgetTitle>
        <CommandButton>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 18.5C15.5899 18.5 18.5 15.5899 18.5 12C18.5 8.41015 15.5899 5.5 12 5.5C8.41015 5.5 5.5 8.41015 5.5 12C5.5 15.5899 8.41015 18.5 12 18.5Z" stroke="currentColor" strokeWidth="2"/>
            <path d="M19.5 12H22.5M1.5 12H4.5M12 4.5V1.5M12 22.5V19.5" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
          </svg>
          Turn on lights
        </CommandButton>
        <CommandButton>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 9H21M9 15L12 18M12 18L15 15M12 18V12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          Download files
        </CommandButton>
        <CommandButton>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 8V16M8 12H16M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          Create reminder
        </CommandButton>
      </QuickCommandsWidget>
    </DashboardContainer>
  );
};

export default Dashboard;
