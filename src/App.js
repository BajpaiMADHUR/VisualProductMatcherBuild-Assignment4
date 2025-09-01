import React, { useState } from 'react';
import axios from 'axios';
import ImageUpload from './components/ImageUpload';
import ProductResults from './components/ProductResults';
import './styles.css';

const API_ENDPOINT = 'http://127.0.0.1:5000/api/search';

function App() {
  const [results, setResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async ({ file, imageUrl }) => {
    setIsLoading(true);
    setError(null);
    setResults([]);

    try {
      const formData = new FormData();
      if (file) {
        formData.append('image', file);
      } else if (imageUrl) {
        formData.append('url', imageUrl);
      }

      const response = await axios.post(API_ENDPOINT, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setResults(response.data.similar_products);
    } catch (err) {
      console.error('API Error:', err);
      setError('Failed to fetch results. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container">
      <header className="header">
        <h1 className="heading">Visual Product Matcher 📸</h1>
        <p className="subheading">Find products by image</p>
      </header>

      <main>
        <ImageUpload onSearch={handleSearch} />

        {isLoading && <p className="loading-state">Searching for similar products...</p>}

        {error && <p className="error-state">Error: {error}</p>}

        {results.length > 0 && !isLoading && !error && (
          <ProductResults products={results} />
        )}
      </main>

      <footer className="footer">
        <p>Built as a Visual Product Matcher Project</p>
      </footer>
    </div>
  );
}

export default App;