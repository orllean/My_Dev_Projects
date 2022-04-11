let currencyValue = 1.0;
let currencyFrom = "Estados Unidos, Dolar (USD)";
let currencyTo = "Brasil, Real (BRL)";
let currencyConverted = 0;
const inputCurrencyValue = document.querySelector("#currency-value");
const inputCurrencyFrom = document.querySelector("#currency-from");
const inputCurrencyTo = document.querySelector("#currency-to");
const convertion = document.querySelector("h2");
const lastUpdate = document.querySelector("p");

inputCurrencyValue.addEventListener("change", () => {
	currencyValue = Number(inputCurrencyValue.value);
	main();
});

inputCurrencyFrom.addEventListener("change", () => {
	currencyFrom = inputCurrencyFrom.value;
	main();
});

inputCurrencyTo.addEventListener("change", () => {
	currencyTo = inputCurrencyTo.value;
	main();
});

function convertFromBTC() {
	switch (true) {
		case currencyTo.includes("USD"):
			currencyConverted = currencyValue * 42694.1;
			break;
		case currencyTo.includes("BRL"):
			currencyConverted = currencyValue * 200645.19;
			break;
		case currencyTo.includes("EUR"):
			currencyConverted = currencyValue * 39255.94;
			break;
		case currencyTo.includes("BTC"):
			currencyConverted = currencyValue;
			break;
		default:
			break;
	}
}

function convertFromEUR() {
	switch (true) {
		case currencyTo.includes("USD"):
			currencyConverted = currencyValue * 1.09;
			break;
		case currencyTo.includes("BRL"):
			currencyConverted = currencyValue * 5.11;
			break;
		case currencyTo.includes("EUR"):
			currencyConverted = currencyValue;
			break;
		case currencyTo.includes("BTC"):
			currencyConverted = currencyValue * 0.000025;
			break;
		default:
			break;
	}
}

function convertFromBRL() {
	switch (true) {
		case currencyTo.includes("USD"):
			currencyConverted = currencyValue * 0.21;
			break;
		case currencyTo.includes("BRL"):
			currencyConverted = currencyValue;
			break;
		case currencyTo.includes("EUR"):
			currencyConverted = currencyValue * 0.2;
			break;
		case currencyTo.includes("BTC"):
			currencyConverted = currencyValue * 0.000005;
			break;
		default:
			break;
	}
}

function convertFromUSD() {
	switch (true) {
		case currencyTo.includes("USD"):
			currencyConverted = currencyValue;
			break;
		case currencyTo.includes("BRL"):
			currencyConverted = currencyValue * 4.74;
			break;
		case currencyTo.includes("EUR"):
			currencyConverted = currencyValue * 0.92;
			break;
		case currencyTo.includes("BTC"):
			currencyConverted = currencyValue * 0.000023;
			break;
		default:
			break;
	}
}

function currencyConvert() {
	switch (true) {
		case currencyFrom.includes("USD"):
			convertFromUSD();
			break;
		case currencyFrom.includes("BRL"):
			convertFromBRL();
			break;
		case currencyFrom.includes("EUR"):
			convertFromEUR();
			break;
		case currencyFrom.includes("BTC"):
			convertFromBTC();
			break;
		default:
			break;
	}
}

function currencyOutCome() {
	switch (true) {
		case currencyTo.includes("USD"):
			convertion.textContent =
				currencyConverted.toLocaleString("en-US", {
					style: "currency",
					currency: "USD",
				}) + " USD";
			break;
		case currencyTo.includes("BRL"):
			convertion.textContent =
				currencyConverted.toLocaleString("pt-BR", {
					style: "currency",
					currency: "BRL",
				}) + " BRL";
			break;
		case currencyTo.includes("EUR"):
			convertion.textContent =
				currencyConverted.toLocaleString("de-DE", {
					style: "currency",
					currency: "EUR",
				}) + " EUR";
			break;
		case currencyTo.includes("BTC"):
			convertion.textContent = `${currencyConverted.toLocaleString("USD")} BTC`;
			break;
		default:
			break;
	}
}

function main() {
	currencyConvert();
	currencyOutCome();
}
