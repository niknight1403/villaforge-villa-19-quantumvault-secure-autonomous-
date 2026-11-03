import React, { useState } from 'react';

export const VaultUploader = () => {
  const [status, setStatus] = useState('idle');

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    setStatus('encrypting');
    try {
      // Simulated Client-Side Encryption via Web Crypto API
      const key = await window.crypto.subtle.generateKey(
        { name: 'AES-GCM', length: 256 },
        true,
        ['encrypt']
      );
      
      const fileData = await file.arrayBuffer();
      const iv = window.crypto.getRandomValues(new Uint8Array(12));
      const encrypted = await window.crypto.subtle.encrypt(
        { name: 'AES-GCM', iv },
        key,
        fileData
      );

      setStatus('uploading');
      // Upload logic to FastAPI Gateway
      console.log('Encrypted blob ready for upload:', encrypted.byteLength, 'bytes');
      setStatus('success');
    } catch (err) {
      console.error('Encryption failed', err);
      setStatus('error');
    }
  };

  return (
    <div className="p-6 bg-gray-900 text-white rounded-lg">
      <h2 className="text-xl font-bold mb-4">Zero-Knowledge Vault</h2>
      <input type="file" onChange={handleFileUpload} className="block w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:bg-blue-600 file:text-white" />
      <p className="mt-2">Status: {status}</p>
    </div>
  );
};