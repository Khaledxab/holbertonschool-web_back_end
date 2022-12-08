import kue from 'kue';
const queue = kue.createQueue();

const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100);
    // send notification
    job.progress(50, 100);
    // send notification
    job.progress(100, 100);
    done();
    }

queue.process('push_notification_code', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
    }
);

