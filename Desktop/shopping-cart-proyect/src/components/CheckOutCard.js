import  React from 'react';
import { styled } from '@mui/material/styles';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardActions from '@mui/material/CardActions';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
import accouting from "accounting"


    interface ExpandMoreProps extends React.ComponentProps<typeof IconButton> {
    expand: boolean;
    }


    const ExpandMore = styled(({ expand, ...other }: ExpandMoreProps) => (
    <IconButton {...other} />
    ))(({ theme, expand }) => ({
    transform: expand ? 'rotate(180deg)' : 'rotate(0deg)',
    marginLeft: 'auto',
    transition: theme.transitions.create('transform', {
        duration: theme.transitions.duration.shortest,
    }),
    }));

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
            subheader="in stock"
        />
        <CardMedia
            image={image}
        />

        <CardActions disableSpacing>
            <IconButton aria-label="share">
            <AddShoppingCartIcon />
            </IconButton>
            <ExpandMore
            >
            <ExpandMoreIcon />
            </ExpandMore>
        </CardActions>

        </Card>
    );
    }
