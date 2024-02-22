import { makeStyles } from "@mui/styles";
import Drawer from "@mui/material/Drawer";
import Typography from "@mui/material/Typography";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import { useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { AddCircleOutlineOutlined, SubjectOutlined } from "@mui/icons-material";
import WbSunnyIcon from "@mui/icons-material/WbSunny";
import CameraIndoorIcon from "@mui/icons-material/CameraIndoor";
import HellaGraphSvg from "../images/navigation-logo.svg";

const drawerWidth = 250;

const useStyles = makeStyles({
  page: {
    background: "#403d3d",
    width: "100%",
  },
  root: {
    display: "flex",
  },
  drawer: {
    width: drawerWidth,
  },
  drawerPaper: {
    width: drawerWidth,
  },
  graph: {
    paddingLeft: 30,
    paddingTop: 20,
  },
});

export default function Layout({ children }) {
  const classes = useStyles();
  const history = useNavigate();
  const location = useLocation();

  const menuItems = [
    {
      text: "Wetterstation",
      icon: <WbSunnyIcon style={{ color: "yellow" }} />,
      path: "/",
    },
    {
      text: "1.OG Raum 1",
      icon: <CameraIndoorIcon style={{ color: "yellow" }} />,
      path: "/1OGRaum1",
    },
  ];

  return (
    <div className={classes.root}>
      <Drawer
        className={classes.drawer}
        variant="permanent"
        classes={{ paper: classes.drawerPaper }}
        anchor="left"
      >
        <div>
          <Typography variant="h5" className={classes.title}>
            <img
              src={HellaGraphSvg}
              alt="Hella Graphs"
              className={classes.graph}
            />
          </Typography>
        </div>

        <List>
          {menuItems.map((item) => (
            <ListItem
              button
              key={item.text}
              onClick={() => history(item.path)}
              className={location.pathname == item.path ? classes.active : null}
            >
              <ListItemIcon>{item.icon}</ListItemIcon>
              <ListItemText primary={item.text} />
            </ListItem>
          ))}
        </List>
      </Drawer>

      <div className={classes.page}>{children}</div>
    </div>
  );
}
