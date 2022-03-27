let produto = "arroz".toUpperCase();
let qtd = 3;
let precoUnitario = 4.89;

let precoTotal = qtd * precoUnitario;
// saída float com duas casas decimias
let pTotal_1 = new Intl.NumberFormat("pt-BR").format(qtd * precoUnitario);
// saída formato moeda c duas casas decimias
let pTotal_2 = (qtd * precoUnitario).toLocaleString("pt-BR", {
	style: "currency",
	currency: "BRL",
});

document.write(`<p>Preço total 1 R$ ${precoTotal.toFixed(2)} </p><hr>`);
document.write(`<p>Preço total 2 R$ ${pTotal_1} </h><hr>`);
document.write(`<p>Preço total 3 ${pTotal_2} </h><hr>`);

document.write("<h2> Informações </h2>");

let lutador = {
	nome: "Fedor Vladmirovich Emelianenko",
	nac: "Russo",
	idade: 44,
	peso: 106,
	altura: 1.83,
	imc: function () {
		return (this.peso / (this.altura * this.altura)).toFixed(2);
	},
};

console.log(Object.keys(lutador));
console.log(Object.values(lutador));
console.log(Object.entries(lutador));

for (const [key, value] of Object.entries(lutador)) {
	if (key !== "imc") {
		document.write(`${key.toUpperCase()}: ${value} <br>`);
	}
}

document.write(
	`${Object.keys(lutador)[
		Object.keys(lutador).length - 1
	].toUpperCase()}: ${lutador.imc()}`
);
