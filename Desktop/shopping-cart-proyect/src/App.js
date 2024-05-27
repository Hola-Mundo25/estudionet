import './App.css';
import React from 'react';
import Navbar from './components/Navbar/Navbar'
// import Products from './components/Products';
import CheckOutPage from './components/CheckOutPage';
function App() {
  return (
    <>
      <Navbar/>
      {/* <Products/> */}
      <CheckOutPage/>
      {/* <Product/> */}
    </>
  );
}

export default App;
