let tentativa = 0;
const content = document.querySelector("#content");
const placar = document.querySelector("#placar");
const input = document.querySelector("#inputNum");
const btnChutar = document.querySelector("#btnChutar");
const btnSom = document.querySelector("#btnSom");
const aviso = document.querySelector("#aviso");
const avisoContent = document.querySelector("#avisoContent");
const sound = document.querySelector("#sound");

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

function alerta(e, txt) {
	content.style.visibility = "hidden";
	aviso.innerHTML = txt;
	avisoContent.classList.add(e);
	avisoContent.style.visibility = "visible";
	setTimeout(() => {
		avisoContent.style.visibility = "hidden";
		avisoContent.classList.remove(e);
		aviso.innerHTML = "";
		content.style.visibility = "visible";
		input.value = "";
		input.focus();
	}, 2500);
}

function playSound() {
	sound.volume = 0.3;
	sound.currentTime = 0;
	sound.play();
}

function gameOver(winner) {
	switch (winner) {
		case true:
			alerta("acertou", "Você ACERTOU o número secreto, Parabéns!");
			break;
		default:
			alerta("errou", `Fim de Jogo!<br>O número secreto era: ${numSecreto}.`);
			break;
	}
	setTimeout(() => {
		location.reload();
	}, 2500);
}

function scoreBoard(gameOver) {
	if (tentativa === 1 && gameOver) {
		placar.textContent = `Tentativa: ${tentativa} de 3 ❤ ❤ ❤`;
	} else if ((tentativa === 1 && !gameOver) || (tentativa === 2 && gameOver)) {
		placar.textContent = `Tentativa: ${tentativa} de 3 💔 ❤ ❤`;
	} else if ((tentativa === 2 && !gameOver) || (tentativa === 3 && gameOver)) {
		placar.textContent = `Tentativa: ${tentativa} de 3 💔 💔 ❤`;
	} else if (tentativa === 3 && !gameOver) {
		placar.textContent = `Tentativa: ${tentativa} de 3 💔 💔 💔`;
	}
}

function round(x, y) {
	if (x === y) {
		scoreBoard(true);
		gameOver(true);
	} else if (tentativa < 3) {
		if (x < y) {
			scoreBoard();
			alerta("maior", "Seu chute foi MAIOR que o número secreto");
		} else if (x > y) {
			scoreBoard();
			alerta("menor", "Seu chute foi MENOR que o número secreto");
		}
	} else {
		scoreBoard();
		gameOver(false);
	}
}

btnChutar.addEventListener("click", () => {
	if (!validaChute(chute)) {
		alerta(
			"errou",
			`Você não está sendo um(a) mentalista!<br>Digite um número inteiro entre 1 e 10.`
		);
	} else {
		tentativa++;
		playSound();
		round(numSecreto, chute);
	}
});

btnSom.addEventListener("click", () => {
	if (sound.muted) {
		sound.muted = false;
		btnSom.textContent = "🔈";
	} else {
		sound.muted = true;
		btnSom.textContent = "🔇";
	}
	input.focus();
});
