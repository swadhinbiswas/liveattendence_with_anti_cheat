import React from 'react'
import "../Addstudent"
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import PersonRemoveIcon from '@mui/icons-material/PersonRemove';
import SystemSecurityUpdateIcon from '@mui/icons-material/SystemSecurityUpdate';


import './adminmenu.css'




const Admin = () => {
  return (
    <div className='adminpanel'>

      <div className="menu">
      <div className="box">
        <a href='#' className='item'>
          <AccountCircleIcon className='icon'/>
     </a>
          </div>
          <div className="box">
          <a href='#' className='item'>
          <AddCircleIcon className='icon'/>
        </a>
          </div>
          <div className="box">
          <a href='#' className='item'>
          <PersonRemoveIcon className='icon'/>
          </a>
          </div>
          <div className="box">
          <a href='#' className='item'>
          <SystemSecurityUpdateIcon className='icon'/>
         </a>
          </div>
      </div>

    <div className="chart"> 
<h1> test</h1>

    
    </div>
        

      
    </div>
  )
}

export default Admin