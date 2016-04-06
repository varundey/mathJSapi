
var q = (process.argv[2]);
var workerpool = require('workerpool');
var pool = workerpool.pool(__dirname + '/math_worker.js');

var TIMEOUT = 10000; // milliseconds

  var expr = q;
  if (expr === undefined) {
    console.log("None");
    process.exit(0);
  }

  pool.exec('evaluate', [expr])
      .timeout(TIMEOUT)
      .then(function (result) {
        console.log(result);
        process.exit(0);
      })
      .catch(function (err) {
        console.log("None",err);
        process.exit(0);
      });


