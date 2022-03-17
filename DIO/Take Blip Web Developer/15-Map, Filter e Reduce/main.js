// Map X forEach
const arr = [1, 2, 3, 4, 5];

arr.map((item) => {
	console.log(item * 2);
});

// retorma um novo array
console.log(arr.map((item) => item * 2));

arr.forEach((item) => {
	console.log(item * 3);
});

// retorma undefined
console.log(arr.forEach((item) => item * 3));

// Filter
const frutas = [
	"maçã fuji",
	"laranja",
	"maçã verde",
	"abacaxi",
	"maçã nacional",
];

// retorma um novo array
console.log(frutas.filter((fruta) => fruta.includes("maçã")));

// Reduce com valor inicial
const iniValue = 10;
const sumWithIni = arr.reduce(
	(previousValue, currentValue) => previousValue + currentValue,
	iniValue
);

console.log(sumWithIni);

// Reduce sem valor inicial
const sumWithoutIni = arr.reduce(
	(previousValue, currentValue) => previousValue + currentValue
);

console.log(sumWithoutIni);

function soma(arr) {
	return arr.reduce((prev, current) => {
		console.log({ prev });
		console.log({ current });
		return prev + current;
	}, 0);
}

console.log(soma(arr));
