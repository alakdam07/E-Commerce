import React, { ReactElement, useEffect, useState } from 'react'
import { Link } from "react-router-dom";

interface Props {
  props: any
}

function Home(props): ReactElement {
  // console.log("From home", props);

  const [state, setstate] = useState([])
  useEffect(() => {
    getData()
  }, [])
  const getData = async () => {
    const order = await fetch('http://127.0.0.1:8000/api/order-list/')
    const orderData = await order.json();
    //console.log(orderData);

    setstate(orderData)
  }
  //console.log("Duplicate", Object.values(state.reduce((acc, cur: any) => Object.assign(acc, { [cur.id]: cur }), {})));

  const data = state.map((i: any) => i?.customer?.name)
  const customer = new Set(data)

  return (
    <>
      <div className="App">
        {
          state.map((person: any, index: number) => {
            return (
              <ul key={index} style={{ listStyle: "none" }}>

                <li style={{ color: "white" }}>
                  {new Set(person?.customer?.name)}
                </li>

                <li style={{ width: 200, background: "white" }}>

                  <Link
                    to={"/customer-detail/" + person.customer.id}
                  >
                    Edit
                </Link>
                </li>
              </ul>

            )
          })

        }




      </div>
    </>)
}

export default Home;
