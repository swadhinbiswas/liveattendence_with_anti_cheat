import React from "react";
import "../styles/profile.css";

const Profile = () => {
  return (
    <div className="card-containe">
      <span className="card">ID</span>
      <img
        className="round"
        src="https://randomuser.me/api/portraits/women/79.jpg"
        alt="profile"
      />
      <h3 className="stu">John Doe</h3>
      <h3 className="stu"> Student</h3>
      <h3 className="stu"> 3rd Year</h3>
      <h3 className="stu"> ID:1234567890</h3>
      <h3 className="stu"> DOB: 01/01/2000</h3>
      <h3 className="stu">All:</h3>
    </div>
  );
};

export default Profile;
