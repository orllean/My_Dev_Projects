/* Estrutura
function name(params) {
    instrução
    retrun #opcional
}
# variáveis dentro de uma função só podem ser usadas nelas
# retrun - encerra a função e pode retornar um valor a ser utilizado

*/
//Função anônima
const soma = function (a, b) {
	return a + b;
};
const soma2 = (a, b) => {
	return a + b;
};
//console.log(soma2(2, 8));
//console.log(soma(3, 5));
//console.log(soma(5, 8));

//Função autoinvocavel
(function () {
	let name = "1-orlean";
	//return console.log(name);
})();

(function fullName(a, b) {
	let name = a + " " + b;
	//return console.log(name);
})("2-orlean", "costa");

const fullName = (function (a, b) {
	let name = a + " " + b;
	return name;
})("3-orlean", "costa");
//console.log(fullName);
(() => console.log(`Welcome ${fullName}!`))();
// callback
function calc(opc, a, b) {
	return opc(a, b);
}
function sum1(a, b) {
	return a + b;
}
function sub(a, b) {
	return a - b;
}
console.log(calc(sum1, 3, 9));
console.log(calc(sub, 3, 9));
//parametro padrão
function mult(a = 1, b = 1) {
	return a * b;
}
console.log(mult());

//parametro indefinido e uso do arguments
function findMax() {
	let max = -Infinity;
	for (let i = 0; i < arguments.length; i++) {
		if (arguments[i] > max) {
			max = arguments[i];
		}
	}
	return max;
}
console.log(findMax(-1, -12, -354, -23));
// arrays spread - permite ihterar seus elementos
function sum(a, s, d) {
	return a + s + d;
}
const numbers = [2, 3, 4, 5]; //apenas a quantidade de equivalente a de argumentos será usada
console.log(sum(...numbers));

let numberStore = [0, 1, 2];
let newNumber = 12;

// numberStore = [numberStore, newNumber]; [ [ 0, 1, 2 ], 12 ]
numberStore = [...numberStore, newNumber]; // [ 0, 1, 2, 12
console.log(numberStore);

function fullname2(name, surname) {
	return name + " " + surname;
}
let people = ["4-orlean", "costa"];
console.log(fullname2(...people));

// arrays rest - The rest parameter syntax allows a function to accept an indefinite number of arguments as an array, providing a way to represent variadic functions in JavaScript. combina seus elementos em um array
function myFun(...theArgs) {
	console.log(theArgs);
}
myFun("one", "two", "three", "four", "five", "six");

//Destructuring assignment - The destructuring assignment syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.
const user = {
	id: 42,
	displayName: "jdoe",
	fullName: {
		firstName: "John",
		lastName: "Doe",
	},
};

const { id, displayName, Name = "Zé" } = user;
console.log(id);
console.log(displayName);
console.log(Name);

// Unpacking properties from objects passed as a function parameter
function userId({ id }) {
	return id;
}

function userFullName({
	fullName: { firstName: name },
	fullName: { lastName: surname },
}) {
	return `${name} ${surname}`;
}
console.log(userFullName(user));

// this
const aluno = {
	id: 155,
	fullNome: "orlean almeida costa",
	nasc: 1971,
	nameSurname: function () {
		const arr = this.fullNome.split(" ");
		const fName = arr[0];
		const lName = arr[arr.length - 1];
		return fName + " " + lName;
	},
	idade: function () {
		return new Date().getFullYear() - this.nasc;
	},
};
console.log(aluno.nameSurname());
console.log(aluno.idade());

//call
const pessoa = {
	nome: "Leo",
};
const animal = {
	nome: "Ted",
};
function getSomething() {
	console.log(this.nome);
}
getSomething.call(animal);

//call com parâmetros
const myObj = {
	n1: 2,
	n2: 4,
};
function soma3(a, b) {
	console.log(this.n1 + this.n2 + a + b);
}
soma3.call(myObj, 1, 5);

//apply
getSomething.apply(pessoa);
soma3.apply(myObj, [1, 5]);

//bind
const rNome = function () {
	return this.nome;
};
let leo = rNome.bind({ nome: "Leo" });

console.log(leo());

//arrow
