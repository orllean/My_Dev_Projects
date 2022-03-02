function hello() {
	console.log("Hello cruel world!");
}
hello();

function welcome(name, surname) {
	let fullname = name.toUpperCase() + " " + surname.toUpperCase();
	console.log(`Welcome ${fullname}!`);
}
welcome("Orlean", "Costa");
