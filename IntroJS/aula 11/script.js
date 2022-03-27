function carregou() {
	console.log("onLoad body");
}
function rolou() {
	console.log("onScroll body");
}
function sobreH1() {
	console.log("onMouseOver h1");
}
function ganhaFocoInput() {
	console.log("onFocus input");
}
function perdeFocoInput() {
	console.log("onFocusOut input");
}
const inputText = document.querySelector("#input");

function presTeclaInput() {
	console.log(`${inputText.value.length + 1} teclas pressionadas`);
	// console.log("onKeyPress input");
}

const bt1 = document.querySelector("#btn1");
bt1.addEventListener("mousemove", mouseOver);
bt1.addEventListener("click", mouseClickBtn1);
function mouseOver() {
	console.log("mouseOver btn1");
}
function mouseClickBtn1() {
	console.log("mouseClick btn1");
}

const bt2 = document.querySelector("#btn2");
bt2.addEventListener("blur", focusOut);
bt2.addEventListener("click", mouseClickBtn2);
function focusOut() {
	console.log("mouseOver btn2");
}
function mouseClickBtn2() {
	console.log("mouseClick btn2");
}

const input = document.querySelector("#input");
const bt3 = document.querySelector("#btn3");
bt3.addEventListener("click", function (event) {
	event.preventDefault();
	console.log("click btEnviar");
	input.value = "";
});
