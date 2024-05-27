import React from "react";
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography'
import { styled } from '@mui/material/styles';
import products from './product-data'
import CheckOutCard from "./CheckOutCard";

const useStyle = styled((theme) => ({
    root: {
        flexGrow: 1,
        padding: "2rem",
    },
}))

const CheckOutPage = () =>{
    const classes = useStyle()

function FormRow() {
    return(
        <>
        {products.map((product)=>
            <Grid product xs={12} sm={8} lg={4}>
                <CheckOutCard key={product.id} product={product}/>
            </Grid>
        )}
        </>
    );
}

return (
    <div className={classes.root}>
        <Grid container spacing={3}>
            <Grid item xs={12}>
                <Typography align="center" gutterBottom variant="h4">
                    Shopping cart
                </Typography>
            </Grid>
            <Grid item xs={12} sm={8} md={9} container spacing={2}>
                <FormRow />
            </Grid>
            <Grid item xs={12} sm={4} md={3}>
                <Typography align="center" gutterBottom variant="h4">
                    Total
                </Typography>
            </Grid>
        </Grid>
    </div>
)
}

export default CheckOutPage