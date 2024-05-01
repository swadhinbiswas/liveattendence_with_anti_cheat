import React, { useContext, useEffect, useState } from 'react';
import LogoDevRoundedIcon from '@mui/icons-material/LogoDevRounded';
import EmojiEmotionsIcon from '@mui/icons-material/EmojiEmotions';
import DashboardIcon from '@mui/icons-material/Dashboard';
import AdminPanelSettingsIcon from '@mui/icons-material/AdminPanelSettings';
import AssessmentIcon from '@mui/icons-material/Assessment';
import VerifiedUserIcon from '@mui/icons-material/VerifiedUser';
import LockIcon from '@mui/icons-material/Lock';
import HelpIcon from '@mui/icons-material/Help';
import '../styles/sidebar.css';
import '../components/DevInfo';
import ImageAvatars from '../components/Imageavater';

const Side = () => {
 

  return (
    <div className='menu'>

      <div className='logo'>
        <EmojiEmotionsIcon className='icon'/>
        <h3>Face App </h3>
      </div>
        <div className="menu-list">
          <a href='#' className='item'>
            <DashboardIcon className='icon'/>
            Dashboard</a>
            <a href='#' className='item'>
            <AdminPanelSettingsIcon className='icon'/>
            Admin</a>
            <a href='#' className='item'>
            <AssessmentIcon className='icon'/>
            Report</a>
            <a href='#' className='item'>
            <VerifiedUserIcon className='icon'/>
            Verifaction</a>
            <a href='#' className='item'>
            <LockIcon className='icon'/>
            Block</a>
            <a href='#' className='item'>
            <HelpIcon className='icon'/>
            Help</a>
            
        </div>
        <div className='divinfo'>
        <h3>Developers <LogoDevRoundedIcon className='icon'/></h3>
        
          <ImageAvatars/>



        </div>
        

       

  

      </div>
      
   
    
)
  
}

export default Side