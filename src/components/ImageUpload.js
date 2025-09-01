import React, { useState } from 'react';
import { FaUpload, FaSearch } from 'react-icons/fa';
import '../styles.css';

const ImageUpload = ({ onSearch }) => {
  const [file, setFile] = useState(null);
  const [imageUrl, setImageUrl] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (e) => {
    const uploadedFile = e.target.files[0];
    setFile(uploadedFile);
    setImageUrl('');
  };

  const handleUrlChange = (e) => {
    setImageUrl(e.target.value);
    setFile(null);
  };

  const handleSearch = async () => {
    if (!file && !imageUrl) {
      alert('Please upload an image or enter a URL.');
      return;
    }

    setIsLoading(true);
    try {
      await onSearch({ file, imageUrl });
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="card">
      <h2 className="heading">Find Similar Products 🔎</h2>
      <div className="input-group">
        <label htmlFor="file-upload" className="label">Upload Image</label>
        <label htmlFor="file-upload" className="file-input-label">
          <FaUpload className="file-input-icon" />
          <p className="text-sm">Click to upload or drag and drop</p>
          {file && <p className="text-sm">File selected: {file.name}</p>}
        </label>
        <input id="file-upload" type="file" onChange={handleFileChange} style={{ display: 'none' }} />
      </div>
      <div className="or-divider">
        <span>OR</span>
      </div>
      <div className="input-group">
        <label htmlFor="image-url" className="label">Image URL</label>
        <input
          id="image-url"
          type="url"
          value={imageUrl}
          onChange={handleUrlChange}
          placeholder="e.g., https://example.com/product.jpg"
          className="text-input"
        />
      </div>
      <button
        onClick={handleSearch}
        className="btn-primary"
        disabled={isLoading}
      >
        {isLoading ? (
          <>
            <svg className="spinner" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" width="20" height="20">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span>Searching...</span>
          </>
        ) : (
          <>
            <FaSearch />
            <span>Search</span>
          </>
        )}
      </button>
      {(file || imageUrl) && (
        <div className="image-preview-container">
          <h3 className="preview-heading">Image to Search:</h3>
          {file && (
            <img src={URL.createObjectURL(file)} alt="Uploaded" className="preview-image" />
          )}
          {imageUrl && !file && (
            <img src={imageUrl} alt="From URL" className="preview-image" />
          )}
        </div>
      )}
    </div>
  );
};

export default ImageUpload;