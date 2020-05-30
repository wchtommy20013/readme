#!/usr/bin/env node
process.stdout.write(require('../dist/index').init(process.argv.slice(2)).toString() + "\n");


