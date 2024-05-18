import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid } from '@mui/x-data-grid';

import axios from 'axios';

const BaseUrl = 'http://localhost:8000/admin/getstudents'; // Corrected typo

const columns = [
  { field: 'id', headerName: 'Student ID', width: 130 }, // Adjusted width for ID
  { field: 'name', headerName: 'Name', width: 180 }, // Combined first and last name
  { field: 'Department', headerName: 'Department', width: 150 },
  { field: 'Section', headerName: 'Section', width: 100 },
  { field: 'Semester', headerName: 'Semester', width: 100 },
  { field: 'Total_Attendance', headerName: 'Attendance', width: 130 },
  { field: 'email', headerName: 'Email', width: 200 },
  { field: 'last_seen', headerName: 'Last Seen', width: 180 },
  { field: 'status', headerName: 'Status', width: 120 },
];

const StudentList = () => {
  const [rows, setRows] = React.useState([]); // Initialize empty state

  React.useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(BaseUrl);
        const formattedData = Object.entries(response.data).map(([studentId, studentData]) => ({
          id: studentId, // Use student ID as unique identifier
          ...studentData, // Spread remaining student data
          name: `${studentData.name || ''}`, // Handle potential missing names
        }));
        setRows(formattedData);
      } catch (error) {
        console.error('Error fetching student data:', error);
        // Handle errors gracefully (e.g., display an error message)
      }
    };

    fetchData();
  }, []);

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 5,
            },
          },
        }}
        pageSizeOptions={[5]}
        checkboxSelection
        disableRowSelectionOnClick
      />
    </Box>
  );
};

export default StudentList;
