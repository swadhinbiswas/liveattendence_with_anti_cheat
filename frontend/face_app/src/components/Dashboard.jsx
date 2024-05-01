import React from 'react'
import Admin from './Admin/Admin'
import Profile from './Profile'
import Login from './Login'
import Side from './Side'
import '../styles/dashboard.css'

const Dashboard = () => {
  return (
    <div className="dashboard">
    <Side  className="sidebar"/>
     <Login className="admin" />
     <Profile className="profile"/>
     

   </div>
  )
}

export default Dashboard