export const theme = {
  colors: {
    // Primary colors
    primaryBg: '#121212',
    secondaryBg: '#1E1E1E',
    primaryAccent: '#8A2BE2',
    secondaryAccent: '#9370DB',
    highlight: '#B39DDB',
    
    // Text colors
    textPrimary: '#FFFFFF',
    textSecondary: '#CCCCCC',
    
    // Status colors
    success: '#4CAF50',
    warning: '#FFC107',
    error: '#F44336',
    
    // Gradients
    primaryGradient: 'linear-gradient(135deg, #8A2BE2 0%, #9370DB 100%)',
    accentGradient: 'linear-gradient(135deg, #9370DB 0%, #B39DDB 100%)'
  },
  
  fonts: {
    primary: "'Roboto', sans-serif",
    secondary: "'Orbitron', sans-serif",
    mono: "'Roboto Mono', monospace"
  },
  
  fontSizes: {
    small: '12px',
    body: '14px',
    bodyLarge: '16px',
    heading3: '18px',
    heading2: '20px',
    heading1: '24px'
  },
  
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
    xl: '32px',
    xxl: '48px'
  },
  
  borderRadius: {
    small: '4px',
    medium: '8px',
    large: '12px',
    circle: '50%'
  },
  
  shadows: {
    small: '0 2px 4px rgba(0, 0, 0, 0.3)',
    medium: '0 4px 8px rgba(0, 0, 0, 0.3)',
    large: '0 8px 16px rgba(0, 0, 0, 0.3)',
    glow: '0 0 8px rgba(138, 43, 226, 0.6)'
  },
  
  transitions: {
    fast: '0.2s ease',
    normal: '0.3s ease',
    slow: '0.5s ease'
  },
  
  zIndex: {
    base: 1,
    overlay: 10,
    modal: 100,
    tooltip: 1000
  }
};
