import React from "react";
import { Link } from "react-router-dom";

const Sidebar: React.FC = () => {
  return (
    <div className="h-screen bg-gray-900 text-white w-64 flex flex-col">
      <div className="p-4 text-2xl font-bold text-orange-500">WeatherApp</div>
      <nav className="flex-1">
        <ul className="space-y-2 p-4">
          <li>
            <Link
              to="/dashboard"
              className="flex items-center p-2 text-gray-300 hover:bg-gray-800 rounded-md"
            >
              <span className="text-sm">Dashboard</span>
            </Link>
          </li>
          <li>
            <Link
              to="/settings"
              className="flex items-center p-2 text-gray-300 hover:bg-gray-800 rounded-md"
            >
              <span className="text-sm">Settings</span>
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;
