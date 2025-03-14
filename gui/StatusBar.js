import React from 'react';
import styled from 'styled-components';

const StatusBarContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 30px;
  background: ${props => props.theme.colors.secondaryBg};
  border-top: 1px solid rgba(138, 43, 226, 0.3);
  padding: 0 ${props => props.theme.spacing.md};
  font-size: ${props => props.theme.fontSizes.small};
  color: ${props => props.theme.colors.textSecondary};
`;

const StatusText = styled.div`
  display: flex;
  align-items: center;
  
  svg {
    margin-right: ${props => props.theme.spacing.xs};
    color: ${props => props.theme.colors.primaryAccent};
  }
`;

const StatusInfo = styled.div`
  display: flex;
  align-items: center;
`;

const StatusItem = styled.div`
  display: flex;
  align-items: center;
  margin-left: ${props => props.theme.spacing.md};
  
  svg {
    margin-right: ${props => props.theme.spacing.xs};
    color: ${props => props.theme.colors.primaryAccent};
  }
`;

const StatusBar = ({ status }) => {
  return (
    <StatusBarContainer>
      <StatusText>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          <path d="M12 16V12M12 8H12.01" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
        {status}
      </StatusText>
      
      <StatusInfo>
        <StatusItem>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            <path d="M12 6V12L16 14" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          {new Date().toLocaleTimeString()}
        </StatusItem>
        
        <StatusItem>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M5 12H19M12 5V19" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          New Command
        </StatusItem>
        
        <StatusItem>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            <path d="M19.4 15C19.1277 15.8031 19.2583 16.6718 19.7601 17.37C20.2619 17.9682 21.0377 18.3351 21.8601 18.37C21.9468 17.9025 21.9936 17.4249 22 16.94C22 16.2245 21.8926 15.5138 21.6841 14.83C21.2029 14.9334 20.6991 14.8684 20.2601 14.6379C19.8211 14.4073 19.4759 14.0235 19.28 13.56M4.6 15C4.87228 15.8031 4.74172 16.6718 4.23993 17.3C3.73814 17.9682 2.96234 18.3351 2.13993 18.37C2.05317 17.9025 2.00645 17.4249 2 16.94C2 16.2245 2.10742 15.5138 2.31589 14.83C2.79707 14.9334 3.30094 14.8684 3.73993 14.6379C4.17892 14.4073 4.52411 14.0235 4.72 13.56M19.4 8.99998C19.1277 8.19686 19.2583 7.32818 19.7601 6.69998C20.2619 6.07179 21.0377 5.70493 21.8601 5.66998C21.9468 6.13748 21.9936 6.61506 22 7.09998C22 7.81545 21.8926 8.52618 21.6841 9.20998C21.2029 9.10652 20.6991 9.17158 20.2601 9.40212C19.8211 9.63266 19.4759 10.0165 19.28 10.48M4.6 8.99998C4.87228 8.19686 4.74172 7.32818 4.23993 6.69998C3.73814 6.07179 2.96234 5.70493 2.13993 5.66998C2.05317 6.13748 2.00645 6.61506 2 7.09998C2 7.81545 2.10742 8.52618 2.31589 9.20998C2.79707 9.10652 3.30094 9.17158 3.73993 9.40212C4.17892 9.63266 4.52411 10.0165 4.72 10.48" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          Settings
        </StatusItem>
      </StatusInfo>
    </StatusBarContainer>
  );
};

export default StatusBar;
