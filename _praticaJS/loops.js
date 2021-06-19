//while
const names=['papai', 'arthur', 'brisa']
let index=0;

while(index<names.length){
    const name=names[index];
    //console.log(name);
    index++;
}

for (let index = 0; index < names.length; index++) {
    const element = names[index];
    //console.log(element);
}

for (const iterator of names) {
    console.log(iterator)
}