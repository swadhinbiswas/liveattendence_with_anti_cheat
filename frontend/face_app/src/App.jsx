import React from 'react'
import Dashboard from './components/Dashboard'
import {BrowserRouter,Route,Routes} from 'react-router-dom'
import Login from './components/Login'
import Adminpage from './components/Adminpage'




const App = () => {
  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Login/>} />
      <Route path='/dashboard' element={<Dashboard/>} />
      <Route path='/admin' element={<Adminpage/>} />
    </Routes>
    </BrowserRouter>
    
  )
}

export default App