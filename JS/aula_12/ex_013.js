var agora = new Date()
var nDiaSem = agora.getDay()
var dia

console.log(`o número do dia da semana é: ${nDiaSem}`)
switch (nDiaSem) {
    case 0:
        dia = 'domingo'
        break;
    case 1:
        dia = 'segunda'
        break;
    case 2:
        dia = 'terça'
        break;
    case 3:
        dia = 'quarta'
        break;
    case 4:
        dia = 'quinta'
        break;
    case 5:
        dia = 'sexta'
        break;
    default:
        dia = 'sábado'
        break;
}
console.log(`e hoje é ${dia}`)