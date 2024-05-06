/**
 * connects to redis server on machine
 * logs message to console when connection works correctly/incorrectly.
 */
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

/**
 * function setNewSchool and displaySchoolValue
 * function display... modified to use async/await
 */

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
	try {
		const reply = await getAsync(schoolName);
		console.log(reply);
	} 	catch (error) {
		console.error(error);
	}
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
