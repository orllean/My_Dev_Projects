const notas = document.querySelectorAll(".nota");
const btCalcular = document.querySelector("#calcular");
const tagResultado = document.querySelector("#resultado");

btCalcular.addEventListener("click", main);

function empty() {
	let isEmpt = false;
	notas.forEach((nota) => {
		if (nota.value === "") {
			isEmpt = true;
		}
	});
	return isEmpt;
}

function getNotas() {
	let arr = [];
	notas.forEach((nota) => {
		arr.push(Number(nota.value));
	});
	return arr;
}

function media(arr) {
	let sum = arr.reduce((prev, curr) => prev + curr, 0);
	return (sum / arr.length).toFixed(1);
}

function resultado(media) {
	let label = `Com a média de ${media} você está`;
	switch (true) {
		case media < 5:
			tagResultado.textContent = `${label} REPROVADO!`;
			break;
		case media < 7:
			tagResultado.textContent = `${label} EM RECUPERAÇÃO!`;
			break;

		default:
			tagResultado.textContent = `${label} APROVADO!`;
			break;
	}
}

function limpaNotas() {
	notas.forEach((nota) => {
		nota.value = "";
	});
}

function main() {
	if (empty()) {
		alert("*Todas as notas são requeridas.");
	} else {
		resultado(media(getNotas()));
		limpaNotas();
	}
}
