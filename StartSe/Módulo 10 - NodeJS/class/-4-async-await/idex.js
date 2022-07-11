import fetch from "node-fetch";
// https://api.github.com/users/orllean

function main() {
	const user = "orllean";
	const apiUrl = "https://api.github.com";
	fetch(`${apiUrl}/users/${user}`)
		.then((response) => {
			return response.json();
		})
		.then((user) => {
			console.log(`User with fetch: ${user.name}`);
		});
}

async function mainAsyncAwait() {
	const gitUser = "orllean";
	const apiUrl = "https://api.github.com";
	const response = await fetch(`${apiUrl}/users/${gitUser}`);
	const user = await response.json();
	console.log(`User with async/await: ${user.name}`);
}

async function getGitUsersId() {
	const gitUser1 = "orllean";
	const gitUser2 = "rprrafa";
	const apiUrl = "https://api.github.com";
	const response1 = await fetch(`${apiUrl}/users/${gitUser1}`);
	const response2 = await fetch(`${apiUrl}/users/${gitUser2}`);
	const user1 = await response1.json();
	const user2 = await response2.json();
	console.log(`${user1.name} ID: ${user1.id}`);
	console.log(`${user2.name} ID: ${user2.id}`);
}

async function getGitUsersIdPromieAll() {
	const gitUser1 = "orllean";
	const gitUser2 = "rprrafa";
	const apiUrl = "https://api.github.com";
	const response1 = fetch(`${apiUrl}/users/${gitUser1}`);
	const response2 = fetch(`${apiUrl}/users/${gitUser2}`);
	const promises = await Promise.all([response1, response2])
	const user1 = await promises[0].json();
	const user2 = await promises[1].json();
	console.log(`${user1.name} ID: ${user1.id}`);
	console.log(`${user2.name} ID: ${user2.id}`);
}

// main();
// mainAsyncAwait();
// getGitUsersId();
getGitUsersIdPromieAll()