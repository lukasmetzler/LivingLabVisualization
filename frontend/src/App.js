import "./App.css";
import Layout from "./components/Layout";
import { ThemeProvider } from "@mui/styles";
import { createTheme } from "@mui/material/styles";
import { purple } from "@mui/material/colors";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Wetterstation from "./pages/Wetterstation";

const theme = createTheme({
  palette: {
    primary: {
      main: "#fefefe",
    },
    secondary: purple,
  },
  typography: {
    fontFamily: "Quicksand",
    fontWeightLight: 400,
    fontWeightRegular: 500,
    fontWeightMedium: 600,
    fontWeightBold: 700,
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Layout></Layout>
      <Router>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/wetterstation" element={<Wetterstation />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
