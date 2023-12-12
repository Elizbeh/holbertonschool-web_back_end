import kue from 'kue';

const  createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
        throw new Error(`Jobs is not an array`);
    }
    // create a job in the queue
    jobs.forEach((jobData) => {
        const jobCreated = queue.create('push_notification_code_3', jobData);

	jobCreated.on('enqueue', () => {
            console.log(`Notification job created: ${jobCreated.id}`)
	});

	jobCreated.on('complete', () => {
            console.log(`Notification job ${jobCreated.id} completed`)
	});

	jobCreated.on('failed', (err) => {
            console.log(`Notification job ${jobCreated
	} failed: ${err}`);
	});

	jobCreated.on('progress', (progress, data) => {
            console.log(`Notification job ${jobCreated.id} ${progress}% complete`);
	});
	jobCreated.save();
    });
}


export default createPushNotificationsJobs;
