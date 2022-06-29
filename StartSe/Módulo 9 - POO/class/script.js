"use strict";

class aluno {
	static DANGAY = 0;
	static YUDANSHA = 1;
	nome;
	sexo;
	nasc;
	constructor(nome, sexo = "m", nasc, grau = 0) {
		this.nome = nome;
		this.sexo = sexo;
		this.nasc = nasc;
		this.grau = grau;
	}
	getDados() {
		this.sexo == "m" ? (this.sexo = "masculino") : (this.sexo = "feminino");
		return `Nome: ${this.nome} Sexo: ${this.sexo} ${this.#getIdade()}`;
	}
	#getIdade() {
		let year = new Date(Date.now()).getFullYear();
		let idade = year - new Date(Date.parse(this.nasc)).getFullYear();
		return `Idade: ${idade}`;
	}
}

const aluno1 = new aluno("maria", "f");
const aluno2 = new aluno("joão");
aluno1.nasc = "09/22/2000";
aluno2.grau = aluno.YUDANSHA;
const aluno3 = new aluno();
aluno3.nome = "zé";
aluno3.grau = aluno.YUDANSHA;
aluno3.nasc = "07/25/1971";
const aluno4 = new aluno("ana", "f", aluno.DANGAY);

class cAluno {
	#nome;
	#sexo;
	#nasc;

	constructor(nome, sexo = "m", nasc) {
		this.#nome = nome;
		this.#sexo = sexo;
		this.#nasc = nasc;
	}

	setNome(nome) {
		nome.length > 3
			? (this.#nome = nome)
			: alert("digite um nome comn 3 caracteres ao menos.");
	}

	setSexo(sexo) {
		if ((sexo.length == 1 && sexo == "m") || sexo == "f") {
			this.#sexo = sexo;
		} else {
			alert("digite M ou F.");
		}
	}

	getDados() {
		this.#sexo == "m" ? (this.#sexo = "masculino") : (this.#sexo = "feminino");
		return `Nome: ${this.#nome} Sexo: ${this.#sexo} ${this.#getIdade()}`;
	}

	#getIdade() {
		let year = new Date(Date.now()).getFullYear();
		let idade = year - new Date(Date.parse(this.#nasc)).getFullYear();
		return `Idade: ${idade}`;
	}
}

const aluno5 = new cAluno("leo", "m", "07/25/1971");
