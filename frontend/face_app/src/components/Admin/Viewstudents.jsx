import React from 'react'
import { DataGridPro } from '@mui/x-data-grid';
import Box from '@mui/material/Box';
import { useDemoData } from '@mui/x-data-grid-generator';


const Viewstudents = () => {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 100000,
    editable: true,
  });

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGridPro
        {...data}
        checkboxSelection
        disableSelectionOnClick
        density="compact"
      />
    </Box>
  )
}

export default Viewstudents