var arr = ["apples", "bananas", "orange"];
var arr1 = ["blue", "green", "black"];
//console.log(arr)

for (const item of arr) {
	//console.log(item)
}

for (var adj of ["ragging", "happy", "hungry"]) {
	for (var noun of ["dad", "kid1", "kid2"]) {
		//console.log('the ' + adj + ' ' + noun)
	}
}

var aluno = [
	{
		name: "papai",
		sex: "male",
		year: "1970",
	},
];

i = 0;
for (var iterator of arr) {
	i++;
	//console.log(i)
}

for (i = 0; i <= 2; i++) {
	//console.log(i)
	//console.log(aluno[i])
}
//console.log(`Aluno: ${aluno.name}`)
var menssage = "Today we are going shopping!";
menssage = menssage.replace("day", "morrow");
//console.log(menssage);

//console.log('I code'.length)
//console.log('I code'.includes('love'))
//console.log(arr.length)

//console.log(arr.includes('bananas'))

//varible scope
var myGlobalNum = 5;
if (myGlobalNum > 3) {
	let myLocalNum = 4;
	/* console.log(myLocalNum)
    console.log(myGlobalNum)
    console.log(`${myGlobalNum} + ${myLocalNum} soma possível dentro do scopo `)
    console.log(myGlobalNum + myLocalNum) */
}
//declaração impossivel => console.log(myGlobalNum + myLocalNum)

var collor = "yellow";
//console.log(collor)

for (let collor of ["blue1", "green1", "black1"]) {
	//console.log(collor)
}

for (let collor of arr1) {
	//console.log(collor)
}

//console.log(collor)

//ternary operator

var train = Math.floor(Math.random() * 4);
var car = Math.floor(Math.random() * 3);

//car < train ? console.log("drive a car") : console.log("buy train tickets");

// += additional assignment -= subtract assingnment

let ant = 60;
let gift = 5;
let grasshopper = 0;

for (i = 0; i < 3; i++) {
	ant -= gift;
	grasshopper += gift;
	//console.log(`ant: ${ant} grasshopper: ${grasshopper}`)
}

//create a function declaration that uses a retrun statement
//EX_1

let wallet = 50;
function inYen(dollars) {
	let yen = dollars * 113;
	return yen;
}

function inBath(dollars) {
	let bath = dollars * 33;
	return bath;
}

//console.log(wallet + ' US dollars is:')
//console.log(inYen(wallet) + ' Japanese yen:')
//console.log(inBath(wallet) + ' Taih bath:')

//EX_2
arr2 = [25, 21, 53, 46, 16];

function large(a, b) {
	return a > b ? a : b;
}

function maximum(array) {
	let max = 0;
	for (let num of array) {
		max = large(max, num);
	}
	return max;
}

for (let list of arr2) {
	//console.log(list)
}
//console.log(maximum(arr2))

//recursive function-1
function sendPostcards(amount) {
	console.log("Postcard " + amount + " sent!");
	if (amount === 1) {
		console.log("All Postcards sent!");
		return amount;
	} else {
		let amountRemaing = amount - 1;
		console.log("Calling function again:");
		return sendPostcards(amountRemaing);
	}
}

//sendPostcards(5)

//recursive function-2
const travelDocument =
	'Hello grasshoperTravel! You will ge going to Brasil. You travel code is: "no1grasshoper" Enjoy your trip grasshoper';

function updateAllNames(string, oldPart, newPart) {
	if (string.includes(oldPart) === false) {
		return string;
	}

	string = string.replace(oldPart, newPart);
	return updateAllNames(string, oldPart, newPart);
}

//console.log(travelDocument);
//console.log(updateAllNames(travelDocument, 'grasshoper', 'grasshopper'));

//recursive function-3
function sumUpTo(number) {
	if (number === 1) {
		//console.log('befor: '+number)
		return 1;
	}
	//console.log('affter: '+number)
	return number + sumUpTo(number - 1);
}
//sumUpTo(3)=>(3+sumUpTo(2))
//sumUpTo(2)=>(2+sumUpTo(1))
//sumUpTo(1)=>1)
//so, sumUpTo(3) returns (3 + (2 + (1))) which is 6
//console.log(sumUpTo(3))

//recursive function-3
function ftl(n) {
	if (n === 1) {
		return 1;
	}
	return n * ftl(n - 1);
}
//console.log(ftl(4))

//Array - length (comprimento do array)
let numberOfItems = arr.length;
//console.log('There are '+numberOfItems+' items in arr')

//Array - slice(x,y) x=> to start y=> to end not included (uma parte, porção do array original)
//console.log(arr1.slice(2, 3));

//Array - push (add um novo elemento no final do array)
let last = aluno[aluno.length - 1];
//console.log(last)
let newAluno = {
	name: "brisa",
	sex: "female",
	year: "2009",
};
aluno.push(newAluno);
last = aluno[aluno.length - 1];
//console.log(last)
//console.log(last.name)

//Array - pop (remove o ultimo elemento de um array)
let atUltimoAluno = aluno.pop();
atUltimoAluno.year = "2010";
aluno.push(atUltimoAluno);
last = aluno[aluno.length - 1];
//console.log(last)
//console.log(last.year)

var arr3 = [1, 3, 5, 7];
let trocaUltimo = arr3.pop();
trocaUltimo = 9;
arr3.push(trocaUltimo);
//console.log(arr3);

//use spread (...) operator to copy all elements of an array into another array
let arr4 = [...arr3, ...arr2];
//console.log(arr4)

let timeTravel = ["6am", "8am", "10am", "12pm", "14pm", "16pm"];

function morning(time) {
	return time.includes("am");
}

function evening(time) {
	return time.includes("pm");
}

