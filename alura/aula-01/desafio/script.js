var num = 1;
var notas = [];

function validaNota() {
	while (true) {
		let input = prompt(`Digite a ${num}ª nota [ Ex: 6,7 ]. `);
		if (input && isNaN(parseFloat(input))) {
			alert("Digite uma nota válida");
		} else if (input) {
			return parseFloat(input.replace(",", "."));
		} else {
			alert("Nenhum valor digitado!");
			return 0;
		}
	}
}

function addNota() {
	notas.push(validaNota());
	num++;
}

var nome = prompt("Qual o seu nome? ");
while (nome.length < 3) {
	nome = prompt("Digite um nome com 3 caracteres no mínimo! ");
}

for (let i = 0; i < 2; i++) {
	addNota();
}

while (true) {
	let continuar = prompt(
		"Deseja digitar outra nota? [ S = sim, N = não ]"
	).toLowerCase();
	if (continuar.includes("s")) {
		addNota();
	} else {
		break;
	}
}

var total = 0;
notas.forEach((i) => {
	total += i;
});

var numNotas = notas.length;
var maxNota = Math.max(...notas);
var minNota = Math.min(...notas);
var mediaNota = (total / numNotas).toFixed(1);
var resultado = function () {
	if (mediaNota >= 8) {
		return "aprovado";
	} else if (mediaNota >= 6) {
		return "recuperação";
	} else {
		return "reprovado";
	}
};

alert(`Bem vindo(a) ${nome.toUpperCase()} ao seu sistema de média!
Você digitou ${numNotas} notas.
A maior nota foi: ${maxNota}
A menor nota foi: ${minNota}
A média final foi: ${mediaNota}
Nesta unidade você está: ${resultado().toUpperCase()}`);
