import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../services/api";

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const data = await login(username, password);
      localStorage.setItem("token", data.access_token);
      setError(null);
      navigate("/dashboard");
    } catch (err) {
      setError("Invalid username or password.");
    }
  };

  return (
    <div className="bg-gray-800 container mx-auto mt-10 p-5">
      <h2 className="text-2xl font-bold text-center text-orange-600">Login</h2>
      {error && <p className="text-red-500 text-center">{error}</p>}
      <form onSubmit={handleLogin} className="max-w-md mx-auto mt-5 space-y-4">
        <div>
          <label className="block text-orange-600">Username</label>
          <input
            type="text"
            className="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label className="block text-orange-600">Password</label>
          <input
            type="password"
            className="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button
          type="submit"
          className="w-full bg-orange-500 text-white py-2 rounded-2xl hover:bg-orange-600">
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
