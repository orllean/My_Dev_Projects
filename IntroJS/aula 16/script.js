let num = 0;
const imgDado = document.querySelector("#imgDado");
const btn = document.querySelector("#btn");
const numSorteado = document.querySelector("#sorteado");
const sound = document.querySelector("#dadoRolando");

function aleatorioEntre(min, max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

btn.addEventListener("click", () => {
	imgDado.classList.add("animar");
	numSorteado.classList.add("aparecer");
	sound.play();
	btn.style.visibility = "hidden";

	setTimeout(() => {
		num = aleatorioEntre(1, 6);
		imgDado.setAttribute("src", "images/dado/" + num + ".png");
		numSorteado.textContent = num;
		btn.style.visibility = "visible";
		imgDado.classList.remove("animar");
		numSorteado.classList.remove("aparecer");
	}, 1530);
});
