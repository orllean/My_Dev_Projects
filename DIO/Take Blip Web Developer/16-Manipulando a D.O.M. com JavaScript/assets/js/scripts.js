function changetMode() {
	changeClasse();
	changeTexto();
}

function changeTexto() {
	if (body.classList.contains("dark-mode")) {
		h1.innerText = "Dark Mode ON";
		btMode.innerText = "Light Mode";
	} else {
		h1.innerText = "Light Mode ON";
		btMode.innerText = "Dark Mode";
	}
}

function changeClasse() {
	body.classList.toggle("dark-mode");
	btMode.classList.toggle("dark-mode");
	footer.classList.toggle("dark-mode");
}

const body = document.getElementsByTagName("body")[0];
const h1 = document.getElementById("page-title");
const footer = document.getElementsByTagName("footer")[0];
const btMode = document.getElementById("mode-selector");

btMode.addEventListener("click", changetMode);
