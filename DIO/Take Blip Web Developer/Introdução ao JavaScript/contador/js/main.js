let count = 0;
const NUMBER = document.getElementById('number')

function increment() {
    count++;
    NUMBER.innerHTML = count;
}

function decrement() {
    count--;
    NUMBER.innerHTML = count;
}