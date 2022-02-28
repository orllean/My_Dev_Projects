//Estruturas de decisão
var notaAluno1 = 6;
var notaAluno2 = 5;
var notaAluno3 = 4;
//if statement
if (typeof notaAluno1 == "number") {
	if (notaAluno1 < 5) {
		console.log("Reprovado");
	} else if (notaAluno1 < 7) {
		console.log("Recuperação");
	} else {
		console.log("Aprovado");
	}
} else {
	console.log("Erro: Digite uma nota válida");
}

if (notaAluno1 > notaAluno2 && notaAluno1 > notaAluno3) {
	console.log(`O aluno 1 tem a maior nota: ${notaAluno1}`);
} else if (notaAluno2 > notaAluno1 && notaAluno2 > notaAluno3) {
	console.log(`O aluno 2 tem a maior nota: ${notaAluno2}`);
} else {
	console.log(`O aluno 3 tem a maior nota: ${notaAluno3}`);
}
//forma curta de if statement
notaAluno3 < 5
	? console.log("Reprovado - if ternário")
	: console.log("Aprovado - if ternário");

//switch-case statement
switch (true) {
	case notaAluno1 > notaAluno2 && notaAluno1 > notaAluno3:
		console.log(`A maior nota foi do aluno 1: ${notaAluno1}`);
		break;
	case notaAluno2 > notaAluno1 && notaAluno2 > notaAluno3:
		console.log(`A maior nota foi do aluno 2: ${notaAluno2}`);
		break;
	default:
		console.log(`A maior nota foi do aluno 3: ${notaAluno3}`);
		break;
}
//Estruturas de repetição
const arr = ["bola", "mala", "dado", "cama", "mesa"];
const obj = {
	nome: "leo",
	sexo: "m",
	idade: 50,
};
//for
for (let i = 0; i < arr.length; i++) {
	console.log(arr[i]);
}
for (let i in arr) {
	console.log(i);
	console.log(arr[i]);
}
for (let i in obj) {
	console.log(i);
	console.log(obj[i]);
}
for (let i of arr) {
	console.log(i);
}
//for of tem uso restrito com objetos assim como for in para arrays
//while
var i = 0;
while (i < 10) {
	i++;
	console.log(`${i} - while`);
}
//do while
i = 0;
do {
	i++;
	console.log(`${i} - do-while`);
} while (i < 10);
