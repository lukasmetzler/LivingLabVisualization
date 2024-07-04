import React from "react";

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
              src="../images/grafana-logo.png"
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
              src="../images/monitoring-logo"
              alt="Monitoring Logo"
              className="h-16 mx-auto"
            />
            <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-100 text-center mt-4">
              Monitoring
            </h2>
          </a>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
