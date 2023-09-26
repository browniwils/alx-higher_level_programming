#!/usr/bin/node

const request = require("request");
const url = process.argv[2];

request(url, (error, res, body) => {
  if (error) {
    console.error(error);
  }
  console.log(`code: ${res.statusCode}`);
});
