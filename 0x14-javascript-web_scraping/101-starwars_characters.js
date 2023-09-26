#!/usr/bin/node

const request = require("request");
const id = process.argv[2];
const base = "https://swapi-api.alx-tools.com/api/films/";
const url = base.concat(id);

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    let charactersProcessed = 0;
    const characterNames = [];

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const char = JSON.parse(body).name;
          characterNames.push(char);
        }
        charactersProcessed++;

        if (charactersProcessed === characters.length) {
          characterNames.forEach((actor) => {
            console.log(actor);
          });
        }
      });
    });
  } else {
    console.log(error);
  }
});
