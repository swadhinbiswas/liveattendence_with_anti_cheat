import React from 'react'
import AlternateEmailIcon from '@mui/icons-material/AlternateEmail';
import PasswordIcon from '@mui/icons-material/Password';
import Fingerprint from '@mui/icons-material/Fingerprint';
import '../styles/login.css'


const Login = () => {
  

  return (
    <div className='container'>
    <div className='login'>
      
      <div className='loginvid'>
      
     <img  className='imagex' src='https://raw.githubusercontent.com/swadhinbiswas/liveattendence_with_anti_cheat/main/frontend/face_app/src/assets/faceapp.gif' alt='login' />
      </div>
      <div className='inputs'>
      <h1 className='logintext'>Login</h1>
        <div className="input">
          <AlternateEmailIcon className='icon' />
          <input type='email' placeholder='email' />
        </div>
        <div className="input">
          <PasswordIcon className='icon' />
          <input type='password' placeholder='password' />
        </div>
        <div className="input">
        <Fingerprint className='icon' />
          <input className='loginbtn' type='Button' value='Login' />
          
        </div>
      
      </div>
     
    </div>
    </div>
  )
}

export default Login