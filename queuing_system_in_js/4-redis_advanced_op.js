import { createClient } from 'redis';
import redis from 'redis';

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.hset('HolbertonSchools', 'Portland', 50, (err, reply) => {
    if (err) {
        console.error(`Error setting Portland: ${err}`);
    } else {
        console.log(`Reply: ${reply}`);
    }
});

client.hset('HolbertonSchools', 'Seatle', 80, (err, reply) => {
    if (err) {
        console.error(`Error setting Seatle: ${err}`);
    } else {
        console.log(`Reply: ${reply}`);
    }
});

client.hset('HolbertonSchools', 'New York', 20, (err, reply) => {
    if (err) {
        console.error(`Error setting Portland: ${err}`);
    } else {
        console.log(`Reply: ${reply}`);
    }
});

client.hset('HolbertonSchools', 'Bogota', 20, (err, reply) => {
    if (err) {
        console.error(`Error setting Bogota: ${err}`);
    } else {
        console.log(`Reply: ${reply}`);
    }
});

client.hset('HolbertonSchools', 'Cali', 40, (err, reply) => {
    if (err) {
        console.error(`Error setting Cali: ${err}`);
    } else {
        console.log(`Reply: ${reply}`);
    }
});

client.hset('HolbertonSchools', 'Paris', 2, (err, reply) => {
    if (err) {
        console.error(`Error setting Paris: ${err}`);
    } else {
        console.log(`Reply: ${reply}`);
    }
});

client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) throw err;
    console.log(reply);
});
