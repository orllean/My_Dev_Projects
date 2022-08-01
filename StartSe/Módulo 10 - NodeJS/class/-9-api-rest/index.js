import express from "express";

const app = express();
const PORT = 3000;
let users = [
	{ id: 1, name: "Rafael Ribeiro", age: 31 },
	{ id: 2, name: "Orlean Costa", age: 51 },
];
app.listen(PORT, () => {
	console.log(`servidor rodando na em http://localhost:${PORT}`);
});

app.get("/", (request, response) => {
	return response.send("<h1>Trabalhando com servidor Express</h1>");
});

app.get("/users", (request, response) => {
	return response.send(users);
});
