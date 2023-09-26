#!/usr/bin/node

const request = require("request");
const id = process.argv[2];
const base = "https://swapi-api.alx-tools.com/api/films/";
const url = base.concat(id);

request(url, (error, res, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
