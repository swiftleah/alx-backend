import kue from 'kue';

const queue = kue.createQueue();

const jobdata = {
	phoneNumber: '0709934576',
  	message: 'hi, it is me!',
};

const job = queue.create('push_notification_code', jobdata);

job.on('enqueue', () => {
	console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
	console.log('Notification job completed');
});

job.on('failed', () => {
	console.log('Notification job failed');
});

job.save();
