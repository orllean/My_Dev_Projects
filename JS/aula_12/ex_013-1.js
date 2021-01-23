var sexo
var idade
var categoria

sexo = 'm'
idade = 5


switch (true) {
    case (sexo == 'm' && idade <= 5) :
        categoria = 'fraldinha masc'
        break;
    case (sexo == 'f' && idade <= 5):
        categoria = 'fraldinha fem'
        break;
    default:
        categoria = 'asoluto'
        break;
}
console.log(`atleta ${categoria}`)