import React from 'react'
import './Notice.css'
import PurchaseCard from '../components/NoticeCard';

const Notice = () => {
  return (
    <div className="container">
      <div className='block'>
        <h2>Данные о извещениях</h2>
        <div className='row1'>
          <PurchaseCard />
          <PurchaseCard />
          <PurchaseCard />
        </div>
        <div className='row2'>
          <PurchaseCard />
          <PurchaseCard />
          <PurchaseCard />
        </div>
      </div>
    </div>
  )
}
export default Notice;