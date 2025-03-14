import { createGlobalStyle } from 'styled-components';

export const GlobalStyles = createGlobalStyle`
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Orbitron:wght@400;500;700&family=Roboto+Mono&display=swap');

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  html, body {
    height: 100%;
    width: 100%;
    overflow: hidden;
    font-family: ${props => props.theme.fonts.primary};
    font-size: ${props => props.theme.fontSizes.body};
    color: ${props => props.theme.colors.textPrimary};
    background-color: ${props => props.theme.colors.primaryBg};
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  #root {
    height: 100%;
    width: 100%;
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: ${props => props.theme.fonts.secondary};
    font-weight: 500;
    margin-bottom: ${props => props.theme.spacing.md};
  }

  h1 {
    font-size: ${props => props.theme.fontSizes.heading1};
  }

  h2 {
    font-size: ${props => props.theme.fontSizes.heading2};
  }

  h3 {
    font-size: ${props => props.theme.fontSizes.heading3};
  }

  p {
    margin-bottom: ${props => props.theme.spacing.md};
    line-height: 1.5;
  }

  button, input, select, textarea {
    font-family: inherit;
    font-size: inherit;
  }

  button {
    cursor: pointer;
    border: none;
    background: none;
    outline: none;
  }

  a {
    color: ${props => props.theme.colors.primaryAccent};
    text-decoration: none;
    transition: color ${props => props.theme.transitions.fast};

    &:hover {
      color: ${props => props.theme.colors.highlight};
    }
  }

  /* Custom scrollbar */
  ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }

  ::-webkit-scrollbar-track {
    background: ${props => props.theme.colors.secondaryBg};
  }

  ::-webkit-scrollbar-thumb {
    background: ${props => props.theme.colors.secondaryAccent};
    border-radius: ${props => props.theme.borderRadius.medium};
  }

  ::-webkit-scrollbar-thumb:hover {
    background: ${props => props.theme.colors.primaryAccent};
  }

  /* Electron specific - make app draggable from title bar */
  .titlebar {
    -webkit-app-region: drag;
  }

  .titlebar-button {
    -webkit-app-region: no-drag;
  }
`;
