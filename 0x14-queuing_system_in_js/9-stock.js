import express from 'express';
import { promisify } from 'util';
import kue from 'kue';

const listProducts = [
    {
        itemId: 1,
        itemName: 'Suitcase 250',
        price: 50,
        initialAvailableQuantity: 4,
    },
    {
        itemId: 2,
        itemName: 'Suitcase 450',
        price: 100,
        initialAvailableQuantity: 10,
    },
    {
        itemId: 3,
        itemName: 'Suitcase 650',
        price: 350,
        initialAvailableQuantity: 2,
    },
    {
        itemId: 4,
        itemName: 'Suitcase 1050',
        price: 550,
        initialAvailableQuantity: 5,
    },
];

// get item by id
function getItemById(itemId) {
    return listProducts.find((item) => item.itemId === itemId);
}

// express server
const app = express();
app.listen(1245, () => {
    console.log('API available on localhost port 1245');
});

app.get('/list_products', (req, res) => {
    res.json(listProducts);
}
);

// redis connection
const queue = kue.createQueue();
const get = promisify(queue.client.get).bind(queue.client);
const set = promisify(queue.client.set).bind(queue.client);

// purchase
app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    if (!item) {
        res.status(404).send('Item not found');
    } else {
        const { initialAvailableQuantity } = item;
        const key = `availableQuantity${itemId}`;
        const availableQuantity = await get(key);
        if (availableQuantity) {
            if (availableQuantity > 0) {
                const newAvailableQuantity = availableQuantity - 1;
                await set(key, newAvailableQuantity);
                res.json({ status: 'Reservation confirmed', itemId });
            } else {
                res.json({ status: 'Not enough stock available', itemId });
            }
        } else {
            if (initialAvailableQuantity > 0) {
                const newAvailableQuantity = initialAvailableQuantity - 1;
                await set(key, newAvailableQuantity);
                res.json({ status: 'Reservation confirmed', itemId });
            } else {
                res.json({ status: 'Not enough stock available', itemId });
            }
        }
    }
}
);
