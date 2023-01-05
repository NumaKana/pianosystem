import AWS from 'aws-sdk';
import bluebird from 'bluebird';
const  promisifyAll = bluebird.promisifyAll
import exec from './exec.js';

import { fileURLToPath } from 'url';
import path from 'path';
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

startTimer('init');

import exec_ from 'child_process'

process.env.LAMBDA_TASK_ROOT = "/mnt/c/Users/kr814/workspace/pianosystem-1/deploy-2.23.6-1";

import a from 'fs'
const fs = promisifyAll(a);
const s3 = promisifyAll(new AWS.S3(), {suffix: "Mysuffix"});
const BUCKET = 'lilycompile-save-tmp';
const LY_DIR = `${process.env.LAMBDA_TASK_ROOT}/ly`;
const mime = {
  pdf: 'application/pdf',
  midi: 'audio/midi',
  png: 'image/png'
};

process.chdir('./file');
process.env.PATH += `:${LY_DIR}/usr/bin`;
process.env.LD_LIBRARY_PATH = `${LY_DIR}/usr/lib`;

//console.log(process.env)

function noop () {}

// Make sure this declaration is hoisted
var curTimer = null;
function startTimer(label) {
  if (curTimer) console.timeEnd(curTimer);
  if (label) console.time(label);
  curTimer = label;
}

function generateId() {
  return [
    Date.now(),
    ...process.hrtime(),
    Math.random().toString(36).substr(2)
  ].join('-');
}

exec_.exec('ls', (err, stdout, stderr) => {
  if (err) {
    console.log(`stderr: ${stderr}`)
    return
  }
  console.log(`stdout: ${stdout}`)
}
)

function runLilypond() {
  return exec(`${LY_DIR}/usr/bin/lilypond --formats=pdf --include="${__dirname}/fonts/font-stylesheets" -o rendered input.ly >&2`);
}

async function uploadFile(id, file, mode) {
  try {
    await s3.putObjectMysuffix({
      Bucket: BUCKET,
      Key: id,
      Body: await fs.readFileAsync(file),
      ContentType: mime[mode],
      StorageClass: 'REDUCED_REDUNDANCY'
    });
    return true;
  } catch (err) {
    return false;
  }
}

async function uploadFiles(id, result) {
  result.files = {
    pdf: await uploadFile(`${id}.pdf`, 'rendered.pdf', 'pdf'),
    midi: await uploadFile(`${id}.midi`, 'rendered.midi', 'midi')
  };

  return result;
}

async function run(event) {
  console.log('Received event:', JSON.stringify(event, null, 2));
  const id = event.id || generateId();

  startTimer('writing input');
  await Promise.all([
    fs.writeFileAsync('input.ly', event.code),
    fs.unlinkAsync('rendered.pdf').catch(noop),
    fs.unlinkAsync('rendered.midi').catch(noop)
  ]);

  startTimer('lilypond');
  let result = await runLilypond();
  result.id = id;

  startTimer('upload');
  result = await uploadFiles(id, result);

  startTimer(null);
  return result;
}

export function handler (event, context, callback) {
  run(event)
  .then(res => callback(null, res))
  .catch(err => {
    console.error('FAILING')
    callback(err)
  });
}