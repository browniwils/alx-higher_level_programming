#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (!err) {
    const data = JSON.parse(body);
    const users = {};

    data.forEach((element) => {
      if (element.completed && users[element.userId] === undefined) {
        users[element.userId] = 1;
      } else if (element.completed) {
        users[element.userId] += 1;
      }
    });
    console.log(users);
  }
});
