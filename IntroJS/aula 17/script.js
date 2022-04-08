/* &#x1F508 com som  &#x1F507 sem som */
/* &#x1F494 loose &#x2764 life*/
let tentativa = 0;
let txt = "";
const placar = document.querySelector("#placar");
const input = document.querySelector("#inputNum");
const btnChutar = document.querySelector("#btnChutar");
const btnSom = document.querySelector("#btnSom");
const avisoContent = document.querySelector("#avisoContent");
const aviso = document.querySelector("#aviso");

function random(min, max) {
	return (numSecreto = Math.floor(Math.random() * (max - min + 1)) + min);
}

function getInput(num) {
	return (chute = num);
}

function validaChute(num) {
	if (num < 1 || num > 10) {
		return false;
	}
	return true;
}

function alerta() {
	console.log("erro");
}

function playGame(x, y) {
	console.log(x, y);
}

btnChutar.addEventListener("click", () => {
	if (!validaChute(chute)) {
		alerta();
	} else {
		playGame(numSecreto, chute);
	}
});

btnSom.addEventListener("click", () => {
	console.log(2);
});
