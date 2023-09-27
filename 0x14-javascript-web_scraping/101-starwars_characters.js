#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const base = 'https://swapi-api.alx-tools.com/api/films/';
const url = base.concat(id);

request(url, function (error, res, body) {
  if (!error) {
    const { characters } = JSON.parse(body).results;
    characters.forEach((element) => {
      request(element, function (error, res, body) {
        if (!error) {
          const { name } = JSON.parse(body);
          console.log(name);
        }
      });
    });
    printChars(characters, 0);
  }
});
