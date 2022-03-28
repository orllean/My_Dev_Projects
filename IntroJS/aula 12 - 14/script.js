/* variables */
/* input */
const inputObj = document.querySelectorAll(".data");
let input = [];
/* buttons */
const sendObj = document.querySelector("#send");
const cleanObj = document.querySelector("#clean");
/* output */
const imcObj = document.querySelector("#resultImc");
const warnerObj = document.querySelector("#warner");
const outputObj = document.querySelectorAll(".person");

/* validated */
function validated() {
	for (const data of inputObj) {
		if (data.value === "") {
			alert(`* O campo ${data.getAttribute("name").toUpperCase()} é requerido`);
			return false;
		}
	}
	return true;
}
/* get input */
function getImc(w, h) {
	return (w / (h * h)).toFixed(1);
}
function getInput() {
	input = [];
	for (const data of inputObj) {
		input.push(data.value);
	}
	input.push(getImc(inputObj[2].value, inputObj[3].value));
}
/* display imc */
function warner(imc) {
	let text = "";
	switch (true) {
		case imc < 18.5:
			text = "Baixo peso";
			break;
		case imc >= 18.5 && imc <= 24.9:
			text = "Peso normal";
			break;
		case imc >= 25 && imc <= 29.9:
			text = "Sobrepeso";
			break;
		case imc >= 30 && imc <= 34.9:
			text = "Obesidade I";
			break;
		case imc >= 35 && imc <= 39.9:
			text = "Obesidade II";
			break;
		default:
			text = "Obesidade III";
			break;
	}
	if (imc >= 30) {
		warnerObj.classList.add("alert");
	} else {
		warnerObj.classList.remove("alert");
	}
	return text;
}
function displayImc() {
	imcObj.value = input[4];
	warnerObj.textContent = warner(imcObj.value);
}
/* display result */
function displayResult() {
	const person = {
		name: input[0],
		age: input[1],
		weigth: input[2],
		height: input[3],
		imc: input[4],
		sit: warnerObj.textContent,
	};
	outputObj[0].textContent = person.name.toUpperCase();
	outputObj[1].textContent = person.age + " anos";
	outputObj[2].textContent = person.weigth + " Kg";
	outputObj[3].textContent = person.height + " m";
	outputObj[4].textContent = person.imc + " - " + person.sit;
}

/* main */
sendObj.addEventListener("click", function (event) {
	event.preventDefault();
	if (validated()) {
		getInput();
		displayImc();
		displayResult();
	}
});
/* clean output */
cleanObj.addEventListener("click", () => {
	for (const data of outputObj) {
		data.textContent = "";
	}
	outputObj[0].textContent = "Resumo:";
	warnerObj.classList.remove("alert");
	warnerObj.textContent = "";
});
