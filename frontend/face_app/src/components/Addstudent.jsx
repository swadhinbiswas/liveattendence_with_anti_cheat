import React from 'react'
import "../styles/addstudent.css"
const Addstudent = () => {
  return (
    <div class="form">
    <form action="" class="form__content">
        <div class="form__box">
            <input type="text" class="form__input" placeholder="Enter Name" />
            <label for="" class="form__label">ENTER NAME</label>
            <div class="form__shadow"></div>
        </div>
        <div class="form__box">
            <input type="text" class="form__input" placeholder="Enter Student Mail" />
            <label for="" class="form__label">Enter Email</label>
            <div class="form__shadow"></div>
        </div>
        <div class="form__box">
            <input type="text" class="form__input" placeholder="Enter Department" />
            <label for="" class="form__label">Department</label>
            <div class="form__shadow"></div>
        </div>
        <div class="form__box">
            <input type="text" class="form__input" placeholder="Enter Status" />
            <label for="" class="form__label">Status</label>
            <div class="form__shadow"></div>
        </div>
        <div class="form__box">
            <input type="text" class="form__input" placeholder="Enter section" />
            <label for="" class="form__label">Section</label>
            <div class="form__shadow"></div>
        </div>
        <div class="form__box">
            <input type="text" class="form__input" placeholder="Enter student ID" />
            <label for="" class="form__label">STUDENT ID </label>
            <div class="form__shadow"></div>
        </div>
        <div class="form__box">
            <input type="email" class="form__input" placeholder="Total Attendence" />
            <label for="" class="form__label">Default 0</label>
            <div class="form__shadow"></div>
        </div>

        <div class="form__button">
            <input type="Submit" class="form__submit" value="Add Student" />
        </div>
    </form>
</div>
   
    
  )
}

export default Addstudent

