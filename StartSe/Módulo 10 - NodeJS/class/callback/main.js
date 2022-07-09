function mensagemGabriel(callback) {
	setTimeout(() => {
		console.log("bebam água");
		callback();
	}, 0);
}

function mensagemRafael() {
	console.log("bora pra cima");
}

mensagemGabriel(mensagemRafael);
// mensagemRafael();
