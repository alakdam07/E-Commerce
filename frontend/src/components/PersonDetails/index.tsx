import React, { useEffect, useState } from 'react'

interface Props {
  props: any;
}

const PersonDetails = (props) => {
  console.log(props.match.url);

  const [state, setstate] = useState<any>({
    customer: ``,
    products: []
  })

  useEffect(() => {
    const getData = async () => {
      const response = await fetch(`http://127.0.0.1:8000/api/customer-detail/${props.match.params.id}`);
      const data = await response.json()
      console.log(data);
      setstate({
        customer: data,
        product: data.products
      })

    }
    getData()
  }, [props.match.params.id])





  return (
    <>
      <div>
        {
          <p style={{ color: "red" }}>{state?.customer?.name}</p>

        }
        {
          state?.product?.map(i => <div key={i.id}><p >{i.name}</p></div>)
        }

      </div>
    </>)
}

export default PersonDetails;
