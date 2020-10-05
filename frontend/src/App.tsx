import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [state, setstate] = useState()
  useEffect(() => {
    getData()
  }, [])
  const getData = async () => {
    const order = await fetch('http://127.0.0.1:8000/api/order-list/')
    const orderData = await order.json();
    console.log("Order-Data", orderData);

    const response = await fetch('http://127.0.0.1:8000/api/customer-detail/9/');
    const data = await response.json()
    console.log(data);
    setstate(data)
  }
  console.log("Customer-List", state);

  return (
    <>
      <div className="App">
        {
          <p>{state?.name}</p>
        }

      </div>
    </>
  );
}

export default App;
