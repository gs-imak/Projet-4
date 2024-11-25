import React from "react";

const Header: React.FC = () => {
  return (
    <header className="bg-gray-800 text-white p-4 flex justify-between items-center">
      <h1 className="text-lg font-bold">Dashboard</h1>
      <div>
        <button className="bg-orange-500 text-white px-4 py-2 rounded hover:bg-orange-600">
          Logout
        </button>
      </div>
    </header>
  );
};

export default Header;
