// Javascript program to print all the prime numbers upto n

const prompt = require("prompt-sync")({sigint: true});

function prime(n) {
    if (n < 2) {
        return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

function printprime(n) {
    for (let i = 2; i <= n; i++) {
        if (prime(i)) {
            console.log(i);
        }
    }
}

let n = prompt("Enter a number- ");
printprime(n)
