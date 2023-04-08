import React from 'react'
import BarChart from '../components/Statistics/BarChart';
import Piechart from '../components/Statistics/PieChart';

const Statistics = () => {
  return (
    <div className="container">
      <div className='block'>
        <h2>Статистика данных</h2>
        <BarChart />
        <Piechart />
      </div>
    </div>
  )
}
export default Statistics;