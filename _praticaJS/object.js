//define a simple object (with no propeties or methods)

/* const blank = {};
console.log("Blank type: ", typeof blank);
console.log("Blank value: ", blank);
 */

//define an object with PROPERTIES (atributes)

/* 
const book = {
	title: "1994",
	author: "George Orwell",
	isAvailable: false,
};
console.log("Book type: ", typeof book);
console.log("Book value: ", book);
 */

//add actions we can take on it

/* 
const book = {
	title: "1994",
	author: "George Orwell",
	isAvailable: false,
	checkIn: function () {
		this.isAvailable = true;
	},
	checkOut: function () {
		this.isAvailable = false;
	},
};
console.log("Book type: ", typeof book);
console.log("Book value: ", book);
 */

//created objects using CONSTRUTORS

/* 
const book = new Object();
console.log("Book type: ", typeof book);
console.log("Book value: ", book);
console.log('\n');

const data={ title: '1994', author: 'George Orwell', isAvailable: false };
const book1=new Object(data);
console.log("Book1 type: ", typeof book1);
console.log("Book1 value:\n ", book1);
 */

//access PROPERTIES and METHODS

const book = {
	title: "1994",
	author: "George Orwell",
	isAvailable: false,
	checkIn: function () {
		this.isAvailable = true;
	},
	checkOut: function () {
		this.isAvailable = false;
	},
};
console.log(book.author);
book.author = "G. Orwell";
console.log(book.author);
console.log("\n");

console.log("Is available: ", book.title, book.isAvailable);
book.checkIn();
console.log("Is available: ", book.title, book.isAvailable);
