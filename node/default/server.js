'use strict';

const express = require('express');

// Constants - Werden aus irgendeinen Grund nicht gefunden
const PORT = $PORT;
const HOST = $HOST;

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, HOST);
console.log(`Running on http:slash_slash${HOST}:${PORT}`);
