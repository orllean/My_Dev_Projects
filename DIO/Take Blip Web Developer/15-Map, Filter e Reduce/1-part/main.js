const maca = {
	value: 2,
	cat: 5,
};

const laranja = {
	value: 5,
	cat: 8,
};

function mapComThis(arr, thisArg) {
	return arr.map(function (item, index) {
		return `${item * this.cat}, ${index}`;
	}, thisArg);
}

const nums = [2, 3];

console.log(mapComThis(nums, maca));
console.log(mapComThis(nums, laranja));
