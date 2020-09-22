#!/usr/bin/node
const firstSquare = require('./5-square');
class Square extends firstSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 1; i <= this.height; i++) {
        for (let j = 1; j <= this.width; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  }
}
module.exports = Square;
