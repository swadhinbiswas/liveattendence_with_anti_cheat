import React, { useState } from "react";
import axios from "axios";
import { Button, TextField } from "@mui/material";
import './studentprofile.css'
import SearchIcon from '@mui/icons-material/Search';

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
      <div className="search">

      <TextField label="Outlined secondary" color="secondary" className=".search-input"
       focused 
       onChange={(e) => setStudentId(e.target.value)}/>
       
       <Button variant="contained" endIcon={<SearchIcon  className="icon"/>}>
  Search
</Button>
      </div>
      {loading && <div>Loading...</div>}
      {error && <div>Error loading student data: {error.message}</div>}
       {studentData && (
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
// Path: liveattendence_with_anti_cheat/frontend/face_app/public/test.jsx