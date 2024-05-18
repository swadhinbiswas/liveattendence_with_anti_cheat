import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import "../styles/addstudent.css";

const BaseUrl = "http://localhost:8000/admin/create";

const Addstudent = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    status: '',
    Department: '',
    Semester: '',
    Section: '',
    Total_Attendance: '',
    id: ''
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(BaseUrl, formData, {
        headers: {
          'Content-Type': 'application/json',
          'accept': 'application/json'
        }
      });
      console.log('Student added successfully:', response.data);
      navigate(`/student/${response.data.id}`); 
    } catch (error) {
      console.error('Error adding student:', error);
    }
  };

  return (
    <div className="form">
      <form onSubmit={handleSubmit} className="form__content">
        <div className="form__box">
          <input
            type="text"
            name="name"
            className="form__input"
            placeholder="Enter Name"
            value={formData.name}
            onChange={handleChange}
          />
          <label className="form__label">ENTER NAME</label>
          <div className="form__shadow"></div>
        </div>
        <div className="form__box">
          <input
            type="text"
            name="email"
            className="form__input"
            placeholder="Enter Student Mail"
            value={formData.email}
            onChange={handleChange}
          />
          <label className="form__label">Enter Email</label>
          <div className="form__shadow"></div>
        </div>
        <div className="form__box">
          <input
            type="text"
            name="Department"
            className="form__input"
            placeholder="Enter Department"
            value={formData.Department}
            onChange={handleChange}
          />
          <label className="form__label">Department</label>
          <div className="form__shadow"></div>
        </div>
        <div className="form__box">
          <input
            type="text"
            name="Semester"
            className="form__input"
            placeholder="Enter Semester"
            value={formData.Semester}
            onChange={handleChange}
          />
          <label className="form__label">Semester</label>
          <div className="form__shadow"></div>
        </div>
        <div className="form__box">
          <input
            type="text"
            name="status"
            className="form__input"
            placeholder="Enter Status"
            value={formData.status}
            onChange={handleChange}
          />
          <label className="form__label">Status</label>
          <div className="form__shadow"></div>
        </div>
        <div className="form__box">
          <input
            type="text"
            name="Section"
            className="form__input"
            placeholder="Enter section"
            value={formData.Section}
            onChange={handleChange}
          />
          <label className="form__label">Section</label>
          <div className="form__shadow"></div>
        </div>
        <div className="form__box">
          <input
            type="text"
            name="id"
            className="form__input"
            placeholder="Enter student ID"
            value={formData.id}
            onChange={handleChange}
          />
          <label className="form__label">STUDENT ID</label>
          <div className="form__shadow"></div>
        </div>
        <div className="form__box">
          <input
            type="text"
            name="Total_Attendance"
            className="form__input"
            placeholder="Total Attendance"
            value={formData.Total_Attendance}
            onChange={handleChange}
          />
          <label className="form__label">Default 0</label>
          <div className="form__shadow"></div>
        </div>

        <div className="form__button">
          <input type="submit" className="form__submit" value="Add Student" />
        </div>
      </form>
    </div>
  );
};

export default Addstudent;
