let amigo = {
    nome: 'josé',
    sexo: 'm',
    peso: 71.8,
    engordar(p = 0) {
        console.log(`Engordou!... ${p}Kg`)
        this.peso += p
    }
}
console.log(amigo)
console.log(`${amigo.nome} pesa: ${amigo.peso}`)
amigo.engordar(2)
console.log(`${amigo.nome} pesa: ${amigo.peso}`)