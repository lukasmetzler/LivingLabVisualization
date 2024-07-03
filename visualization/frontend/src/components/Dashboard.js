import React from "react";

const Dashboard = () => {
  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100">
          Dashboard
        </h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-6">
          <div className="bg-white dark:bg-gray-800 p-4 rounded shadow">
            <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-100">
              Statistik 1
            </h2>
            <p className="mt-2 text-gray-600 dark:text-gray-300">
              Hier könnte eine Beschreibung oder Statistik stehen.
            </p>
          </div>
          <div className="bg-white dark:bg-gray-800 p-4 rounded shadow">
            <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-100">
              Statistik 2
            </h2>
            <p className="mt-2 text-gray-600 dark:text-gray-300">
              Hier könnte eine Beschreibung oder Statistik stehen.
            </p>
          </div>
          <div className="bg-white dark:bg-gray-800 p-4 rounded shadow">
            <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-100">
              Statistik 3
            </h2>
            <p className="mt-2 text-gray-600 dark:text-gray-300">
              Hier könnte eine Beschreibung oder Statistik stehen.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
