//Maps are Objects
// creat a map and set values
const fruits = new Map([
	["apples", 500],
	["bananas", 300],
	["oranges", 200],
]);
// The get() method gets the value of a key in a Map:
console.log(fruits.get("bananas"));

// creat a map
const stack = new Map();
// set map values
// The set() method can also be used to change existing Map values:
stack.set("HTML 5", "front-end");
stack.set("css", "front-end");
stack.set("javaScript", "front-end");
stack.set("PHP", "back-end");
stack.set("Phyton", "back-end");
console.log(stack.get("css"));
//The size property returns the number of elements in a Map:
console.log(fruits.size);
console.log(stack.size);
//The delete() method removes a Map element:
fruits.delete("apples");
console.log(fruits.size);
//The clear() method removes all the elements from a Map:
fruits.clear();
console.log(fruits.size);
//The has() method returns true if a key exists in a Map:
console.log(stack.has("javaScript"));

//Sets
//Sets are Objects
//A JavaScript Set is a collection of unique values. Each value can only occur once in a Set. If you add equal elements, only the first will be saved. A Set can hold any value of any data type.
// Create a Set with elements
const vowel = new Set(["a", "i", "u", "o", "e"]);
// Create a Set
const consonant = new Set();
// add value to the Set
consonant.add("g");
consonant.add("b");
consonant.add("d");
consonant.add("c");
consonant.add("f");

//The has() method returns true if a value exists.
console.log(vowel.has("b"));
//The size property returns the number of elements:
console.log(consonant.size);
//Removes an element from a Set
consonant.delete("f");
console.log(consonant.size);

//The forEach() method invokes a function for each Set element:
vowel.forEach(function (e) {
	console.log(e);
});
//The values() method returns an Iterator object containing all the values in a Set:
console.log(consonant.values());
//Now you can use the Iterator object to access the elements:
const element = consonant.values();
for (const i of element) {
	console.log(i);
}
