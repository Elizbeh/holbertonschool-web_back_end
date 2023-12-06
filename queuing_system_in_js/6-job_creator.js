import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message',
};

const job = queue.create('push_notification_code', jobData);

job
  .on('complete', () => {
    console.log('Notification job completed');
    process.exit(0);
  })
  .on('failed', () => {
    console.log('Notification job failed');
    process.exit(1);
  })
  .on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  });

job.save((err) => {
  if (err) {
    console.error('Error creating job:', err);
    process.exit(1);
  }
});
