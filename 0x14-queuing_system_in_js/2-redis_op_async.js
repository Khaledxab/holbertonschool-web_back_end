'use strict';

const { promisify } = require('util');

import redis from 'redis';
const client = redis.createClient();
const client2 = promisify(client.get).bind(client);

client.on("error", (error) => {
  if (error) console.log(`Redis client not connected to the server: ${error}`)
}).on('ready', () => {
    console.log('Redis client connected to the server');
});

// add setNewSchool function 
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// add displaySchoolValue function
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
    }

(async() => {
  await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();


//call the functions
//setNewSchool('HolbertonSanFrancisco', '100');
//displaySchoolValue('Holberton');
//displaySchoolValue('HolbertonSanFrancisco');
