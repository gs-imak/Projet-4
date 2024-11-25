import React from "react";
import { Link } from "react-router-dom";

const HomePage: React.FC = () => {
  return (
    <div className="container mx-auto mt-10 p-5 text-center">
      <h1 className="text-4xl font-bold text-blue-600">Welcome to Weather Analytics</h1>
      <p className="text-lg mt-4 text-gray-600">
        Analyze and interact with weather data for actionable insights.
      </p>
      <Link
        to="/dashboard"
        className="inline-block mt-6 px-6 py-3 bg-blue-500 text-white font-medium text-lg rounded hover:bg-blue-600"
      >
        Get Started
      </Link>
    </div>
  );
};

export default HomePage;
