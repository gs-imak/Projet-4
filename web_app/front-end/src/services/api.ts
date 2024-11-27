const BASE_URL = "http://localhost:8000";

/**
 * Helper function to handle HTTP requests.
 * @param endpoint - The API endpoint (e.g., '/auth/login').
 * @param options - Fetch options such as method, headers, and body.
 * @returns The JSON response from the API.
 */
const apiFetch = async (endpoint: string, options: RequestInit = {}) => {
  try {
    const token = localStorage.getItem("token");

    // Add Authorization header if a token exists
    const headers = {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    };

    const response = await fetch(`${BASE_URL}${endpoint}`, {
      ...options,
      headers,
    });

    if (!response.ok) {
      // Handle HTTP errors
      const error = await response.text();
      throw new Error(`API Error: ${response.status} ${error}`);
    }

    // Parse JSON response
    return response.json();
  } catch (error) {
    console.error("API Request Failed:", error);
    throw error;
  }
};

/**
 * API Service functions for specific endpoints
 */

// Login API
export const login = async (username: string, password: string) => {
  return apiFetch("/auth/login", {
    method: "POST",
    body: JSON.stringify({ username, password }),
  });
};

// Fetch data from ElasticSearch
export const searchElastic = async (query: string) => {
  return apiFetch("/elasticsearch/search", {
    method: "POST",
    body: JSON.stringify({ query }),
  });
};

// Query data from Hadoop
export const queryHadoop = async (filePath: string) => {
  return apiFetch("/hadoop/query", {
    method: "POST",
    body: JSON.stringify({ file_path: filePath }),
  });
};
