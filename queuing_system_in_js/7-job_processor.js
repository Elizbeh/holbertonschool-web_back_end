import kue from 'kue';

// Create an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  // Track the progress of the job
  job.progress(0, 100);

  // Check if the phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Update the progress to 50%
  job.progress(50, 100);

  // Log the notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Simulate notification sending
  setTimeout(() => {
    // Complete the job
    done();
  }, 1000); // Simulate 1 second notification sending time
};

const queue = kue.createQueue();

// Set up queue processing, allowing two jobs to be processed simultaneously
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract data from the job
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});
