import express from "express";

const app = express();
const PORT = 3000;

app.listen(PORT, () => {
	console.log(`servidor rodando na em http://localhost:${PORT}`);
});

app.get("/", (request, response) => {
	return response.send("<h1>Trabalhando com servidor Express</h1>");
});
