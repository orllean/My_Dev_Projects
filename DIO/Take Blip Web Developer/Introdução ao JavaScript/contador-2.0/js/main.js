let count = 0;
const NUMBER = document.getElementById('number')
document.getElementById('add').addEventListener("click", increment);
document.getElementById('sub').addEventListener("click", decrement);

function increment() {
    count++;
    NUMBER.innerHTML = count;
    colorNumber (count);
}

function decrement() {
    count--;
    NUMBER.innerHTML = count;
    colorNumber (count);
}

function colorNumber (num) {
    if (num > 0) {
        NUMBER.style.color = 'darkblue';
    } else if (num < 0) {
        NUMBER.style.color = 'darkmagenta';        
    } else {
        NUMBER.style.color = 'black';        
    }    
}