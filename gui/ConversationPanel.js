import React, { useState, useRef, useEffect } from 'react';
import styled from 'styled-components';

const ConversationContainer = styled.div`
  display: flex;
  flex-direction: column;
  flex: 1;
  background-color: ${props => props.theme.colors.primaryBg};
  padding: ${props => props.theme.spacing.md};
  overflow: hidden;
`;

const ChatHistory = styled.div`
  flex: 1;
  overflow-y: auto;
  padding-right: ${props => props.theme.spacing.sm};
  margin-bottom: ${props => props.theme.spacing.md};
`;

const MessageGroup = styled.div`
  margin-bottom: ${props => props.theme.spacing.lg};
`;

const MessageHeader = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: ${props => props.theme.spacing.xs};
`;

const Avatar = styled.div`
  width: 32px;
  height: 32px;
  border-radius: ${props => props.theme.borderRadius.circle};
  background-color: ${props => props.isUser ? 'rgba(138, 43, 226, 0.2)' : 'rgba(138, 43, 226, 0.5)'};
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: ${props => props.theme.spacing.sm};
  
  svg {
    width: 18px;
    height: 18px;
    color: ${props => props.isUser ? props.theme.colors.secondaryAccent : props.theme.colors.primaryAccent};
  }
`;

const SenderName = styled.div`
  font-weight: 500;
  color: ${props => props.isUser ? props.theme.colors.secondaryAccent : props.theme.colors.primaryAccent};
`;

const Timestamp = styled.div`
  font-size: ${props => props.theme.fontSizes.small};
  color: ${props => props.theme.colors.textSecondary};
  margin-left: ${props => props.theme.spacing.sm};
`;

const MessageBubble = styled.div`
  max-width: 80%;
  padding: ${props => props.theme.spacing.sm} ${props => props.theme.spacing.md};
  border-radius: ${props => props.theme.borderRadius.medium};
  background-color: ${props => props.isUser ? 'rgba(138, 43, 226, 0.1)' : props.theme.colors.secondaryBg};
  border: 1px solid ${props => props.isUser ? 'rgba(138, 43, 226, 0.3)' : 'rgba(255, 255, 255, 0.1)'};
  color: ${props => props.theme.colors.textPrimary};
  margin-left: ${props => props.isUser ? 'auto' : '0'};
  box-shadow: ${props => props.theme.shadows.small};
  line-height: 1.5;
`;

const InputArea = styled.div`
  display: flex;
  align-items: center;
  background-color: ${props => props.theme.colors.secondaryBg};
  border-radius: ${props => props.theme.borderRadius.medium};
  border: 1px solid rgba(138, 43, 226, 0.3);
  padding: ${props => props.theme.spacing.sm};
  transition: border-color ${props => props.theme.transitions.fast};
  
  &:focus-within {
    border-color: ${props => props.theme.colors.primaryAccent};
    box-shadow: ${props => props.theme.shadows.glow};
  }
`;

const TextInput = styled.input`
  flex: 1;
  background: transparent;
  border: none;
  color: ${props => props.theme.colors.textPrimary};
  font-size: ${props => props.theme.fontSizes.body};
  padding: ${props => props.theme.spacing.sm};
  outline: none;
  
  &::placeholder {
    color: ${props => props.theme.colors.textSecondary};
  }
`;

const MicButton = styled.button`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: ${props => props.theme.borderRadius.circle};
  background: ${props => props.active ? props.theme.colors.primaryGradient : 'transparent'};
  color: ${props => props.active ? props.theme.colors.textPrimary : props.theme.colors.primaryAccent};
  margin-right: ${props => props.theme.spacing.sm};
  transition: all ${props => props.theme.transitions.fast};
  
  &:hover {
    background: ${props => props.active ? props.theme.colors.primaryGradient : 'rgba(138, 43, 226, 0.1)'};
  }
  
  svg {
    width: 20px;
    height: 20px;
  }
`;

const SendButton = styled.button`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: ${props => props.theme.borderRadius.circle};
  background: ${props => props.theme.colors.primaryGradient};
  color: ${props => props.theme.colors.textPrimary};
  transition: all ${props => props.theme.transitions.fast};
  
  &:hover {
    opacity: 0.9;
    transform: scale(1.05);
  }
  
  svg {
    width: 20px;
    height: 20px;
  }
`;

const VoiceVisualization = styled.div`
  display: ${props => props.active ? 'flex' : 'none'};
  align-items: center;
  justify-content: center;
  height: 40px;
  flex: 1;
  padding: 0 ${props => props.theme.spacing.md};
