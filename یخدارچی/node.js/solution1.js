var readline = require("readline");
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

var x, y;

rl.on("line", function (line) {
  let T = parseInt(line);
  if (T < 0) {
    console.log("Ice");
  } else if (T > 100) {
    console.log("Steam");
  } else {
    {
      console.log("Water");
    }
  }
});

// a = readline()
