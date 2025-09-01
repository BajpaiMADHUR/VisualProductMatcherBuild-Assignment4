from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Product Database: A Python list acting as a simple database (at least 50 products)
# Each product has a name, category, and image URL.
products = [
    {"id": 1, "name": "Classic Blue Denim Jeans", "category": "jeans", "image_url": "https://images.unsplash.com/photo-1624378439400-0967022f1546"},
    {"id": 2, "name": "Stylish Grey Blazer", "category": "blazer", "image_url": "https://images.unsplash.com/photo-1543087900-53e34311855a"},
    {"id": 3, "name": "White Polo Shirt", "category": "shirt", "image_url": "https://images.unsplash.com/photo-1620799140403-edc8651a2517"},
    {"id": 4, "name": "Black Leather Boots", "category": "footwear", "image_url": "https://images.unsplash.com/photo-1525966221132-c13f9c5462c1"},
    {"id": 5, "name": "Striped Red Tie", "category": "accessory", "image_url": "https://images.unsplash.com/photo-1542861295-d85c898396a8"},
    {"id": 6, "name": "Floral Summer Dress", "category": "dress", "image_url": "https://images.unsplash.com/photo-1596752763266-9e96e9e4a8d4"},
    {"id": 7, "name": "Khaki Cargo Shorts", "category": "shorts", "image_url": "https://images.unsplash.com/photo-1593457585094-187518001d9f"},
    {"id": 8, "name": "Navy Blue Winter Coat", "category": "coat", "image_url": "https://images.unsplash.com/photo-1601666497277-226e6378e9f5"},
    {"id": 9, "name": "Silver Watch", "category": "accessory", "image_url": "https://images.unsplash.com/photo-1523275371512-bc32433e46c7"},
    {"id": 10, "name": "Running Sneakers", "category": "footwear", "image_url": "https://images.unsplash.com/photo-1549298324-425211913348"},
    {"id": 11, "name": "Purple Backpack", "category": "bag", "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c3499"},
    {"id": 12, "name": "Denim Skirt", "category": "skirt", "image_url": "https://images.unsplash.com/photo-1579301072973-2280d92305c4"},
    {"id": 13, "name": "Leather Biker Jacket", "category": "jacket", "image_url": "https://images.unsplash.com/photo-1594916894082-f3801f409549"},
    {"id": 14, "name": "Green Hoodie", "category": "hoodie", "image_url": "https://images.unsplash.com/photo-1579296316499-c992d9d16a57"},
    {"id": 15, "name": "Elegant High Heels", "category": "footwear", "image_url": "https://images.unsplash.com/photo-1602148152341-a1e16f731118"},
    {"id": 16, "name": "Brown Leather Wallet", "category": "accessory", "image_url": "https://images.unsplash.com/photo-1611186871040-cf193c6d66e5"},
    {"id": 17, "name": "Checkered Flannel Shirt", "category": "shirt", "image_url": "https://images.unsplash.com/photo-1603242008779-6b5d63f25c78"},
    {"id": 18, "name": "Workout Leggings", "category": "leggings", "image_url": "https://images.unsplash.com/photo-1616588265880-60b702f3044a"},
    {"id": 19, "name": "Sporty Backpack", "category": "bag", "image_url": "https://images.unsplash.com/photo-1592659762303-90081d34b279"},
    {"id": 20, "name": "Gold Hoop Earrings", "category": "jewelry", "image_url": "https://images.unsplash.com/photo-1560965378-4384a8385a8a"},
    {"id": 21, "name": "Casual Blue Sneakers", "category": "footwear", "image_url": "https://images.unsplash.com/photo-1595952219808-f4e3c9710f81"},
    {"id": 22, "name": "Formal Black Suit", "category": "suit", "image_url": "https://images.unsplash.com/photo-1593721385412-f04646700f13"},
    {"id": 23, "name": "Light Pink Scarf", "category": "accessory", "image_url": "https://images.unsplash.com/photo-1598444158434-cf2a970e5138"},
    {"id": 24, "name": "Vintage Sunglasses", "category": "accessory", "image_url": "https://images.unsplash.com/photo-1591873832187-b6771d600645"},
    {"id": 25, "name": "Gray Sweatpants", "category": "sweatpants", "image_url": "https://images.unsplash.com/photo-1605330364402-23c2a0459c5d"},
    {"id": 26, "name": "Brown Loafers", "category": "footwear", "image_url": "https://images.unsplash.com/photo-1529124976735-e5f8f3c7e46e"},
    {"id": 27, "name": "Red Beanie Hat", "category": "headwear", "image_url": "https://images.unsplash.com/photo-1549487445-565538356947"},
    {"id": 28, "name": "White T-Shirt", "category": "shirt", "image_url": "https://images.unsplash.com/photo-1579633804473-2e06a3075253"},
    {"id": 29, "name": "Blue Swimsuit", "category": "swimsuit", "image_url": "https://images.unsplash.com/photo-1587375257521-4f1b8c199d79"},
    {"id": 30, "name": "Silver Necklace", "category": "jewelry", "image_url": "https://images.unsplash.com/photo-1620247477610-d7c38c03732b"},
    {"id": 31, "name": "Yellow Rain Jacket", "category": "jacket", "image_url": "https://images.unsplash.com/photo-1592327798367-a92c4d92a95c"},
    {"id": 32, "name": "Striped Jumper", "category": "jumper", "image_url": "https://images.unsplash.com/photo-1617196035849-c16f27b9b7e7"},
    {"id": 33, "name": "Black Leather Belt", "category": "accessory", "image_url": "https://images.unsplash.com/photo-1620786524388-c8c7d62f6b8a"},
    {"id": 34, "name": "Denim Overalls", "category": "overalls", "image_url": "https://images.unsplash.com/photo-1620799140403-edc8651a2517"},
    {"id": 35, "name": "Brown Leather Gloves", "category": "accessory", "image_url": "https://images.unsplash.com/photo-1607593259961-3a059d020a50"},
    {"id": 36, "name": "Green Bomber Jacket", "category": "jacket", "image_url": "https://images.unsplash.com/photo-1594916894082-f3801f409549"},
    {"id": 37, "name": "Red Running Shoes", "category": "footwear", "image_url": "https://images.unsplash.com/photo-1525966221132-c13f9c5462c1"},
    {"id": 38, "name": "Pink Purse", "category": "bag", "image_url": "https://images.unsplash.com/photo-1566895252873-19615a6b7d52"},
    {"id": 39, "name": "White Hoodie", "category": "hoodie", "image_url": "https://images.unsplash.com/photo-1616706930063-e3c6a469a47a"},
    {"id": 40, "name": "Gray Formal Shirt", "category": "shirt", "image_url": "https://images.unsplash.com/photo-1622340246221-d7d8f34f7863"},
    {"id": 41, "name": "Brown Beanie Hat", "category": "headwear", "image_url": "https://images.unsplash.com/photo-1549487445-565538356947"},
    {"id": 42, "name": "Black T-Shirt", "category": "shirt", "image_url": "https://images.unsplash.com/photo-1589133469853-5e93342337d1"},
    {"id": 43, "name": "Blue Formal Suit", "category": "suit", "image_url": "https://images.unsplash.com/photo-1593721385412-f04646700f13"},
    {"id": 44, "name": "Black Leather Pants", "category": "pants", "image_url": "https://images.unsplash.com/photo-1579296316499-c992d9d16a57"},
    {"id": 45, "name": "Yellow Hoodie", "category": "hoodie", "image_url": "https://images.unsplash.com/photo-1588107567812-78d10459c73d"},
    {"id": 46, "name": "Brown Leather Wallet", "category": "accessory", "image_url": "https://images.unsplash.com/photo-1611186871040-cf193c6d66e5"},
    {"id": 47, "name": "Running Sneakers", "category": "footwear", "image_url": "https://images.unsplash.com/photo-1549298324-425211913348"},
    {"id": 48, "name": "Stylish Grey Blazer", "category": "blazer", "image_url": "https://images.unsplash.com/photo-1543087900-53e34311855a"},
    {"id": 49, "name": "Casual Blue Sneakers", "category": "footwear", "image_url": "https://images.unsplash.com/photo-1595952219808-f4e3c9710f81"},
    {"id": 50, "name": "White Polo Shirt", "category": "shirt", "image_url": "https://images.unsplash.com/photo-1620799140403-edc8651a2517"},
]

@app.route('/api/search', methods=['POST'])
def search():
    """
    Handles search requests from the front-end.
    It accepts either a file upload or an image URL.
    """
    if 'image' in request.files:
        print("Image file received!")
    elif 'url' in request.form:
        print("Image URL received!")
    else:
        # Basic error handling
        return jsonify({"error": "No image file or URL provided"}), 400

    # In a real application, you would perform a visual search here
    # For this project, we'll simulate the results by returning a random subset
    import random
    
    # Get a random subset of 5 products from the database
    similar_products = random.sample(products, 5)

    # Assign a dummy similarity score (between 0.7 and 1.0)
    for product in similar_products:
        product['similarity_score'] = random.uniform(0.7, 1.0)

    # Return the list of products as a JSON response
    return jsonify({"similar_products": similar_products})

if __name__ == '__main__':
    app.run(debug=True)