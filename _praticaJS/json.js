// Json = JavaScript Object Notation

//Object format
const book={
    title: '1984',
    author: 'George Orwell',
    isAvailable: false
};
//convert to Json.stringify()
const bookJson=JSON.stringify(book);
console.log(bookJson);

const copys=[book, book]
const jsonBooks=JSON.stringify(copys);
console.log(jsonBooks);

//convert to javascript object

//json text
const jsonObj='{"title":"Becoming","author":"Michele Obama","isAvailable":true}'
//to object
const book2=JSON.parse(jsonObj);
console.log(book);
console.log(book2);

const library=[book,book2];
console.log(library);
console.log(library[0].author);
console.log('\n ----------------')

//objects in javascript

const myBooks=[
    new Object({ title: '1984', author: 'George Orwell', isAvailable: false }),
    new Object({ title: 'Becoming', author: 'Michele Obama', isAvailable: true })
];

console.log(myBooks.length);
console.log(myBooks);