`;

const VoiceBar = styled.div`
  width: 4px;
  height: ${props => props.height}px;
  background-color: ${props => props.theme.colors.primaryAccent};
  border-radius: ${props => props.theme.borderRadius.small};
  margin: 0 2px;
  transition: height 0.1s ease;
`;

const ConversationPanel = () => {
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'Jarvis',
      content: 'Hello! I am Jarvis, your AI assistant. How can I help you today?',
      timestamp: new Date().toLocaleTimeString()
    }
  ]);
  const [inputText, setInputText] = useState('');
  const [isListening, setIsListening] = useState(false);
  const [voiceBars, setVoiceBars] = useState(Array(15).fill(5));
  
  const chatHistoryRef = useRef(null);
  
  // Scroll to bottom when messages change
  useEffect(() => {
    if (chatHistoryRef.current) {
      chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
    }
  }, [messages]);
  
  // Simulate voice visualization when listening
  useEffect(() => {
    let interval;
    if (isListening) {
      interval = setInterval(() => {
        setVoiceBars(prev => prev.map(() => Math.floor(Math.random() * 30) + 5));
      }, 100);
    }
    
    return () => clearInterval(interval);
  }, [isListening]);
  
  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };
  
  const handleSendMessage = () => {
    if (inputText.trim() === '') return;
    
    // Add user message
    const userMessage = {
      id: messages.length + 1,
      sender: 'You',
      content: inputText,
      timestamp: new Date().toLocaleTimeString(),
      isUser: true
    };
    
    setMessages(prev => [...prev, userMessage]);
    setInputText('');
    
    // Simulate Jarvis response after a short delay
    setTimeout(() => {
      const jarvisResponse = {
        id: messages.length + 2,
        sender: 'Jarvis',
        content: `I'm processing your request: "${inputText}"`,
        timestamp: new Date().toLocaleTimeString()
      };
      
      setMessages(prev => [...prev, jarvisResponse]);
    }, 1000);
  };
  
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };
  
  const toggleListening = () => {
    setIsListening(!isListening);
    
    // Simulate voice recognition result after 3 seconds
    if (!isListening) {
      setTimeout(() => {
        setIsListening(false);
        setInputText('What is the weather like today?');
      }, 3000);
    }
  };
  
  return (
    <ConversationContainer>
      <ChatHistory ref={chatHistoryRef}>
        {messages.map(message => (
          <MessageGroup key={message.id}>
            <MessageHeader>
              <Avatar isUser={message.isUser}>
                {message.isUser ? (
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 11C14.2091 11 16 9.20914 16 7C16 4.79086 14.2091 3 12 3C9.79086 3 8 4.79086 8 7C8 9.20914 9.79086 11 12 11Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    <path d="M12 14C8.13401 14 5 17.134 5 21H19C19 17.134 15.866 14 12 14Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                ) : (
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="9" stroke="currentColor" strokeWidth="2"/>
                    <path d="M12 6V12L16 14" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                )}
              </Avatar>
              <SenderName isUser={message.isUser}>{message.sender}</SenderName>
              <Timestamp>{message.timestamp}</Timestamp>
            </MessageHeader>
            <MessageBubble isUser={message.isUser}>{message.content}</MessageBubble>
          </MessageGroup>
        ))}
      </ChatHistory>
      
      <InputArea>
        <MicButton active={isListening} onClick={toggleListening}>
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 1C10.3431 1 9 2.34315 9 4V12C9 13.6569 10.3431 15 12 15C13.6569 15 15 13.6569 15 12V4C15 2.34315 13.6569 1 12 1Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            <path d="M19 10V12C19 16.4183 15.4183 20 11 20M5 10V12C5 16.4183 8.58172 20 13 20M12 20V23M8 23H16" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </MicButton>
        
        {isListening ? (
          <VoiceVisualization active={isListening}>
            {voiceBars.map((height, index) => (
              <VoiceBar key={index} height={height} />
            ))}
          </VoiceVisualization>
        ) : (
          <TextInput
            type="text"
            placeholder="Type a message..."
            value={inputText}
            onChange={handleInputChange}
            onKeyPress={handleKeyPress}
          />
        )}
        
        <SendButton onClick={handleSendMessage}>
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22 2L11 13M22 2L15 22L11 13M22 2L2 9L11 13" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </SendButton>
      </InputArea>
    </ConversationContainer>
  );
};

export default ConversationPanel;
