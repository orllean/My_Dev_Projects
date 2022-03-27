const titulo = document.querySelector("h1");
titulo.textContent = "Aula - 09 manipulando DOM";
/* MANIPULAR CSS */
const subTitulo1 = document.querySelector("h2");
subTitulo1.style.backgroundColor = "#ffc107";
subTitulo1.style.padding = ".3rem";

const img = document.querySelector("#foto");
img.setAttribute("src", "img/pride-fc.jpg");
img.setAttribute("width", "510vw");

const subTitulo2 = document.querySelector(".box:nth-child(2) h2");
subTitulo2.textContent = "Título - h2 manipulando DOM ";

let box = document.querySelectorAll(".box");
box[0].setAttribute("class", "azul");
box[1].setAttribute("class", "escura");

box[0].removeAttribute("class");

/////// MODOS DE COR ///////
const main = document.querySelector("main");
const darkMode = document.querySelector("#btDark");
const lightMode = document.querySelector("#btLight");

darkMode.addEventListener("click", modoDark);
lightMode.addEventListener("click", modoLight);

function modoDark() {
	// event.preventDefault()
	console.log("dark on");
	main.classList.add("dark");
	main.classList.remove("light");
}
function modoLight() {
	console.log("light on");
	main.classList.add("light");
	main.classList.remove("dark");
}
/* arr function */
const arrF = () => {
	document.write(`
	<h2 class="box azul"> Olá mundo cruel! </h2>
	`);
};
arrF();
