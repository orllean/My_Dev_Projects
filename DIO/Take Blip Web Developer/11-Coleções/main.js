//Atividade 1: Maps
console.log("Atividade 1: Maps");
function getAdmin(map) {
	let admins = [];
	for ([key, value] of map) {
		if (value === "admin") {
			admins.push(key);
		}
	}
	return admins;
}

const user = new Map([
	["Edelclides", "admin"],
	["Orlean", "user"],
	["Almeri ", "admin"],
]);
console.log(getAdmin(user));
console.log("------------------------------------");

//Atividade 2: Sets
console.log("Atividade 2: Sets");
function unicos(arr) {
	const setUnicos = new Set(arr);
	return [...setUnicos];
}

const arr = [30, 30, 40, 5, 223, 2049, 3034, 5];
console.log(unicos(arr));

console.log("------------------------------------");
