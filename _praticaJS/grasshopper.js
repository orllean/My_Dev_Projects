var arr=[
    'apples',
    'bananas',
    'orange'
];
var arr1=[
    'blue',
    'green',
    'black'
];
//console.log(arr)

for (const item of arr) {
    //console.log(item)
}

for (var adj of [
    'ragging',
    'happy',
    'hungry'
    ]) 
{    
    for (var noun of [
        'dad',
        'kid1',
        'kid2'
        ]) 
    {        
        //console.log('the ' + adj + ' ' + noun)
    }
}

var aluno=[
    {
        name:'papai',
        sex:'male',
        year:'1970'
    }
];

i=0
for (var iterator of arr) {
    i++
    //console.log(i)
}

for (i=0; i<=2; i++) {
    //console.log(i)
    //console.log(aluno[i])
}
//console.log(`Aluno: ${aluno.name}`)
var menssage=
'Today we are going shopping!';
menssage=menssage.replace('day', 'morrow');
//console.log(menssage);

//console.log('I code'.length)
//console.log('I code'.includes('love'))
//console.log(arr.length)

//console.log(arr.includes('bananas'))

//varible scope
var myGlobalNum=5;
if (myGlobalNum>3) {
    let myLocalNum=4
    /* console.log(myLocalNum)
    console.log(myGlobalNum)
    console.log(`${myGlobalNum} + ${myLocalNum} soma possível dentro do scopo `)
    console.log(myGlobalNum + myLocalNum) */
}
//declaração impossivel => console.log(myGlobalNum + myLocalNum)

var collor='yellow'
//console.log(collor)

for (let collor of [
    'blue1',
    'green1',
    'black1'
]) {
    //console.log(collor)
}

for (let collor of arr1) {
    //console.log(collor)
}

//console.log(collor)

//ternary operator

var train=Math.floor(Math.random() * 4);
var car=Math.floor(Math.random() * 3);

car<train?console.log('drive a car'):console.log('buy train tickets')

// += additional assignment -= subtract assingnment

let ant=60;
let gift=5;
let grasshopper=0;

for(i=0;i<3;i++){
    ant-=gift;
    grasshopper+=gift
    //console.log(`ant: ${ant} grasshopper: ${grasshopper}`)
}

//create a function declaration that uses a retrun statement
//EX_1

let wallet=50;
function inYen(dollars) {
    let yen=dollars*113;
    return yen;
}

function inBath(dollars) {
    let bath=dollars*33;
    return bath;
}

//console.log(wallet + ' US dollars is:')
//console.log(inYen(wallet) + ' Japanese yen:')
//console.log(inBath(wallet) + ' Taih bath:')

//EX_2
arr2=[
    25,
    21,
    53,
    46,
    16
];

function large(a, b){
    return a>b?a:b;
}

function maximum(array){
    let max=0;
    for (let num of array) {
        max=large(max, num);
    }
    return max;
};

for (let list of arr2) {
    //console.log(list)
}
//console.log(maximum(arr2))

//recursive function-1
function sendPostcards(amount) {
    console.log('Postcard '+amount+' sent!');
    if (amount===1) {
        console.log('All Postcards sent!');
        return amount;        
    } else {
        let amountRemaing=amount-1;
        console.log('Calling function again:');
        return sendPostcards(amountRemaing);
    }
};

//sendPostcards(5)

//recursive function-2
const travelDocument='Hello grasshoperTravel! You will ge going to Brasil. You travel code is: "no1grasshoper" Enjoy your trip grasshoper'

function updateAllNames(string, oldPart, newPart) {
    if (string.includes(oldPart)===false) {
        return string;
    }
    
    string=string.replace(oldPart, newPart);
    return updateAllNames(string, oldPart, newPart);
};

//console.log(travelDocument);
//console.log(updateAllNames(travelDocument, 'grasshoper', 'grasshopper'));

//recursive function-3
function sumUpTo(number){
    if (number===1) {
        console.log('befor: '+number)
        return 1;
    }
    console.log('affter: '+number)
    return number+sumUpTo(number-1);
}
//sumUpTo(3)=>(3+sumUpTo(2))
//sumUpTo(2)=>(2+sumUpTo(1))
//sumUpTo(1)=>1)
//so, sumUpTo(3) returns (3 + (2 + (1))) which is 6
console.log(sumUpTo(3))

//recursive function-3
function ftl(n){
    if (n===1) {
        return 1;
    }
    return n*ftl(n-1);
};
console.log(ftl(4))

//Array - length (comprimento do array)
let numberOfItems=arr.length; 
console.log('There are '+numberOfItems+' items in arr')

//Array - slice(x,y) x=> to start y=> to end not included (uma parte, porção do array original)
console.log(arr1.slice(2, 3));

//Array - push (add um novo elemento no final do array)
let last=aluno[aluno.length-1]
console.log(last)
let newAluno={
    name:   'brisa',
    sex:    'female',
    year:    '2009'
};
aluno.push(newAluno);
last=aluno[aluno.length-1];
console.log(last)
//console.log(last.name)


//Array - pop (remove o ultimo elemento de um array)
let atUltimoAluno=aluno.pop();
atUltimoAluno.year='2010';
aluno.push(atUltimoAluno)
last=aluno[aluno.length-1];
console.log(last)
//console.log(last.year)

var arr3=[
    1,
    3,
    5,
    7
]
let trocaUltimo=arr3.pop();
trocaUltimo=9;
arr3.push(trocaUltimo);
console.log(arr3);