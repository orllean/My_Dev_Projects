const btAdd = document.querySelector("#task-form button");
const tasks = document.getElementById("tasks");
const taskInput = document.getElementById("task-input");

btAdd.addEventListener("click", function (evt) {
	evt.preventDefault();
	addToDo();
});

function addToDo() {
	const div = document.createElement("div");
	if (taskInput.value !== "") {
		div.innerHTML = `<input type="checkbox" name="task" id="task"> <label for=${taskInput.value}>${taskInput.value}</label>`;
		tasks.append(div);
		taskInput.value = "";
	} else {
		window.alert("Digite uma tarafa antes de clicar em adicionar.");
	}
}
