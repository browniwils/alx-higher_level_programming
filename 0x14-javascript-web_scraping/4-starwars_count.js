#!/usr/bin/node

const request = require("request");
const API = process.argv[2];
let movies = 0;

request(API, (error, res, body) => {
  if (error) {
    console.error(error);
  }
  const results = JSON.parse(body).results;
  for (const index in results) {
    const char = results[index].characters;
    for (const x in char) {
      if (char[x].includes("18")) {
        movies += 1;
      }
    }
  }
  console.log(movies);
});
