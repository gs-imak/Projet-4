import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const Sidebar: React.FC = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false); // actual auth state
  const navigate = useNavigate();

  const handleAuthButtonClick = () => {
    if (isLoggedIn) {
      setIsLoggedIn(false);
    } else {
      navigate("/login");
    }
  };

  return (
    <div className="h-screen bg-gray-800 text-white w-64 flex flex-col justify-between">
      <div>
        <div className="p-4 text-2xl font-bold text-orange-700">WeatherApp</div>
        <nav>
          <ul className="space-y-2 p-4">
            <li>
              <Link
                to="/dashboard"
                className="flex items-center p-2 text-gray-300 hover:bg-orange-800 rounded-md"
              >
                <span className="text-sm">Dashboard</span>
              </Link>
            </li>
            <li>
              <Link
                to="/settings"
                className="flex items-center p-2 text-gray-300 hover:bg-orange-800 rounded-md"
              >
                <span className="text-sm">Settings</span>
              </Link>
            </li>
          </ul>
        </nav>
      </div>
      <div className="p-4">
        <button
          onClick={handleAuthButtonClick}
          className="w-full bg-orange-500 text-white py-2 rounded-2xl hover:bg-orange-600">
          {isLoggedIn ? "Logout" : "Login"}
        </button>
      </div>
    </div>
  );
};

export default Sidebar;