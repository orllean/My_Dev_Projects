import { installments } from "./installments.js";

export class financing {
	#taxaJuros;
	#prazo;
	#parcelas = [];
	constructor(valor, entrada, taxaJuros, prazo) {
		this.#taxaJuros = taxaJuros;
		this.#prazo = prazo;
		this.#parcelas.push(new installments(0, 0, 0, 0, valor - entrada));
	}

    
}
