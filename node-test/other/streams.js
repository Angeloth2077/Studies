const fs = require('fs');
const rstream = fs.createReadStream('./kaine.txt');
const wstream = fs.createWriteStream('./kaine2.txt');

//rstream.on('data', (buffer) => {
//    console.log(buffer);
//    wstream.write(buffer);
//})

rstream.pipe(wstream);