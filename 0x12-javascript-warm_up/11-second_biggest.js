#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
    console.log('0');
} else {
    let max = parseInt(args[0]);
    let prevMax = ''


    for (let i = 0; i < args.length; i++) {
        let intArg = parseInt(args[i])
        if (max < intArg) {
            prevMax = max;
            max = intArg;
        }
    }
    console.log(`${prevMax}`);
}