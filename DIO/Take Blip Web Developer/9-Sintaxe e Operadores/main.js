function comparaNums(num1, num2) {
	let saoIguaias = "";
	let soma = num1 + num2;
	let compara10 = soma < 10 ? "menor" : "maior";
	let compara20 = soma < 20 ? "menor" : "maior";
	if (num1 !== num2) {
		saoIguaias = " não";
	}
	return `Os números ${num1} e ${num2}${saoIguaias} são iguais. A soma entre eles é: ${soma}, que é ${compara10} que 10 e ${compara20} que 20.`;
}

console.log(comparaNums(11, 8));
