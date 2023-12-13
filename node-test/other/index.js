const letts = require('./module1');
const os = require('os');
const fs = require('fs');

fs.writeFile('./sexting.txt', 'ohh me vengo', () => {
    console.log('done');
})