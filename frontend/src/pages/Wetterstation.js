import React from "react";
import { Grid, Card, CardContent, Typography } from "@mui/material";

function Home() {
  return (
    <Grid
      container
      spacing={2}
      sx={{ paddingLeft: "500px", paddingTop: "150px" }}
    >
      <Grid item xs={5}>
        <Card>
          <CardContent>
            <Typography variant="h5" component="h2">
              Solarstrahlung
            </Typography>
            <Typography variant="body2" component="p">
              <iframe
                src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=auto&theme=light&panelId=1"
                width="1180"
                height="500"
                frameborder="0"
              ></iframe>
            </Typography>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={5}>
        <Card>
          <CardContent>
            <Typography variant="h5" component="h2">
              Außentemperatur
            </Typography>
            <Typography variant="body2" component="p">
              <iframe
                src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427065585&to=1707427365586&theme=light&panelId=2"
                width="1180"
                height="500"
                frameborder="0"
              ></iframe>
            </Typography>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={5}>
        <Card>
          <CardContent>
            <Typography variant="h5" component="h2">
              Raffstore Süd
            </Typography>
            <Typography variant="body2" component="p">
              <iframe
                src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427193830&to=1707427493830&theme=light&panelId=4"
                width="1180"
                height="500"
                frameborder="0"
              ></iframe>
            </Typography>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={5}>
        <Card>
          <CardContent>
            <Typography variant="h5" component="h2">
              Beleuchtung
            </Typography>
            <Typography variant="body2" component="p">
              <iframe
                src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427226980&to=1707427526981&theme=light&panelId=3"
                width="1180"
                height="500"
                frameborder="0"
              ></iframe>
            </Typography>
          </CardContent>
        </Card>
      </Grid>
    </Grid>
  );
}

export default Home;
