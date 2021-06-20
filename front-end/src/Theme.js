import { ThemeProvider, createTheme } from '@fluentui/react';
import { Children } from 'react';

const myTheme = createTheme({
  palette: {
    themePrimary: "#00730d",
    themeLighterAlt: "#eff9f1",
    themeLighter: "#c3e9c8",
    themeLight: "#95d59c",
    themeTertiary: "#44ab50",
    themeSecondary: "#10841d",
    themeDarkAlt: "#00670c",
    themeDark: "#00570a",
    themeDarker: "#004007",
    neutralLighterAlt: "#faf9f8",
    neutralLighter: "#f3f2f1",
    neutralLight: "#edebe9",
    neutralQuaternaryAlt: "#e1dfdd",
    neutralQuaternary: "#d0d0d0",
    neutralTertiaryAlt: "#c8c6c4",
    neutralTertiary: "#a19f9d",
    neutralSecondary: "#605e5c",
    neutralPrimaryAlt: "#3b3a39",
    neutralPrimary: "#323130",
    neutralDark: "#201f1e",
    black: "#000000",
    white: "#ffffff",
  },
});

const Theme = ({children}) => (<ThemeProvider theme={myTheme}>{ children }</ThemeProvider>);

export default Theme;
