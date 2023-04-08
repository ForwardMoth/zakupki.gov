import React from 'react'
import ContractCard from '../components/ContractCard';

const Contracts = () => {
  return (
    <div className="container">
      <div className='block'>
        <h2>Данные о контрактах</h2>
        <div className='row1'>
          <ContractCard />
          <ContractCard /> 
          <ContractCard /> 
        </div>
        <div className='row2'>
          <ContractCard />
          <ContractCard /> 
          <ContractCard /> 
        </div>
      </div>
    </div>
  )
}
export default Contracts;