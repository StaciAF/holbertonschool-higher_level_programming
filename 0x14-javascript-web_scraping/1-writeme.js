#!/usr/bin/node
#!/usr/bin/node
const process = require('process');
const fileName = process.argv[2];
const data = process.argv[3];
const fs = require('fs');
fs.writeFile(fileName, data, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
