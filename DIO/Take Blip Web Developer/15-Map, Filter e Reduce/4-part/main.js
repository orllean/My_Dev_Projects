const arr = [1, 2, 3, 4, 5];

function somaNumeros(arr) {
	return arr.reduce((prev, curert) => prev + curert);
}

console.log(somaNumeros(arr));

const saldo = 100;
const precos = [2, 34, 53, 23, 64, 12];

function saldoAtual(arr) {
	return arr.reduce((prev, current) => prev - current, saldo);
}

console.log(saldo);
console.log(precos.reduce((p, c) => p + c));
console.log(saldoAtual(precos));

const prod = [
	{
		nome: "sabão em pó",
		preco: 25,
	},
	{
		nome: "cereal",
		preco: 15,
	},
	{
		nome: "manteiga",
		preco: 30,
	},
];

function calculaSaldo(saldoDisponivel, lista) {
	return lista.reduce((prev, current, index) => {
		console.log("rodada", index + 1);
		console.log("valor anterior", prev.preco);
		console.log("valor atual", current.preco);
		console.log("anterior - atual = ", prev.preco - current.preco);
		return prev - current.preco;
	}, saldoDisponivel);
}
console.log(calculaSaldo(saldo, prod));
