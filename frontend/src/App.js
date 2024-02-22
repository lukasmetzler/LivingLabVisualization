import "./App.css";
import Layout from "./components/Layout";
import { ThemeProvider } from "@mui/styles";
import { createTheme } from "@mui/material/styles";
import { blue } from "@mui/material/colors";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Wetterstation from "./pages/Wetterstation";
import OGRaum1 from "./pages/1OGRaum1";

const theme = createTheme({
  palette: {
    primary: {
      main: "#4d4949",
    },
  },
  typography: {
    fontFamily: "Quicksand",
    fontWeightLight: 400,
    fontWeightRegular: 500,
    fontWeightMedium: 600,
    fontWeightBold: 700,
  },
  components: {
    MuiIconButton: {
      styleOverrides: {
        root: {
          color: "red", // Hier kannst du die Farbe für die Icons anpassen
        },
      },
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Router>
        <Layout></Layout>
        <Routes>
          <Route exact path="/" element={<Wetterstation />} />
          <Route exact path="/1OGRaum1" element={<OGRaum1 />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
