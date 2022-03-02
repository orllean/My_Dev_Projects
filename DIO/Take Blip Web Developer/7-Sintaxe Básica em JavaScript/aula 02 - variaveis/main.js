/* Tipos primitivos */
/* boolean */
var vOuF = false;
console.log(vOuF)
console.log(typeof(vOuF))
/* number */
var num = 35;
console.log(num);
console.log(typeof(num));
/* strintg */
var nome = 'Orlean Costa'
console.log(nome);
console.log(typeof(nome));
/* function */
var f = function () {}
console.log(f);
console.log(typeof(f));
/* undefine */
var test1 
console.log(test1);
console.log(typeof(test1));
/* null */
var test2 = null;
console.log(test2);
console.log(typeof(test2));
console.log(test1 == test2);
console.log(test1 === test2);
/* escopo */
// var - global e local
// let - local
// const - local, somente leitura, valor inicial obrigatório
var varGlobal = 'global'
console.log(varGlobal);

function varLocal () {
    let local = 'local';
    console.log(local);
}
// console.log(local); esta linha retorna um erro pois "local" esta disponivel apenas dentro da função
varLocal();
/*  Atribuição: =
    Comparação: ==
    Comparação identica: === 
*/
/* Operadores aritimeticos
    +  adição
    -  subtração
    *  multiplicação
    /  divisão
    %  resto da divisão
    ** potenciação
*/
/* Operadores relacionais
    >   maior que
    <   menor que
    >=  maior ou igual
    <=  menor ou igual
*/
/* Operadores lógicos
    &&  e
    ||  ou
    !   não
*/