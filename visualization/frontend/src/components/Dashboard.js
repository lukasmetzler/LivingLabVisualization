import React from "react";
import grafanaLogo from "../images/grafana-logo.png";
import monitoringLogo from "../images/monitoring-logo.png";
import TableComponent from "../components/TableComponent"; // Anpassen des Pfades entsprechend Ihrer Ordnerstruktur

const Dashboard = () => {
  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100">
          Dashboard
        </h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <a
            href="http://85.215.59.47/grafana/"
            className="bg-white dark:bg-gray-800 p-4 rounded shadow hover:bg-gray-200 dark:hover:bg-gray-700"
          >
            <img
              src={grafanaLogo}
              alt="Grafana Logo"
              className="h-16 mx-auto"
            />
            <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-100 text-center mt-4">
              Grafana
            </h2>
          </a>
          <a
            href="http://85.215.59.47/monitoring/"
            className="bg-white dark:bg-gray-800 p-4 rounded shadow hover:bg-gray-200 dark:hover:bg-gray-700"
          >
            <img
              src={monitoringLogo}
              alt="Monitoring Logo"
              className="h-16 mx-auto"
            />
            <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-100 text-center mt-4">
              Monitoring
            </h2>
          </a>
        </div>
        <div className="mt-6">
          <TableComponent />
        </div>
        <div className="mt-6">
          <iframe
            src="http://85.215.59.47/grafana/d-solo/dba558fd-aa9d-49d9-a9de-99f38ee4c45c/1-og-raum-1?orgId=1&refresh=30s&from=1720127881185&to=1720129681185&theme=dark&panelId=2"
            width="450"
            height="200"
            frameborder="0"
          ></iframe>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
