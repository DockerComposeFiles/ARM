'use strict';

const express = require('express');

// Constants
const PORT = 8081;
const HOST = '172.25.1.2';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, HOST);
console.log(`Running on http:slash_slash${HOST}:${PORT}`);
