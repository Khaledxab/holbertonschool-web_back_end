import { createClient } from "redis";
import { Expres } from "express";
import { promisify } from "util";
import kue from "kue";

// redis
const client = createClient();
const get = promisify(client.get).bind(client);

// kue 
const queue = kue.createQueue();

// express
const app = express();

// func
const reserveSeat = (number) => {
client.set('available_seats', number);
};

// ""


// route
reserveSeat(50);
let reservationEnabled = true;

app.get ('available_seats', async (req, res) => {
    const key = `available_seats`;
    const value = await get(key);
    res.json({ number: value });
    });

app.get ('rprocess', (req, res) => {
    res.json({ status: 'prcessing' });
    queue.process('reserve_seat', (job, done) => {
        reserveSeat(job.data.number);
        done();
    }
    );
    });

app.get ('reserve_seat', (req, res) => {
    const number = req.query.number;
    if (reservationEnabled) {
        const job = queue.create('reserve_seat', { number }).save((err) => {
            if (!err) console.log(`Reservation job created: ${job.id}`);
        });
        job.on('complete', () => {
            console.log('Reservation job completed');
        });
        job.on('failed', () => {
            console.log('Reservation job failed');
        });
        res.json({ status: `Reservation job created ${job.id}` });
    } else {
        res.json({ status: 'Reservation failed' });
    }
    }
    );


// port = 1245;
app.listen(1245, () => {
    console.log('API available on localhost port 1245');
    }
    );

