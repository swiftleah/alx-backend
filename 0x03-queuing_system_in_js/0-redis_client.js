/**
 * connects to redis server on machine
 * logs message to console when connection works correctly/incorrectly.
 */
import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
	console.log('Redis client connected to the server');
});
