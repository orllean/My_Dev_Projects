const people = ['Leo', 'Arthur', 'Brisa']
const one = 1
const str = 'Hello Word'
const b = true
const person = {
    firstName: 'Orlean',
    lastName: 'Costa'
}
function sayHello(person) {
    console.log('Hello ' + person.lastName)
}
console.log('--- typeof ---')
console.log(typeof people)
console.log(typeof one)
console.log(typeof str)
console.log(typeof b)
console.log(typeof person)
console.log(typeof sayHello)

console.log('--- isntanceof ---')
console.log(people instanceof Array)
console.log(one instanceof Number)
console.log(str instanceof String)
console.log(b instanceof Boolean)
console.log(person instanceof Object)
console.log(sayHello instanceof Function)

console.log('--- function ---')
console.log(sayHello(person))