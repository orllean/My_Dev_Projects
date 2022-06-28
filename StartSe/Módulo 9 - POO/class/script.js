"use strict";

class aluno {
	static DANGAY = 0;
	static YUDANSHA = 1;
	nome;
	sexo;
	constructor(nome, sexo = "m", grau = 0) {
		this.nome = nome;
		this.sexo = sexo;
		this.grau = grau;
	}
	getDados() {
		this.sexo == "m" ? (this.sexo = "masculino") : (this.sexo = "feminino");
		return `Nome: ${this.nome} sexo: ${this.sexo}`;
	}
}

const aluno1 = new aluno("maria", "f");
const aluno2 = new aluno("joão");
aluno2.grau = aluno.YUDANSHA;
const aluno3 = new aluno();
aluno3.nome = "zé";
aluno3.grau = aluno.YUDANSHA;
const aluno4 = new aluno("ana", "f", aluno.DANGAY);
