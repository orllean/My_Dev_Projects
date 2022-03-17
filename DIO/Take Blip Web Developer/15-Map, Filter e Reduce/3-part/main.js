const arr = [1, 2, 3, 4, 5];

function retornaPares(arr) {
	return arr.filter((num) => {
		return num % 2 === 0;
	});
}

console.log(retornaPares(arr));
