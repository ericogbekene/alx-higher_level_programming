#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      /* pass */
    }
  }

  print () {
    for (let i = 0; i <= this.height - 1; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tempW = this.width;
    this.width = this.height;
    this.height = tempW;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
