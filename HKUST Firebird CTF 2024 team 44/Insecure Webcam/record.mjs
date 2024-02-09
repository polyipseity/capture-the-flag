import { Recorder } from 'node-rtsp-recorder';

// rtsp://a1668k:f1r3b1rd@10.211.55.6:8554/firebird_secure/
var rec = new Recorder({
  url: 'rtsp://a1668k:f1r3b1rd@10.211.55.6:8554/firebird_secure/trackID=0',
  timeLimit: 5, // time in seconds for each segmented video file
  folder: './',
  name: 'recordings',
})
// Starts Recording
rec.startRecording();

setTimeout(() => {
  console.log('Stopping recording')
  rec.stopRecording()
  rec = null
}, 10000)
