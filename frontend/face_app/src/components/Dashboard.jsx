import React from 'react'
import Admin from './Admin/Admin'
import Profile from './Profile'
import Login from './Login'
import Side from './Side'
import '../styles/dashboard.css'
import '../components//VideoStream'
import VideoStream from '../components//VideoStream'

const Dashboard = () => {
  return (
    <div className="dashboard">
    <Side  className="sidebar"/>
     <VideoStream className="vid"/>
     <Profile className="profile"/>
     

   </div>
  )
}

export default Dashboard