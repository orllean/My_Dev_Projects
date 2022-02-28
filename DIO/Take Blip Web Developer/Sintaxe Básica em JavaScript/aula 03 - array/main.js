// Array
// declarando
let array = ["string", 33, true, ["a", "b", "c"], [11, 12], [true, false]];
console.log(array);
// acessando um item pelo índice
console.log(array[4]);
// manipulando
array.forEach(function (item, index) {
	console.log(item, index);
});
//forEach - varre cada elemento do array e seus respectivos índices
array.push("new item");
console.log(array);
//push - add elemento no final do array
array.pop();
console.log(array);
//pop - remove elemento no final do array
array.shift();
console.log(array);
//shift - remove elemento no início do array
array.unshift("STRING");
console.log(array);
//unshift -  add elemento no início do array
console.log(array.indexOf(33));
//indexOf - retorna o índice de um elemento
let novoArray = array.slice(3);
console.log(novoArray);
//slice cira um novo array a partir de outro existente. Definir início e fim
array.splice(3);
console.log(array);
//splice remove elementos pelo índice. Definir início e fim
//Object
let aluno = {
	nome: "Orlean Costa",
	idade: 50,
	ativo: true,
	tecnologias: ["html", "css", "javascript"],
	dependentes: [
		{ nome: "Brisa", idade: 14 },
		{ nome: "Arthur", idade: 12 },
	],
};
console.log(aluno);
console.log(aluno.dependentes[0].nome);
let dependentes = [aluno.dependentes]
console.log(dependentes);