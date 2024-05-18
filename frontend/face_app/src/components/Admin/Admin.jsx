import React from 'react'
import "../Addstudent"
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import PersonRemoveIcon from '@mui/icons-material/PersonRemove';
import SystemSecurityUpdateIcon from '@mui/icons-material/SystemSecurityUpdate';
import Studentlist from './Studentlist';
import { Link } from 'react-router-dom';





import './adminmenu.css'




const Admin = () => {
  return (
    <div className='adminpanel'>
      <div className="header">
      <h1 className='admix'>Admin Panel</h1>
      
      <div className="menu">
      <div className="box">
        <Link to="/studentprofile" className='item'>
          <b>Students </b>
          
          <AccountCircleIcon className='icon'/>
     </Link>
          </div>
          <div className="box">
          <Link to="/addstudent" className='item'>
            <b>ADDING </b>
          <AddCircleIcon className='icon'/>
        </Link>
          </div>
          <div className="box">
          <Link to='delete' className='item'>
          <b>REMOVE </b>
          <PersonRemoveIcon className='icon'/>
          </Link>
          </div>
          <div className="box">
          <Link to='#' className='item'>
            <b>UPDATE</b>
          <SystemSecurityUpdateIcon className='icon'/>
         </Link>
          </div>
      </div>

      </div>

    <div className="chart"> 
    <div className="chart__box">
    <h3 className='text'>Student List</h3>
  
    <Studentlist className="list"/>
    </div>
    </div>
        

      
    </div>
  )
}

export default Admin