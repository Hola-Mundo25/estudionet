import  React from 'react';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardActions from '@mui/material/CardActions';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import accouting from "accounting"
import DeleteIcon from '@mui/icons-material/Delete';

// Para ver stylos ver 02:00:00 edel video.

    export default function CheckOutCard({product:{id, name, productType, image, price, rating, description}}) {

    return (
        <Card  style={{ margin: '100px 10px 50px 10px' }} sx={{ maxWidth: 300 }}>
        <CardHeader
            action={
            <Typography
                variant='h5'
                color='textSecondary'
            >
            {/*en caso de querer cambiar la moneda insertamos un
            segundo parametro luego del valor (50, "aqui")*/}
            {accouting.formatMoney(price)} 
            </Typography>
            }
            title={name}
        />
        <CardMedia 
        image={image}
        style={{ height: '200px', width: '300px' }}     
        title={name}/>

        <CardActions disableSpacing>
            <div>
            {Array(rating)
                .fill()
                .map((_, i)=>(
                    <p>&#11088;</p>
                ))}
            </div>
            <IconButton aria-label="share">
                <DeleteIcon fontSize='large'/>
            </IconButton>
        </CardActions>

        </Card>
    );
    }
