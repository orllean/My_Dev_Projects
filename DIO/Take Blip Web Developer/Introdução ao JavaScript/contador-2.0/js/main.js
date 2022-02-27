let count = 0;
const NUMBER = document.getElementById('number');
const ADD = document.getElementById('add');
const SUB = document.getElementById('sub');
ADD.addEventListener("click", increment);
SUB.addEventListener("click", decrement);

function increment() {
    count++;
    NUMBER.innerHTML = count;
    colorNumber (count);
    switchButtum (count)    
}

function decrement() {
    count--;
    NUMBER.innerHTML = count;
    colorNumber (count);
    switchButtum (count)    
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

function switchButtum (num) {
    if (count == 10) {
        ADD.disabled = true;
        ADD.style.cursor = 'default';
        ADD.style.border = 'none';
    } else {
        ADD.disabled = false;
        ADD.style.cursor = 'pointer';
        ADD.style.border = 'solid';

    }
    if (count == -10) {
        SUB.disabled = true;
        SUB.style.cursor = 'default';
        SUB.style.border = 'none';
    } else {
        SUB.disabled = false;
        SUB.style.cursor = 'pointer';
        SUB.style.border = 'solid';

    }
}