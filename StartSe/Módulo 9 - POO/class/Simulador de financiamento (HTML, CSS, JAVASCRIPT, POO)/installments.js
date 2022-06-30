export class installments {
	#numero;
	#valor;
	#juros;
	#amortizacao;
	#saldo;
	constructor(numero, valor, juros, amortizacao, saldo) {
		this.#numero = numero;
		this.#valor = valor;
		this.#juros = juros;
		this.#amortizacao = amortizacao;
		this.#saldo = saldo;
	}

	getSaldo() {
		return this.#saldo;
	}
}
