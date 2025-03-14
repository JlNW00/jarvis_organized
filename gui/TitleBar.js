import React from 'react';
import styled from 'styled-components';

const TitleBarContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 40px;
  background: ${props => props.theme.colors.secondaryBg};
  border-bottom: 1px solid rgba(138, 43, 226, 0.3);
  padding: 0 ${props => props.theme.spacing.md};
  -webkit-app-region: drag;
`;

const Title = styled.div`
  display: flex;
  align-items: center;
  font-family: ${props => props.theme.fonts.secondary};
  font-size: ${props => props.theme.fontSizes.bodyLarge};
  color: ${props => props.theme.colors.primaryAccent};
  
  svg {
    margin-right: ${props => props.theme.spacing.sm};
  }
`;

const WindowControls = styled.div`
  display: flex;
  -webkit-app-region: no-drag;
`;

const WindowButton = styled.button`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  margin-left: ${props => props.theme.spacing.xs};
  border-radius: ${props => props.theme.borderRadius.small};
  color: ${props => props.theme.colors.textSecondary};
  transition: all ${props => props.theme.transitions.fast};
  
  &:hover {
    background-color: rgba(255, 255, 255, 0.1);
    color: ${props => props.theme.colors.textPrimary};
  }
  
  &.close:hover {
    background-color: ${props => props.theme.colors.error};
  }
`;

const TitleBar = ({ title }) => {
  const handleMinimize = () => {
    if (window.api) {
      window.api.minimizeWindow();
    }
  };

  const handleMaximize = () => {
    if (window.api) {
      window.api.maximizeWindow();
    }
  };

  const handleClose = () => {
    if (window.api) {
      window.api.closeWindow();
    }
  };

  return (
    <TitleBarContainer className="titlebar">
      <Title>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" stroke="#8A2BE2" strokeWidth="2"/>
          <path d="M12 6V12L16 14" stroke="#8A2BE2" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
        {title}
      </Title>
      <WindowControls>
        <WindowButton className="titlebar-button" onClick={handleMinimize}>
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="2" y="5.5" width="8" height="1" rx="0.5" fill="currentColor"/>
          </svg>
        </WindowButton>
        <WindowButton className="titlebar-button" onClick={handleMaximize}>
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="2.5" y="2.5" width="7" height="7" rx="0.5" stroke="currentColor"/>
          </svg>
        </WindowButton>
        <WindowButton className="titlebar-button close" onClick={handleClose}>
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 3L9 9M9 3L3 9" stroke="currentColor" strokeWidth="1.2" strokeLinecap="round"/>
          </svg>
        </WindowButton>
      </WindowControls>
    </TitleBarContainer>
  );
};

export default TitleBar;
