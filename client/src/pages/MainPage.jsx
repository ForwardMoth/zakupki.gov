import React from 'react'
import logo from './logo.jpg';
import './MainPage.css'


const MainPage = () => {
  return (
    <div className="container">
      <div className='block'>
        <img src={logo} className="App-logo" alt="logo" />
        <h2>Главная страница</h2>
      </div> 
    </div>
  )
}

export default MainPage;