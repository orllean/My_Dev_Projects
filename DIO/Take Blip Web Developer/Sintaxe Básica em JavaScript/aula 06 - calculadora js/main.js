function calc() {
	const opercao = Number(
		prompt(
			"Escolha uma operação:\n 1 - soma (+)\n 2 - subtração (-)\n 3 - multiplicação (*)\n 4 - divisão (/)\n 5 - resto da divisão (%)\n 6 - potenciação (**)"
		)
	);
	let escolha = [1, 2, 3, 4, 5, 6];
	if (escolha.indexOf(opercao) !== -1) {
		let n1 = Number(prompt("Insira o primeiro valor"));
		let n2 = Number(prompt("Insira o segundo valor"));
		let result;
		if (!n1 || !n2) {
			alert("Erro - parametros inválidos");
			calc();
		} else {
			switch (opercao) {
				case 1:
					soma();
					break;
				case 2:
					sub();
					break;
				case 3:
					mult();
					break;
				case 4:
					divisao();
					break;
				case 5:
					resto();
					break;
				case 6:
					pot();
					break;
			}
		}
		function soma() {
			result = n1 + n2;
			alert(`${n1} + ${n2} = ${result}`);
			novaOpracao();
		}
		function sub() {
			result = n1 - n2;
			alert(`${n1} - ${n2} = ${result}`);
			novaOpracao();
		}
		function mult() {
			result = n1 * n2;
			alert(`${n1} * ${n2} = ${result}`);
			novaOpracao();
		}
		function divisao() {
			result = n1 / n2;
			alert(`${n1} / ${n2} = ${result}`);
			novaOpracao();
		}
		function resto() {
			result = n1 % n2;
			alert(`O Resto da divisão de ${n1} por ${n2} é igual a ${result}`);
			novaOpracao();
		}
		function pot() {
			result = n1 ** n2;
			alert(`${n1} elevado a ${n2}ª = ${result}`);
			novaOpracao();
		}
		function novaOpracao() {
			let opc = Number(
				prompt("Deseja fazer outra operação?\n 1 - Sim\n 2 - Não")
			);
			if (opc == 1) {
				calc();
			} else if (opc == 2) {
				alert("Até mais...");
			} else {
				alert("Digite uma opção válida");
				novaOpracao();
			}
		}
	} else {
		alert("Escolha uma opção válida!");
		calc();
	}
}

calc();
