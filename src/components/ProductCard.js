import React from 'react';
import '../styles.css';

const ProductCard = ({ product }) => {
  return (
    <div className="product-card">
      <img
        src={product.image_url}
        alt={product.name}
        className="product-image"
      />
      <div className="product-info">
        <h3 className="product-name">{product.name}</h3>
        <p className="product-category">{product.category}</p>
        <div className="similarity-score">
          Similarity: <span>{(product.similarity_score * 100).toFixed(2)}%</span>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;