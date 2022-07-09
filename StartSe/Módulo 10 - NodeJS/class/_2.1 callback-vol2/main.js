function mensagemGabriel() {
	const mensagemGabrielPromise = new Promise((resolve, reject) => {
		setTimeout(() => {
			console.log("bebam água");
			resolve();
		}, 0);
	});
	return mensagemGabrielPromise;
}

function mensagemRafael() {
	console.log("bora pra cima");
}

mensagemGabriel().then(mensagemRafael);
