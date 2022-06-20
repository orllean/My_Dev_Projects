const txtInput = document.querySelector("#txtInput");
const btnAdd = document.querySelector("#btnAdd");
const listToDo = document.querySelector("#listToDo");
const selectOption = document.querySelector("#selectOption");

function checkImput(txt) {
	if (txt.length < 3) {
		alert("Digite ao menos 3 caracteres!");
		txtInput.focus();
	} else {
		return txt.length;
	}
}

btnAdd.addEventListener("click", function () {
	const txt = txtInput.value;
	if (checkImput(txt)) {
		txtInput.value = "";
		listToDo.appendChild(addToDo(txt));
		txtInput.focus();
		showHidenAtions();
	}
});

function addToDo(txt) {
	const elementLi = document.createElement("li");
	elementLi.textContent = txt;
	elementLi.appendChild(addBtnErase());
	elementLi.classList.add("to-do-item");
	elementLi.addEventListener("click", function () {
		this.classList.toggle("do");
	});
	return elementLi;
}

function addBtnErase() {
	const btnErase = document.createElement("button");
	btnErase.setAttribute("class", "btn-erase");
	btnErase.textContent = "✘";
	btnErase.addEventListener("click", function () {
		listToDo.removeChild(this.parentNode);
		txtInput.focus();
		showHidenAtions();
	});
	return btnErase;
}

function showHidenAtions() {
	if (listToDo.hasChildNodes()) {
		selectOption.removeAttribute("hidden");
	} else {
		selectOption.setAttribute("hidden", "hidden");
	}
}

selectOption.addEventListener("change", function () {
	const items = document.querySelectorAll(".to-do-item");
	switch (selectOption.selectedIndex) {
		case 1:
			for (const item of items) {
				if (!item.classList.contains("do")) {
					item.classList.add("do");
				}
			}
			break;
		case 2:
			for (const item of items) {
				if (item.classList.contains("do")) {
					item.classList.remove("do");
				}
			}
			break;
		case 3:
			const btns = document.querySelectorAll(".btn-erase");
			for (const btn of btns) {
				btn.dispatchEvent(new Event("click"));
			}
			break;

		default:
			break;
	}
	selectOption.value = "";
});
