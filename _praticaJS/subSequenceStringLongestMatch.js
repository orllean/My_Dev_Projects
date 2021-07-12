function longestWord(arr) {
	let biggestWord = "";
	for (const word of arr) {
		if (word.length > biggestWord.length) {
			biggestWord = word;
		}
	}
	return biggestWord;
}

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

function longestMatch(dictionary, string) {
	let arr = [];
	let map = mapString(string);
	for (const word of dictionary) {
		if (isSubsequence(word, map)) {
			arr.push(word);
		}
	}
	return longestWord(arr);
}

let sequenceString = "javascript";
let dictionaryWord = ["art", "vascular", "avast", "javas", "vat"];

//console.log('\r\n');
console.log("String: ", sequenceString);
console.log("Dictionary word: ", dictionaryWord);

console.log(
	"The longest subsequence of the string is: ",
	longestMatch(dictionaryWord, sequenceString)
);
