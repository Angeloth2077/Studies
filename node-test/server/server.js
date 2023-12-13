const http = require('http');
const fs = require('fs');
const _ = require('lodash');


// ----------------------------Creating the server using the http method--------------------------
const server = http.createServer((req, res) => {


 // --------------------------Setting up the paths for different url's--------------------------
    let path = './';
    
    switch (req.url) {
        case '/':
            path += 'index.html';
            res.statusCode = 200;
        break;
        case '/blog':
            path += 'blog.html';
            res.statusCode = 200;
        break;
        case '/about':
            path += 'about.html';
            res.statusCode = 200;
        break;
        case '/about-me':
            res.statusCode = 301;
            res.setHeader('Location', '/about');
        break;
        default:
            path += '404.html';
            res.statusCode = 404;
        break;
    }


 // --------------------------Making the responce of the server-----------------------------
    fs.readFile(path, {encoding: 'utf-8'}, (err, data) => {
        if(err) {
            console.log(err);
            res.end();
        }else{
            res.setHeader('Content-Type', 'text/html');
            res.write(data);
            res.end();
        }
    });
});

// ---------------------------------Adding the listener of the server on port 3000-------------------------
server.listen(3000, 'localhost', () => {
    console.log('Listening on port 3000');
    console.log(num);
});