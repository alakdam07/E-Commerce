import React, { useEffect, useState } from 'react';

import './App.css';

function App() {
  const [state, setstate] = useState([])
  useEffect(() => {
    getData()
  }, [])
  const getData = async () => {
    const response = await fetch('http://127.0.0.1:8000/api/order-list/');
    const data = await response.json()
    console.log(data);
    setstate(data)
  }
  console.log("state", state);

  return (
    <div className="App">
      {
        state.map((i: any) => {
          return <p> {i.customer.name}</p>
        })
      }
    </div>
  );
}

export default App;
