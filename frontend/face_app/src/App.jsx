import React from 'react'
import Dashboard from './components/Dashboard'
import {BrowserRouter,Route,Routes} from 'react-router-dom'
import Login from './components/Login'
import Addstudent from './components/Addstudent'
import Admin from './components/Admin/Admin'
import StudentProfile from './components/Admin/StudentProfile'
import Delete from './components/Admin/Delete' 





const App = () => {
  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Login/>} />
      <Route path='/dashboard' element={<Dashboard/>} />
      <Route path='/addstudent' element={<Addstudent/>} />
      <Route path='admin' element={<Admin/>} />
      <Route path='studentprofile' element={<StudentProfile/>} />
      <Route path="delete" element={Delete} />
     

      
      
     
    </Routes>
    </BrowserRouter>
    
  )
}

export default App