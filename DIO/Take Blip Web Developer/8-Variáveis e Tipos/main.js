// Atividade 1.0
function pal(str) {
	if (!str) return "Erro: entrada inválida!";
	str = str.toString().toUpperCase();
	for (let i = 0; i < str.length; i++) {
		if (str[i] !== str[str.length - 1 - i]) {
			return `${str} não é um palíndromo.`;
		}
	}
	return `${str} é um palíndromo.`;
}
let txt = "Amor a Roma";
//console.log(pal(txt));

// Atividade 1.1
function pal2(str) {
	if (!str) return "Erro: entrada inválida!";
	return (
		str.toString().toUpperCase().split("").reverse().join("") ===
		str.toUpperCase()
	);
}
console.log(pal2(txt));

// Atividade 2.0 - carece tratamento de erro
//var Input = [1, 3, 4, 6, 80, 33, 23, 90];
var Input = [];
//var Input = null;

function trocPares(arr) {
	var Output = [];
	if (Input.length > 0) {
		for (const i of Input) {
			if (i % 2 !== 0) {
				Output.push(i);
			} else {
				Output.push(0);
			}
		}
	} else {
		Output = -1;
	}
	console.log(Output);
}
//trocPares(Input);

// Atividade 2.1
function subPares(arr) {
	//trata se não for array ou se for um array vazio!
	if (!arr || !arr.length) {
		return -1;
	}
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] % 2 === 0) {
			arr[i] = 0;
		}
	}
	return arr;
}
//console.log(subPares(Input));
