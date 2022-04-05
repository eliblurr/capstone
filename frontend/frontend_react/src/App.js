import * as React from 'react';
import logo from './logo.svg';
import TopBar from './components/TopBar';
import MenuBar from './components/MenuBar';
import './App.css';

import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

function App() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container spacing={0}>
        <Grid item xs={12}>
          <TopBar/>
        </Grid>
        <Grid item xs={4}>
        </Grid>
        <Grid item xs={4}>
          <Item>Content Heading</Item>
        </Grid>
        <Grid item xs={4}>
        </Grid>
        <Grid item xs={4}>
          <MenuBar/>
        </Grid>
        <Grid item xs={8}>
          <Item>Content</Item>
        </Grid>
      </Grid>
    </Box>
  );
}

export default App;
