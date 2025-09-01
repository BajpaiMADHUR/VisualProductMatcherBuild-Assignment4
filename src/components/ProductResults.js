import React, { useState } from 'react';
import ProductCard from './ProductCard';
import '../styles.css';

const ProductResults = ({ products }) => {
  const [minSimilarity, setMinSimilarity] = useState(0);

  const filteredProducts = products.filter(
    (product) => product.similarity_score >= minSimilarity
  );

  return (
    <div className="results-container">
      <div className="results-header">
        <h2 className="results-heading">Similar Products ({filteredProducts.length})</h2>
        <div className="filter-group">
          <label htmlFor="similarity-filter" className="filter-label">Min. Similarity:</label>
          <input
            id="similarity-filter"
            type="range"
            min="0"
            max="1"
            step="0.01"
            value={minSimilarity}
            onChange={(e) => setMinSimilarity(parseFloat(e.target.value))}
            className="filter-input"
          />
          <span className="filter-value">{(minSimilarity * 100).toFixed(0)}%</span>
        </div>
      </div>
      {filteredProducts.length > 0 ? (
        <div className="product-grid">
          {filteredProducts.map((product, index) => (
            <ProductCard key={index} product={product} />
          ))}
        </div>
      ) : (
        <p className="no-results-message">No products found matching the criteria.</p>
      )}
    </div>
  );
};

export default ProductResults;