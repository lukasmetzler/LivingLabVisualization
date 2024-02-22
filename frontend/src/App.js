import { createTheme, ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Layout from "./components/Layout";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Wetterstation from "./pages/Wetterstation";
import OGRaum1 from "./pages/OGRaum1";

const theme = createTheme({
  palette: {
    mode: "dark", // Aktiviere den Dark Mode
    primary: {
      main: "#4d4949",
    },
    background: {
      default: "#121212", // Hintergrundfarbe für Dark Mode
      paper: "#1E1E1E", // Hintergrundfarbe für Papier
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline /> {/* Fügt globale Styles für den Dark Mode hinzu */}
      <Router>
        <Layout>
          <Routes>
            <Route exact path="/" element={<Wetterstation />} />
            <Route exact path="/1OGRaum1" element={<OGRaum1 />} />
          </Routes>
        </Layout>
      </Router>
    </ThemeProvider>
  );
}

export default App;
