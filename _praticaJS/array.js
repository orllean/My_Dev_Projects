//creating an array
let arrLength=3; //comprimento do arraycom três elementos
let arr1=['A',true,5]; //criando um array com: string, boolean, number
let arr2=Array(arrLength); //atribuindo um comprimento ao array 'arr2'

console.log(arr1.length); //imp o comprimento do array
console.log(arr2.length); //imp o comprimento do array

console.log(arr1[0]); //imp o conteúdo do array no índice indicado
console.log(arr1[1]); //imp o conteúdo do array no índice indicado

arr2[0]='bad robot!' //atribuindo valor ao array no índice indicado
console.log(arr2[0]); //imp o comprimento do array 
console.log(arr2[1]); //imp o comprimento do array
console.log(arr2[2]); //imp o comprimento do array

arr2[2]='hello cruel world!' //atribuindo valor ao array no índice indicado
console.log(arr2[arr2.length-1]); //imp o comprimento do array
//array methods
console.log(arr1);
//console.log(arr1.push('new value')/*push add um novo elemento ao final do array */); /* retorna o novo legth */
//console.log(arr1.pop()/*pop remove um elemento ao array */); /* retorna o elemento removido */
console.log(arr1.unshift('new value')/*unshift add um novo elemento no inicio do array */); /* retorna o novo legth */
console.log(arr1);
console.log(arr1.shift()/*pop remove o primeiro elemento do array */); /* retorna o elemento removido */
console.log(arr1);

let arr3=arr1.concat(arr2);
console.log(arr3)

let arr4=arr1.concat([1,3,5])
console.log(arr4)