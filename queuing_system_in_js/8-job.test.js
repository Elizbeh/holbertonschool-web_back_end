import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a queue with Kue and enter test mode
    queue = kue.createQueue({ disableSearch: true, testMode: true });
  });

  afterEach((done) => {
    // Clear the queue and exit test mode after executing the tests
    queue.testMode.clear();
    queue.testMode.exit();
    done();
  });

  it('display an error message if jobs is not an array', () => {
    // Call the function with a non-array argument and catch the error
    expect(() => createPushNotificationsJobs('notAnArray', queue)).to.throw('Jobs is not an array');

    // Ensure no jobs are added to the queue
    expect(queue.testMode.jobs.length).to.equal(0);
  });

  it('create two new jobs to the queue', async () => {
    // calls function with an array of 2 jobs
    const jobs = [
      { phoneNumber: '556', message: 'Message 1'},
      { phoneNumber: '775', message: 'Message 2'},
    ];

    // Use a Promise to wait for the asynchronous operation to complete
    await new Promise((resolve) => {
      createPushNotificationsJobs(jobs, queue);

      // Allow some time for the asynchronous operations to complete
      setTimeout(resolve, 2000);
    });

    // Ensure 2 jobs were added to the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Validate the details of the first job
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    // Validate the details of the second job
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});

