//Atividade 1
const alunos = [
	{
		nome: "João",
		nota: 5,
		turma: "1B",
	},
	{
		nome: "Sofia",
		nota: 9,
		turma: "1B",
	},
	{
		nome: "Paulo",
		nota: 6,
		turma: "2C",
	},
];

function alunosAprovados(arr, media) {
	let aprovados = [];
	for (let i = 0; i < arr.length; i++) {
		const { nome, nota } = arr[i];
		if (nota >= media) {
			aprovados.push(nome);
		}
	}
	return aprovados;
}

console.log(alunosAprovados(alunos, 6));

//Atividade 2

function calculaIdade(anos) {
	return `Daqui a ${anos} anos, ${this.nome} terá ${
		this.idade + anos
	} anos de idade.`;
}

const pessoa1 = {
	nome: "Papai",
	idade: 51,
};
const pessoa2 = {
	nome: "Brisa",
	idade: 15,
};
const pessoa3 = {
	nome: "Arthur",
	idade: 12,
};

console.log(calculaIdade.apply(pessoa1, [25]));
console.log(calculaIdade.call(pessoa2, 25));
