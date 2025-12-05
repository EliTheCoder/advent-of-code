const fs = require("fs");
let a = fs.readFileSync("./input.txt", "utf-8");
let nums = "one two three four five six seven eight nine".split(" ")

let b = a.split("\n").map((x, ind, arr) => {
    let found = false;
    for (let i = 0; i < x.length && found == false; i++) {
        let uu = x.substring(i);
        for (let j = 0; j < nums.length; j++) {
            if (uu.charAt(0).match(/[0-9]/)) {
                found = true;
                break;
            }
            if (uu.match(new RegExp("^"+nums[j]))) {
                x = x.substring(0, i) + (j+1) + x.substring(i+nums[j].length)
                found = true;
                break;
            }
        }
    }
    found = false;
    for (let i = x.length-1; i >= 0 && found == false; i--) {
        let uu = x.substring(i);
        for (let j = 0; j < nums.length; j++) {
            if (uu.charAt(0).match(/[0-9]/)) {
                found = true;
                break;
            }
            if (uu.match(new RegExp("^"+nums[j]))) {
                x = x.substring(0, i) + (j+1) + x.substring(i+nums[j].length)
                found = true;
                break;
            }
        }
    }
    console.log(arr[ind]);
    console.log(x);
    x = x.replaceAll(/[^0-9]/g, "");
    let ao = x.charAt(0) + x.charAt(x.length-1);
    console.log(ao);
    console.log()
    return ao;
});
b.pop();
let c = b.map(Number);

console.log(c.reduce((x,y) => x+y))
