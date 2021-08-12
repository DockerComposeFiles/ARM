'use strict';

const express = require('express');

// Constants
//const PORT = 8080;
//const HOST = '172.25.1.2';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, HOST);
console.log(`Server is Running on http://${HOST}:${PORT}`);
