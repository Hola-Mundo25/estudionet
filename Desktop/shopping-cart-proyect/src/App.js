import './App.css';
import React from 'react';
import Product from './components/Product/Product';
import Navbar from './components/Navbar/Navbar'
import Products from './components/Products';


function App() {
  return (
    <>
      <Navbar/>
      <Products/>
      {/* <Product/> */}
    </>
  );
}

export default App;
