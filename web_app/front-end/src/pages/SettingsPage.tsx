import React, { useState } from "react";

const SettingsPage: React.FC = () => {
  const [formData, setFormData] = useState({
    name: "",
    password: "",
  });

  const [successMessage, setSuccessMessage] = useState("");

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/api/update-user", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setSuccessMessage("Profile updated successfully!");
      } else {
        setSuccessMessage("Failed to update profile. Please try again.");
      }
    } catch (error) {
      setSuccessMessage("An error occurred. Please try again later.");
    }
  };

  // Reset form
  const handleReset = () => {
    setFormData({ name: "", password: "" });
    setSuccessMessage("");
  };

  return (
    <div className="bg-gray-900 text-white min-h-screen p-6">
      <div className="max-w-xl mx-auto bg-gray-800 p-6 rounded-lg shadow-lg">
        <h2 className="text-2xl font-bold text-orange-500 mb-4">Modify your profile</h2>
        {successMessage && (
          <p className="text-sm text-green-500 mb-4">{successMessage}</p>
        )}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="name" className="block text-gray-300">
              Name
            </label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="w-full p-2 bg-gray-700 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"
            />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-gray-300">
              Password
            </label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="w-full p-2 bg-gray-700 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"
            />
          </div>
          <div className="flex space-x-4">
            <button
              type="submit"
              className="bg-orange-500 text-white px-4 py-2 rounded-lg hover:bg-orange-600"
            >
              Save Changes
            </button>
            <button
              type="button"
              onClick={handleReset}
              className="bg-gray-700 text-white px-4 py-2 rounded-lg hover:bg-gray-600"
            >
              Reset
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default SettingsPage;
