import React from "react";

const DashboardPage: React.FC = () => {
  return (
    <div className="flex flex-col flex-1 bg-gray-900 text-white">
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 p-6">
        {/* Weather Summary Container */}
        <div className="bg-gray-800 p-4 rounded-lg shadow-md">
          <h2 className="text-xl font-bold text-orange-500">Weather Summary</h2>
          <p className="mt-2 text-gray-300">Temperature: 25°C</p>
          <p className="mt-1 text-gray-300">Humidity: 60%</p>
          <p className="mt-1 text-gray-300">Wind Speed: 12 km/h</p>
        </div>
        {/* Graph Container */}
        <div className="bg-gray-800 p-4 rounded-lg shadow-md lg:col-span-2">
          <h2 className="text-xl font-bold text-orange-500">Temperature Trends</h2>
          <div className="mt-4">
            {/* Placeholder for Graph */}
            <div className="h-48 bg-gray-700 rounded-md flex items-center justify-center">
              <span className="text-gray-400">Graph Placeholder</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
