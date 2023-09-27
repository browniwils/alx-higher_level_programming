#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const base = 'https://swapi-api.alx-tools.com/api/films/';
const url = base.concat(id);

request(url, function (error, res, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printChars(characters, 0);
  }
});

function printChars(characters, index) {
  request(characters[index], function (error, res, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printChars(characters, index + 1);
      }
    }
  });
}