let amTimes = timeTravel.filter(morning);
let pmTimes = timeTravel.filter(evening);

//console.log("Day times: " + amTimes);
//console.log("Eveni times: " + pmTimes);

//let number=[];
let maxNum = arr4[0];
let minNum = arr4[0];
//console.log(maxNum)
function compareToMaximum(value) {
	maxNum = value > maxNum ? value : maxNum;
}
function compareToMinimum(value) {
	maxNum = value < minNum ? value : maxNum;
}

arr4.forEach(compareToMaximum);
arr4.forEach(compareToMinimum);

//console.log('Maximum:' + maxNum);
//console.log('Minimum:' + minNum);

//I'm stuck in it ***no more***
const myBooks = [
	new Object({
		title: "1984",
		author: "George Orwell",
		isAvailable: false,
	}),
	new Object({
		title: "Becoming",
		author: "Michele Obama",
		isAvailable: false,
	}),
	new Object({
		title: "Berserk",
		author: "Kentaro Miura",
		isAvailable: true,
	}),
	new Object({
		title: "A revolução dos bichos",
		author: "George Orwell",
		isAvailable: true,
	}),
];

function printBookByAuthor(books) {
	console.log("-----Book_Info-----");
	console.log("Title: " + books.title);
	console.log("Author: " + books.author);
	console.log("Avalable: " + books.isAvailable, "\n"); // ,'\n' insere uma quebra de linha
}

function findAuthor(author) {
	let findBook = [];
	for (const book of myBooks) {
		if (book.author === author) {
			findBook.push(book);
		}
	}
	return findBook;
}

function getData(name, search) {
	search(name);
	return search(name);
}

let orwellBooks = getData("George Orwell", findAuthor);
orwellBooks.forEach(printBookByAuthor);

/* function findAuthor(author) {
	let findBook = [];
	for (const i of myBooks) {
		if (i.author === author) {
			findBook.push(i);
		}
	}
	return findBook;
} */

//let orwellBooks = findAuthor("George Orwell");

for (const b of myBooks) {
	//console.log(b.title);
}

let numbers = [2, 3, 5];
function sum(numberArray) {
	let result = 0;
	for (const i of numberArray) {
		result += i;
	}
	return result;
}
//console.log("\n", sum(numbers), "\n");

for (let i = 0 - 3; i < 4; i++) {
	if (i) {
		//console.log(i);
	}
}

let shapes = ["triangle", "square", "pentagon", "circle"];

function setLastValue(arr, str) {
	let last = arr.length - 1;
	arr[last] = str;
}

setLastValue(shapes, "hexagon");
for (const i of shapes) {
	//console.log(i);
}

function getNeighbor(arr, i) {
	let neighborIndex = i + 1;
	return arr[neighborIndex];
}
/* console.log(
	"\n",
	"The neighbor to " + shapes[1] + " is " + getNeighbor(shapes, 1),
	"\n"
); */

for (let index = 0; index < "fruit".length; index++) {
	//console.log("fruit"[index]);
}

for (let index = 0; index < "fruit".length - 1; index++) {
	let neighborIndex = index + 1;
	//console.log("fruit"[index]);
	//console.log("fruit"[neighborIndex]);
}

let obj = [];
let str = "ORLEAN";

for (let i = 0; i < str.length; i++) {
	let letter = str[i];
	obj[letter] = i;
}

//console.log("\n", obj, "\n");

for (let property in obj) {
	//console.log(property + ": " + obj[property]);
}

let randomWord = "tact";
function check(space, word) {
	if (space.length !== word.length) {
		return false;
	}
	for (let i = 0; i < space.length; i++) {
		if (space[i] !== "-" && space[i] !== word[i]) {
			return false;
		}
	}
	return true;
}
/* console.log('-a-t');
console.log(randomWord);
console.log(check('-a-t', randomWord)) */

let stringSequence = ["Orlean", "Arthur", "Brisa"];
function longestWord(arr) {
	let biggestWord = "";
	for (const word of arr) {
		if (word.length > biggestWord.length) {
			biggestWord = word;
		}
	}
	return biggestWord;
}
//console.log(stringSequence);
//console.log("O maior nome do array é:", longestWord(stringSequence), "\n");

let string = "Arthur";
function mapString(str) {
	let map = {};
	for (let i = 0; i < str.length; i++) {
		let letter = str[i];
		if (map[letter]) {
			map[letter].push(i);
		} else {
			map[letter] = [i];
		}
	}
	return map;
}
//console.log(string, "\n");
//console.log(mapString(string), "\n");

let stringMap = mapString(string);
for (const letter in stringMap) {
	//console.log(letter, ": ", stringMap[letter]);
}

let dictionaryWord = "blue";
let sequenceString = "hullabaloo";

function compareLatters(word, object) {
	for (const letter of word) {
		if (object[letter]) {
		} else {
			return false;
		}
	}
	return true;
}
//console.log("\n");
console.log(dictionaryWord);
console.log(sequenceString);

let stringSequenceMap = mapString(sequenceString);
for (const letter in stringSequenceMap) {
	//console.log(letter, ": ", stringSequenceMap[letter]);
}
//console.log(compareLatters(dictionaryWord, stringSequenceMap));

function findNextIndex(array, minIndex) {
	for (const i of array) {
		if (i >= minIndex) {
			return i + 1;
		}
	}
	return false;
}

function isSubsequence(word, map) {
	let minIndex = 0;
	for (let letter of word) {
		if (map[letter]) {
			minIndex = findNextIndex(map[letter], minIndex);
			if (minIndex === false) {
				return false;
			}
		} else {
			return false;
		}
	}
	return true;
}

let mappedString = mapString(sequenceString);
console.log(isSubsequence(dictionaryWord, mappedString));
