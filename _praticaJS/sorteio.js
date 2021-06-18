let sorteio = 0
let jogador = 3
let max = 5
sorteio = 1 + Math.trunc(max * Math.random(max))/*soma-se 1 a parte inteira do valor do produto do máximo e a parte aleatória de máximo que varia entre 0 e 100%*/

console.log(sorteio)

if (jogador < sorteio) {
    console.log(`Você falou ${jogador}. Meu número é MAIOR`)
} else if (jogador > sorteio) {
    console.log(`Você falou ${jogador}. Meu número é MENOR`)
} else if (jogador == sorteio) {
    console.log(`PARABÉNS! Você acertou! Eu tinha sorteado o valor ${sorteio}!`)
}