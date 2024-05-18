import React from 'react'

const Delete = () => {
  const [studentId, setStudentId] = useState("");
  const [studentData, setStudentData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchStudentData = async () => {
    setLoading(true);
    setError(null);
    try {
      // const response = await axios.get(`http://localhost:8000/admin/getstudent/${studentId}`);
      const response = await axios.get(`http://localhost:8000/admin/deletestudent/${studentId}`);
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

      {studentData && (
        <div>
         <p>
          {studentData}
         </p>
        </div>
      )
      }


</div>

   
  )
}

export default Delete