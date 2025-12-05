let x = await Deno.readTextFile("./input.txt", "r")

let matches = x.match(/(mul\(\d+,\d+\))|(do\(\))|don\'t\(\)/g)

let active = true;
let muls = matches.map(a => a.match(/(mul|do|don't)\((\d*),?(\d*)\)/)).map((a,i) => {
    if (a[1] == "mul") {
        if (active) return a[2] * a[3];
        else return 0;
    }
    if (a[1] == "do") {
        active = true;
        return 0;
    }
    if (a[1] == "don't") {
        active = false;
        return 0;
    }
    console.log(a)
})

console.log(muls)

console.log(muls.reduce((a,b) => a+b));