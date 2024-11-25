import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import DashboardPage from "./pages/Dashboard";

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex h-screen">
        <Sidebar />
        <div className="flex flex-col flex-1">
          <Header />
          <Routes>
            <Route path="/dashboard" element={<DashboardPage />} />
            {/* Additional routes can go here */}
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
