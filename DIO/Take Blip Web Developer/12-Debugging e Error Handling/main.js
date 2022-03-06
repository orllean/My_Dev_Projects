function validaArray2(arr, num) {
	try {
		switch (true) {
			case !arr && !num:
				throw new ReferenceError("Envie os parâmetros");
				break;
			case typeof arr !== "object":
				throw TypeError("arr precisa ser do tipo Object");
				break;
			case arr.length !== num:
				throw RangeError("O array não tem a quantidade de itens esperado");
				break;

			default:
				return arr;
		}
	} catch (e) {
		if (e instanceof ReferenceError) {
			console.log("Erro de referência");
			console.log(e.message);
		} else if (e instanceof TypeError) {
			console.log("Erro de tipo");
			console.log(e.message);
		} else if (e instanceof RangeError) {
			console.log("Erro de range");
			console.log(e.message);
		} else {
			console.log("Tipo de erro não esperado:" + e);
		}
	}
}
/* function validaArray(arr, num) {
	try {
		if (!arr && !num) throw new ReferenceError("Envie os parâmetros");
		if (typeof arr !== "object")
			throw TypeError("arr precisa ser do tipo Object");
		if (typeof num !== "number")
			throw TypeError("num precisa ser do tipo número");
		if (arr.length !== num)
			throw RangeError("O array não tem a quantidade de itens esperado");
		return arr;
	} catch (e) {
		if (e instanceof ReferenceError) {
			console.log("Erro de referência");
			console.log(e.message);
		} else if (e instanceof TypeError) {
			console.log("Erro de tipo");
			console.log(e.message);
		} else if (e instanceof RangeError) {
			console.log("Erro de range");
			console.log(e.message);
		} else {
			console.log("Tipo de erro não esperado:" + e);
		}
	}
} */
console.log(validaArray2([1, 2], 3));
