var mic, recorder, soundFile;

var state = 0; // mousePress will increment from Record, to Stop, to Play

function setup() {
  createCanvas(400,400);
  

  // create an audio in
  mic = new p5.AudioIn();

  // users must manually enable their browser microphone for recording to work properly!
  mic.start();

  // create a sound recorder
  recorder = new p5.SoundRecorder();

  // connect the mic to the recorder
  recorder.setInput(mic);

  // create an empty sound file that we will use to playback the recording
  soundFile = new p5.SoundFile();
}

function draw() {
  background(200);
  fill(0);
  micLevel = mic.getLevel();
  text('Mic volume: ' + str(micLevel), 20, 40);

  if (micLevel > 0.001) {
    fill(0,255,0);
  }
  rect(20,60,50,50);
}

function mousePressed() {
  // use the '.enabled' boolean to make sure user enabled the mic (otherwise we'd record silence)
  if (state === 0 && mic.enabled) {

    // Tell recorder to record to a p5.SoundFile which we will use for playback
    recorder.record(soundFile);

    fill(255,0,0);
    ellipse(100,100,50,50);
    text('Recording now! Click to stop.', 20, 20);
    // state++;
  }

  else if (state === 1) {
    recorder.stop(); // stop recorder, and send the result to soundFile

    fill(0,255,0);
    ellipse(100,100,50,50);
    text('Recording stopped. Click to play & save', 20, 20);
    // state++;
  }

  else if (state === 2) {
    soundFile.play(); // play the result!
    var fileName = 'mySound.wav';
    // maveSound(soundFile, fileName); // save file
    // state++;
    postFile(soundFile, fileName);
  }
}

function mouseReleased() {
  state = (state + 1) % 3;
}

function upload(postUrl, file) {
  var formData = new FormData();
  formData.append("filee", file);
  // var req = new XMLHttpRequest();

  // req.open("POST", postUrl);
  // req.onload = function(event) { alert(event.target.responseText); };
  console.log(formData);
  console.log(formData.get("filee"));
  // req.send(formData);

  $.ajax({
    type: 'POST',
    url: postUrl,
    data: formData,
    processData: false,
    contentType: false
  }).done(function(data) {
        console.log("done");
       console.log(data);
       console.log('done2');
  });
}

function postFile(wavFile, name) {
  postUrl = '../configurations/compute/';
  fieldName = 'data';
  filePath = wavFile;
  data = mySaveSound(wavFile, name);
  // blobToFile(data, name);
  console.log(data);
  var blob = new Blob([data], {'type': 'application/octet-stream'});
  var fileOfBlob = new File([blob], 'wei.wav');
  upload(postUrl, fileOfBlob);
}

function blobToFile(theBlob, fileName){
  //A Blob() is almost a File() - it's just missing the two properties below which we will add
  theBlob.lastModifiedDate = new Date();
  theBlob.name = fileName;
}

// helper methods to save waves
function interleave(leftChannel, rightChannel) {
  var length = leftChannel.length + rightChannel.length;
  var result = new Float32Array(length);
  var inputIndex = 0;
  for (var index = 0; index < length;) {
    result[index++] = leftChannel[inputIndex];
    result[index++] = rightChannel[inputIndex];
    inputIndex++;
  }
  return result;
}
function writeUTFBytes(view, offset, string) {
  var lng = string.length;
  for (var i = 0; i < lng; i++) {
    view.setUint8(offset + i, string.charCodeAt(i));
  }
}

/**
 *  Save a p5.SoundFile as a .wav audio file.
 *
 *  @method saveSound
 *  @param  {p5.SoundFile} soundFile p5.SoundFile that you wish to save
 *  @param  {String} name      name of the resulting .wav file.
 */
function mySaveSound(soundFile, name) {
  var leftChannel, rightChannel;
  leftChannel = soundFile.buffer.getChannelData(0);
  // handle mono files
  if (soundFile.buffer.numberOfChannels > 1) {
    rightChannel = soundFile.buffer.getChannelData(1);
  } else {
    rightChannel = leftChannel;
  }
  var interleaved = interleave(leftChannel, rightChannel);
  // create the buffer and view to create the .WAV file
  var buffer = new window.ArrayBuffer(44 + interleaved.length * 2);
  var view = new window.DataView(buffer);
  // write the WAV container,
  // check spec at: https://ccrma.stanford.edu/courses/422/projects/WaveFormat/
  // RIFF chunk descriptor
  writeUTFBytes(view, 0, 'RIFF');
  view.setUint32(4, 36 + interleaved.length * 2, true);
  writeUTFBytes(view, 8, 'WAVE');
  // FMT sub-chunk
  writeUTFBytes(view, 12, 'fmt ');
  view.setUint32(16, 16, true);
  view.setUint16(20, 1, true);
  // stereo (2 channels)
  view.setUint16(22, 2, true);
  view.setUint32(24, 44100, true);
  view.setUint32(28, 44100 * 4, true);
  view.setUint16(32, 4, true);
  view.setUint16(34, 16, true);
  // data sub-chunk
  writeUTFBytes(view, 36, 'data');
  view.setUint32(40, interleaved.length * 2, true);
  // write the PCM samples
  var lng = interleaved.length;
  var index = 44;
  var volume = 1;
  for (var i = 0; i < lng; i++) {
    view.setInt16(index, interleaved[i] * (32767 * volume), true);
    index += 2;
  }
  p5.prototype.writeFile([view], name, 'wav');
  return view;
};