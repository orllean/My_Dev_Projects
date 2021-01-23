let num_1 = [5, 2, 8]
num_1[3] = 9

let num = [] //declara um array vazio
num.push(145) //insere um valor na ult pos. do array
num.push(140)
num.push(150)
num.push(160)
num.push(155)

console.log(num_1)
num_1.sort() // ordenar o vetor crescente
console.log(num_1)

for( let c in num ){
    console.log(`num [${c}]: ${num[c]}`)
}
// loop pelo vetor método OBJETO

console.log(`o vetor [num_1] tem ${num.length} elementos`) // propriedade length retorna  o comprimento do vetor
console.log(`o primeiro elemento do vetro é: [${num[0]}]`)
console.log(`o vetro ordenado é ${num.sort()}`)

for(let c = 0; c < num_1.length; c++){
    console.log(`num_1 [${c}]: ${num_1[c]}`)
}
// loop pelo vetor método FRO

let pos = num_1.indexOf(8)
console.log(`a posição de 8 no vetor [num_1] é: [${pos}]`)


let x = 155
if (num.indexOf(x) == -1) {
    console.log(`valor não encontrado: ${x}`)
} else {
    console.log(`a posição de ${x} no vetor é: [${num.indexOf(x)}]`)
}

var arr = [1, 2, 3, 4, 5, 6];
var novoArr = arr.slice(2, 5); /* não remove elementos do array original e sim retorna um novo array com os elementos especificados pelos parametros start e end, mais não exibe a ultima */
console.log('Array original: ' + arr);
console.log('Novo array: ' + novoArr);

let list_1 = ["bar", "baz", "foo", "qux"];
list_1.splice(list_1.indexOf('foo'), 1);
console.log( list_1 );
// Encontre a posição do índice de "foo", então remova um elemento dessa posição

let list_2 = ["bar", "baz", "foo", "qux"];
list_2.splice(1, 1);
console.log( list_2 );

let list = ["bar", "baz", "foo", "qux"];
list[ list.indexOf('foo') ] = "leo";
console.log( list );