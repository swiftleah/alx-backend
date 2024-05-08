import { expect } from chai;
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs' () => {
	let queue;

	beforeEach(() => {
		queue = kue.createQueue({
