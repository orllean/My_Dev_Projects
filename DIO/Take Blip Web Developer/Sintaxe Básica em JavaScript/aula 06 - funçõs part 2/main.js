//funções declarativas
function welcome() {
    console.log('Hello cruel world!');
}
welcome()
//expressão de função
//com nome e sem na função
var f_1 = function log1() {
    console.log('Exemplo 1 function em expressão c/ nome');
}
f_1()
var f_2 = function () {
    console.log('Exemplo 2 function em expressão s/ nome');
}
f_2()
//arrow function
var f_3 = () => {
    console.log('Exemplo 3 arrow function');
}
f_3()