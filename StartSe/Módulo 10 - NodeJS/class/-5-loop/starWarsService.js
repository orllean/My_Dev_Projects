import fetch from "node-fetch";

const apiUrl = "https://swapi.dev/api";

async function getPeople(page = 1) {
	const respose = await fetch(`${apiUrl}/people?page=${page}`);
	const poeple = await respose.json();

	return poeple.results;
}

export { getPeople };
