import { financing } from "./financing.js";

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

btnCalcular.addEventListener("click", function () {
	const valor = parseFloat(txtValor.value);
	const entrada = parseFloat(txtEntrada.value);
	const taxaJuros = parseFloat(txtTaxaJuros.value);
	const prazo = parseFloat(txtPrazo.value);

	let simulacao = new financing(valor, entrada, taxaJuros, prazo);
	simulacao.calcParcelasMensais();
	simulacao.exibeParcelas();
});
