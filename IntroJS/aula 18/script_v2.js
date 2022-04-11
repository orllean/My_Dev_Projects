let currencyValue = 1.0;
let currencyFrom = "Estados Unidos, Dolar (USD)";
let currencyTo = "Brasil, Real (BRL)";
let currencyConverted = 0;
const inputCurrencyValue = document.querySelector("#currency-value");
const inputCurrencyFrom = document.querySelector("#currency-from");
const inputCurrencyTo = document.querySelector("#currency-to");
const convertion = document.querySelector("h2");
const currencys = {
	USD: {
		USD: 1,
		BRL: 4.74,
		EUR: 0.92,
		BTC: 0.000023,
		LOC: "Estados Unidos, Dolar (USD)",
		OUT: function () {
			return currencyConverted.toLocaleString("en-US", {
				style: "currency",
				currency: "USD",
			});
		},
	},

	BRL: {
		USD: 0.21,
		BRL: 1,
		EUR: 0.2,
		BTC: 0.000005,
		LOC: "Brasil, Real (BRL)",
		OUT: function () {
			return currencyConverted.toLocaleString("pt-BR", {
				style: "currency",
				currency: "BRL",
			});
		},
	},

	EUR: {
		USD: 1.09,
		BRL: 5.11,
		EUR: 1,
		BTC: 0.000025,
		LOC: "Euro, Euro (EUR)",
		OUT: function () {
			return currencyConverted.toLocaleString("de-DE", {
				style: "currency",
				currency: "EUR",
			});
		},
	},

	BTC: {
		USD: 42694.1,
		BRL: 200645.19,
		EUR: 39255.94,
		BTC: 1,
		LOC: "Bitcoin (BTC)",
		OUT: function () {
			return currencyConverted.toLocaleString("USD");
		},
	},
};

window.addEventListener("load", () => {
	currencyOpionsFrom();
	currencyOpionsTo();
	main();
});

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

function currencyOpionsFrom() {
	Object.values(currencys).forEach((value) => {
		let option = new Option(value["LOC"], value["LOC"]);
		inputCurrencyFrom.appendChild(option);
	});
}
function currencyOpionsTo() {
	Object.values(currencys).forEach((value) => {
		let option = new Option(value["LOC"], value["LOC"]);
		inputCurrencyTo.appendChild(option);
	});
	inputCurrencyTo.value = "Brasil, Real (BRL)";
}

function currencyConvert() {
	Object.entries(currencys).forEach(([key, value]) => {
		if (currencyFrom.includes(key)) {
			Object.entries(value).forEach(([key, value]) => {
				if (currencyTo.includes(key)) {
					return (currencyConverted = currencyValue * value);
				}
			});
		}
	});
}

function currencyOutCome() {
	Object.entries(currencys).forEach(([key, value]) => {
		if (currencyTo.includes(key)) {
			convertion.textContent = `${value["OUT"]()} ${key}`;
		}
	});
}

function main() {
	currencyConvert();
	currencyOutCome();
}
