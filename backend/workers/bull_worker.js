const { Worker } = require('bullmq');
const Redis = require('ioredis');
const { generateReport } = require('../config/bullmq_config');

const connection = new Redis({
  host: 'localhost',
  port: 6379
});

// Define the worker to process reports
const reportWorker = new Worker('reportQueue', async (job) => {
  console.log(`Processing report for ${job.data.industry} - ${job.data.tier}`);

  try {
    const report = await generateReport(job.data.industry, job.data.tier);
    console.log(`Report generated: ${report}`);
    return report;
  } catch (error) {
    console.error('Report generation failed:', error);
    throw error;
  }
}, { connection });

// Handle worker errors
reportWorker.on('failed', (job, err) => {
  console.error(`Job ${job.id} failed with error: ${err.message}`);
});

reportWorker.on('completed', (job) => {
  console.log(`Job ${job.id} completed successfully!`);
});

console.log('BullMQ report worker is running...');
