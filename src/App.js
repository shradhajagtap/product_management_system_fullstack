import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [orders, setOrders] = useState([]);
  const [form, setForm] = useState({
    product_name: "",
    product_price: "",
    product_quan: "",
  });

  // Fetch all orders
  const fetchOrders = () => {
    fetch("http://127.0.0.1:8000/api/orders/")
      .then((res) => res.json())
      .then((data) => setOrders(data))
      .catch((err) => console.error("GET Error:", err));
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  // Input handler
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Add Product
  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:8000/api/orders/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to add product");
        return res.json();
      })
      .then(() => {
        fetchOrders(); // refresh table
        setForm({ product_name: "", product_price: "", product_quan: "" }); // clear form
      })
      .catch((err) => console.error("POST Error:", err));
  };

  return (
    <div className="App">
      <h1>🛍️ Product Management System</h1>

      <div className="form">
        <input
          type="text"
          name="product_name"
          placeholder="Product Name"
          value={form.product_name}
          onChange={handleChange}
        />
        <input
          type="number"
          name="product_price"
          placeholder="Price"
          value={form.product_price}
          onChange={handleChange}
        />
        <input
          type="number"
          name="product_quan"
          placeholder="Quantity"
          value={form.product_quan}
          onChange={handleChange}
        />
        <button onClick={handleSubmit}>➕ Add Product</button>
      </div>

      <h2>📋 Orders List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Product</th>
            <th>Price</th>
            <th>Quantity</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.product_name}</td>
              <td>₹{item.product_price}</td>
              <td>{item.product_quan}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
