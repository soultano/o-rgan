import React from "react";
import { Route, Routes } from "react-router-dom";
import "./App.css";

import { Register } from "./components/Register/Register.js";
import Logicals from "./components/logical/logical";
import Category from "./components/kategory/categorys";

function App() {
  return (
    <>
      {/* Ro'yxatnoma yo'nalishi */}
      <Routes>
        <Route path="/" element={<Register />} />
      </Routes>

      {/* Kategoriya yo'nalishi */}
      <Routes>
        <Route path="/Category" element={<Category />} />
      </Routes>

      {/* IQ testi yo'nalishi */}
      <Routes>
        <Route path="/IQ" element={<Logicals />} />
      </Routes>
    </>
  );
}

export default App;
 