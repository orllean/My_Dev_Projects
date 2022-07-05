import { financing } from "./financing.js";
import { financingPeriod } from "./period.js";

const txtValor = document.querySelector("#txtWell");
const txtEntrada = document.querySelector("#txtInitialValue");
const txtTaxaJuros = document.querySelector("#txtRate");
const txtPrazo = document.querySelector("#txtMonths");
const btnCalcular = document.querySelector("#btnCalc");

const listPeriod = document.querySelector("#listPeriod");
const chkPeriod = document.querySelector("#chkPeriod");
const corpoTabela = document.querySelector("#corpoTabela");

chkPeriod.addEventListener("change", function () {
	if (this.checked) {
		listPeriod.removeAttribute("hidden");
	} else {
		listPeriod.setAttribute("hidden", "hidden");
	}
});

function limpaCorpoTabela() {
	while (corpoTabela.firstChild) {
		corpoTabela.removeChild(corpoTabela.firstChild);
	}
}

btnCalcular.addEventListener("click", function () {
	limpaCorpoTabela();
	const valor = parseFloat(txtValor.value);
	const entrada = parseFloat(txtEntrada.value);
	const taxaJuros = parseFloat(txtTaxaJuros.value);
	const prazo = parseFloat(txtPrazo.value);
	let simulacao;
	if (chkPeriod.checked) {
		const carencia = parseInt(listPeriod.value);
		simulacao = new financingPeriod(valor, entrada, taxaJuros, prazo, carencia);
	} else {
		simulacao = new financing(valor, entrada, taxaJuros, prazo);
	}
	simulacao.calcParcelasMensais();
	simulacao.exibeParcelas();
});
