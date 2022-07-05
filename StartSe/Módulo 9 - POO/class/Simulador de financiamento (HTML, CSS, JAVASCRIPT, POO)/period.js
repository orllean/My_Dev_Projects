import { financing } from "./financing.js";
import { installments } from "./installments.js";

export class financingPeriod extends financing {
	#carencia;
	#taxaJuros;
	#parcelas = [];
	constructor(valor, entrada, taxaJuros, prazo, carencia) {
		super(valor, entrada, taxaJuros, prazo);
		this.#taxaJuros = taxaJuros;
		this.#taxaJuros = taxaJuros;
		this.#parcelas = super.getParcelas();
		this.#carencia = carencia;
	}

	calcParcelasMensais() {
		let saldo = this.#parcelas[0].getSaldo();
		for (let i = 0; i < this.#carencia; i++) {
			const numero = this.#parcelas.length;
			saldo += financing.calcJuros(saldo, this.#taxaJuros);
			this.#parcelas.push(new installments(numero, 0, 0, 0, saldo));
		}
		super.calcParcelasMensais();
	}
}
