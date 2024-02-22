import React, { useState } from "react";
import { Grid, Card, CardContent, Typography, Button } from "@mui/material";

function ErstesOGRaum1() {
  const [step, setStep] = useState(1);

  const handleNextStep = () => {
    setStep((prevStep) => (prevStep < 3 ? prevStep + 1 : prevStep));
  };

  const handlePrevStep = () => {
    setStep((prevStep) => (prevStep > 1 ? prevStep - 1 : prevStep));
  };

  return (
    <div>
      <div style={{ textAlign: "center", marginTop: "20px" }}>
        <Button
          disabled={step === 1}
          onClick={handlePrevStep}
          sx={{
            marginRight: "10px",
            backgroundColor: "#4d4949",
            color: "#ffffff",
            "&:hover": {
              backgroundColor: "#333333",
            },
          }}
        >
          Zurück
        </Button>
        <Button
          disabled={step === 3}
          onClick={handleNextStep}
          sx={{
            backgroundColor: "#4d4949",
            color: "#ffffff",
            "&:hover": {
              backgroundColor: "#333333",
            },
          }}
        >
          Weiter
        </Button>
      </div>
      <Grid
        container
        spacing={2}
        sx={{ paddingLeft: "250px", paddingTop: "150px" }}
      >
        {step === 1 && (
          <>
            <Grid item xs={5}>
              <Card>
                <CardContent>
                  <Typography variant="h5" component="h2">
                    Solarstrahlung
                  </Typography>
                  <Typography variant="body2" component="p">
                    <iframe
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=auto&theme=dark&panelId=1"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427065585&to=1707427365586&theme=dark&panelId=2"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427193830&to=1707427493830&theme=dark&panelId=4"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427226980&to=1707427526981&theme=dark&panelId=3"
                      width="1180"
                      height="500"
                      frameborder="0"
                    ></iframe>
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          </>
        )}
        {step === 2 && (
          <>
            <Grid item xs={5}>
              <Card>
                <CardContent>
                  <Typography variant="h5" component="h2">
                    Solarstrahlung
                  </Typography>
                  <Typography variant="body2" component="p">
                    <iframe
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=auto&theme=dark&panelId=1"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427065585&to=1707427365586&theme=dark&panelId=2"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427193830&to=1707427493830&theme=dark&panelId=4"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427226980&to=1707427526981&theme=dark&panelId=3"
                      width="1180"
                      height="500"
                      frameborder="0"
                    ></iframe>
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          </>
        )}
        {step === 3 && (
          <>
            <Grid item xs={5}>
              <Card>
                <CardContent>
                  <Typography variant="h5" component="h2">
                    Solarstrahlung
                  </Typography>
                  <Typography variant="body2" component="p">
                    <iframe
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=auto&theme=dark&panelId=1"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427065585&to=1707427365586&theme=dark&panelId=2"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427193830&to=1707427493830&theme=dark&panelId=4"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427226980&to=1707427526981&theme=dark&panelId=3"
                      width="1180"
                      height="500"
                      frameborder="0"
                    ></iframe>
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          </>
        )}
        {step === 4 && (
          <>
            <Grid item xs={5}>
              <Card>
                <CardContent>
                  <Typography variant="h5" component="h2">
                    Solarstrahlung
                  </Typography>
                  <Typography variant="body2" component="p">
                    <iframe
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=auto&theme=dark&panelId=1"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427065585&to=1707427365586&theme=dark&panelId=2"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427193830&to=1707427493830&theme=dark&panelId=4"
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
                      src="http://localhost:8080/d-solo/e71298cd-3035-4e1f-b8dc-7ce15a33d4c9/wetterstation?orgId=1&refresh=30s&from=1707427226980&to=1707427526981&theme=dark&panelId=3"
                      width="1180"
                      height="500"
                      frameborder="0"
                    ></iframe>
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          </>
        )}
      </Grid>
    </div>
  );
}

export default ErstesOGRaum1;
