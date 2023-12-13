const express = require('express');

// --------------------Setup an Express app---------------------

const app = express();

// --------------------Listen for request-----------------------

app.listen(3000);

app.get('/', (req, res) => {
    res.sendFile('./index.html', {root: __dirname});
});

app.get('/about', (req, res) => {
    res.sendFile('./about.html', {root: __dirname});
});