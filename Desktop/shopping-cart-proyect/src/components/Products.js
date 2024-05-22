import * as React from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Product from './Product/Product';
import products from './product-data'


export default function Products() {
return (
    <Box sx={{ width: '100%' }}>
    <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
        {
            products.map(product =>
            <Grid item xs={12} sm={6} md={4} lg={3}>
                <Product key={product.id} product={product}/>
            </Grid>
        )
        }
    </Grid>
</Box>
);
}
