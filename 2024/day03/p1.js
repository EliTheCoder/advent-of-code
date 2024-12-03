let x = await Deno.readTextFile("./input.txt", "r")

let matches = x.match(/mul\(\d+,\d+\)/g)

let muls = matches.map(a => a.match(/mul\((\d+),(\d+)\)/)).map(b => +b[1] * +b[2])

console.log(muls.reduce((a,b) => a+b));