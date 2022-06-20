const txtInput = document.querySelector("#txtInput");
const btnAdd = document.querySelector("#btnAdd");
const listToDo = document.querySelector("#listToDo");

btnAdd.addEventListener("click", function () {
	const txt = txtInput.value;
	txtInput.value = "";
	listToDo.appendChild(addToDo(txt));
	txtInput.focus();
});

function addToDo(txt) {
	const elementLi = document.createElement("li");
	elementLi.textContent = txt;
	elementLi.appendChild(addBtnErase());
	return elementLi;
}

function addBtnErase() {
	const btnErase = document.createElement("button");
	btnErase.setAttribute("class", "btn-erase");
	btnErase.textContent = "✘";
	btnErase.addEventListener("click", function () {
		listToDo.removeChild(this.parentNode);
		txtInput.focus();
	});
	return btnErase;
}
