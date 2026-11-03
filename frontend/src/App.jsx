import React, { useState } from 'react';

export default function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-900 text-white">
        <div className="p-8 bg-gray-800 rounded-lg shadow-xl">
          <h1 className="text-2xl font-bold mb-4">QuantumVault AI Login</h1>
          <button 
            onClick={() => setIsAuthenticated(true)} 
            className="w-full bg-blue-600 hover:bg-blue-700 py-2 px-4 rounded"
          >
            Sign In
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <header className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">QuantumVault Dashboard</h1>
        <button onClick={() => setIsAuthenticated(false)} className="text-sm text-gray-400">Logout</button>
      </header>
      <main className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="p-6 bg-gray-800 rounded-lg">Secure Storage</div>
        <div className="p-6 bg-gray-800 rounded-lg">Agent Auditor</div>
        <div className="p-6 bg-gray-800 rounded-lg">Billing</div>
      </main>
    </div>
  );
}