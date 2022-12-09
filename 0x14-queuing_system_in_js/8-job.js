function createPushNotificationsJobs(jobs, queue) {
  if (Object.getPrototypeOf(jobs) !== Array.prototype) throw Error('Jobs is not an array');
    jobs.forEach((jData) => {
        const job = queue.create('push_notification_code_3', jData).save((error) => {
            if (!error) console.log(`Notification job created: ${job.id}`);
        });
        job.on('complete', () => console.log(`Notification job ${job.id} completed`));
        job.on('failed', (error) => console.log(`Notification job ${job.id} failed: ${error}`));
        job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`));
    });
}

export default createPushNotificationsJobs;
