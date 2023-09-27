#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const name = process.argv[3];

request(url, (error, res, body) => {
  if (error) {
    console.error(error);
  }

  fs.writeFile(name, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
