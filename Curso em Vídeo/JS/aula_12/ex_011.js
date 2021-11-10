var idade = 17
console.log(`Você tem ${idade} anos`)
if( idade < 16){
    console.log('não vota')
} else if(idade <= 17 || idade > 65){
    console.log('voto facultativo')
} else{
    console.log('voto obrigatório')
}