import React from 'react'

import Admin from './components/Admin'
import Profile from './components/Profile'
import Side from './components/Side'
import './App.css'


const App = () => {
  return (
    <div className="dashboard">
     <Side  className="sidebar"/>
      <Admin className="admin" />
      <Profile className="profile"/>
      

    </div>
  )
}

export default App