let inputs = document.querySelectorAll("input");
let aviso = document.querySelector("#aviso");
const buts = document.querySelectorAll("button");
const form = document.querySelector("form");

buts[0].addEventListener("click", function (e) {
	e.preventDefault();
	let nota1 = inputs[0].value;
	let nota2 = inputs[1].value;
	if (validaNota(nota1, nota2)) {
		main(nota1, nota2);
	}
});

buts[1].addEventListener("click", () => {
	inputs[3].classList.remove("aprovado");
	inputs[3].classList.remove("reprovado");
	inputs[3].classList.remove("recuperacao");
	inputs[0].focus();
});

// VALIDAR E GERAR FLASH MESSAGE
function alerta(text) {
	// form.reset() // limpa form
	aviso.textContent = text;
	aviso.classList.add("alerta");
	setTimeout(() => {
		aviso.textContent = "";
		aviso.classList.remove("alerta");
	}, 1500);
}

function validaInput(num) {
	let nota = num.value;
	if (nota < 0 || nota > 10 || nota === "") {
		alerta("Digite um valor entre 0.0 e 10.0");
		num.value = "";
	}
}

function validaNota(n1, n2) {
	if (n1 === "" || n2 === "") {
		alerta("Todas as notas são requeritas!");
		inputs[0].focus();
		return false;
	}
	return true;
}

function situacao(media) {
	switch (true) {
		case media < 5:
			inputs[3].value = "Reprovado(a)";
			inputs[3].classList.remove("aprovado");
			inputs[3].classList.remove("recuperacao");
			inputs[3].classList.add("reprovado");
			break;
		case media < 7:
			inputs[3].value = "Recuperação";
			inputs[3].classList.remove("aprovado");
			inputs[3].classList.remove("reprovado");
			inputs[3].classList.add("recuperacao");
			break;
		default:
			inputs[3].value = "Aprovado(a)";
			inputs[3].classList.remove("recuperacao");
			inputs[3].classList.remove("reprovado");
			inputs[3].classList.add("aprovado");
			break;
	}
}

function main(n1, n2) {
	let media = ((Number(n1) + Number(n2)) / 2).toFixed(1);
	inputs[2].value = media;
	situacao(media);
}
