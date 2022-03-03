var precoAlcool = 1.2;
var precoGasolina = 2.3;
var rendimentoAlcool = 10.0;
var rendimentoGasolina = 15.0;

const precoPorKmAlcool = precoAlcool / rendimentoAlcool;
const precoPorKmGasolina = precoGasolina / rendimentoGasolina;

const maisEconomico = precoPorKmGasolina <= precoPorKmAlcool ? "G" : "A";
console.log(maisEconomico);
