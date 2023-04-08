import React, { useState } from 'react'
import Button from 'react-bootstrap/Button';

const Parser = () => {

    const [message, setMessage] = useState("");
    let startParser = async () => {

        let res = await fetch("http://127.0.0.1:3444/api/v1/parser/start_all", {
        method: "GET",
        mode: "cors"
        });
        if (res.status === 200) {
            setMessage("Загрузка данных начата");
        } 
        else {
            setMessage("Возникла ошибка, загрузка начата не была");
        }
      };
 
  return (
    <div className="container">
      <div className='block'>
        <h2>Загрузка данных</h2>
        <Button onClick={() => startParser()} variant="light">
            Начать загрузку данных
        </Button>
        <div className="message">{message ? <p>{message}</p> : null}</div>
      </div>
    </div>
  )
}
export default Parser;