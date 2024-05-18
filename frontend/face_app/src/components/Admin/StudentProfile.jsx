import React, { useState } from "react";
import axios from "axios";
import { Button, TextField } from "@mui/material";
import './studentprofile.css'

import MailIcon from '@mui/icons-material/Mail';

import PermIdentityIcon from '@mui/icons-material/PermIdentity';
import ClassIcon from '@mui/icons-material/Class';
import EventSeatIcon from '@mui/icons-material/EventSeat';
import CardMembershipIcon from '@mui/icons-material/CardMembership';



const StudentProfile = () => {
  const [studentId, setStudentId] = useState("");
  const [studentData, setStudentData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchStudentData = async () => {
    setLoading(true);
    setError(null);
    try {
      // const response = await axios.get(`http://localhost:8000/admin/getstudent/${studentId}`);
      const response = await axios.get(`http://localhost:8000/admin/getstudent/${studentId}`);
      setStudentData(response.data);
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  };
  // onChange={(e) => setStudentId(e.target.value)}

  const handleSearchClick = () => {
    if (studentId.trim()) {
      fetchStudentData();
    } else {
      setError(new Error("Student ID cannot be empty"));
    }
  };

  return (
    <div className="profilepage">
        <div id="search-wrapper">

<i class="search-icon fas fa-search"></i>

<input type="text" id="search" placeholder="Insert student ID 🧑‍🎓  " onChange={(e) => setStudentId(e.target.value) }/>
<button id="search-button" onClick={handleSearchClick}>Search</button>


</div>
      {loading && <div>Loading...</div>}
      {error && <div>Error loading student data: {error.message}</div>}
      {/* {studentData && (
        <div>
          <h1>Student Profile</h1>
          <p>Name: {studentData.name}</p>
          <p>Email: {studentData.email}</p>
          <p>Status: {studentData.status}</p>
          <p>Department: {studentData.Department}</p>
          <p>Semester: {studentData.Semester}</p>
          <p>Section: {studentData.Section}</p>
          <p>Total Attendance: {studentData.Total_Attendance}</p>
          <p>Student ID: {studentData.id}</p>
        </div>
      )} */
      }
      {studentData && (

<div className="profile-card">
<div className="header">
  <img className="avatar" src="https://image.spreadshirtmedia.com/image-server/v1/compositions/T347A1PA4306PT17X38Y31D1041847581W17598H17598/views/1,width=550,height=550,appearanceId=1,backgroundColor=FFFFFF,noPt=true/cartoon-characters-womens-t-shirt.jpg" alt="profile" />
  <div className="header-info">
    <h2>{studentData.name}</h2>
    <p>{studentData.status}</p>
  </div> 
</div>
<div className="actions">
  <button>Follow</button>
  <button>Message</button>
  <button>More</button>
</div>
<div className="bio">
  <p>Hello</p>
</div>
<div className="information">
  <div className="info-item">
    <span><MailIcon className='icon'/></span>
    <p>{studentData.email}</p>
  </div>
  <div className="info-item">
  <span><EventSeatIcon className='icon'/></span>
    <p>{studentData.Total_Attendance}</p>
  </div>
  <div className="info-item">
  <span><PermIdentityIcon className='icon'/></span>
    <p>{studentData.Department}</p>
  </div>
  <div className="info-item">
  <span><CardMembershipIcon 
  className='icon'/></span>
    <p>{studentData.Semester}</p>

  </div>
  <div className="info-item">
  <span><ClassIcon className='icon'/></span>
    <p>{studentData.Section}</p>
    
  </div>
</div>
<div className="tags">
 
</div>
</div>

      )}
    
      
{/* 
<div className="profile-card">
      <div className="header">
        <img className="avatar" src="avatar.png" alt="profile" />
        <div className="header-info">
          <h2>{studentData.name}</h2>
          <p>{studentData.status}</p>
        </div> 
      </div>
      <div className="actions">
        <button>Follow</button>
        <button>Message</button>
        <button>More</button>
      </div>
      <div className="bio">
        <p>Hello</p>
      </div>
      <div className="information">
        <div className="info-item">
          <span>Email</span>
          <p>{studentData.email}</p>
        </div>
        <div className="info-item">
          <span>Total Attendance</span>
          <p>{studentData.Total_Attendance}</p>
        </div>
        <div className="info-item">
          <span>Department: </span>
          <p>{studentData.Department}</p>
        </div>
        <div className="info-item">
          <span>Semester </span>
          <p>{studentData.Semester}</p>

        </div>
        <div className="info-item">
          <span>Section </span>
          <p>{studentData.Section}</p>
          
        </div>
      </div>
      <div className="tags">
       
      </div>
    </div> */}
     
     

    </div>
  );
};

export default StudentProfile;
