import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import AddShoppingCart from '@mui/icons-material/AddShoppingCart';
import { Badge } from '@mui/material';
// import logo from '../assets/vs_logo.png'

    export default function Navbar() {
    return (
        <Box sx={{ flexGrow: 1 }}>
        <AppBar position="fixed">
            <Toolbar>
            <IconButton
                size="large"
                edge="start"
                color="inherit"
                aria-label="menu"
                sx={{ mr: 1 }}
            >
            {/* <img src={logo}/> */}
            </IconButton>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                Shopping cart
            </Typography>
            <Button color="inherit">Login</Button>
            <IconButton aria-label='show cart items' color="inherit">
                <Badge badgeContent={2} color='red'>
                    <AddShoppingCart fontSize='large' />
                </Badge>
            </IconButton>
            </Toolbar>
        </AppBar>
        </Box>
    );
    }