import { getPeople } from "./starWarsService.js";

async function main() {
	const starWarsPeople = await getPeople(1);
	// console.log(starWarsPeople);

	/* for (let i = 0; i < starWarsPeople.length; i++) {
		console.log(starWarsPeople[i].name);
	} */

	/* for (const key in starWarsPeople[0]) {
		console.log(key);
		console.log(starWarsPeople[0][key]);
	} */

	/* for (const person of starWarsPeople) {
		console.log(person.name);
	} */

	const starWarsPeopleNames = starWarsPeople.map((person) => {
		/* const name = person.name;
		const height = person.height; */
		// use destrution
		const { name, height, gender } = person;
		return { name, height, gender };
	});
	console.log(starWarsPeopleNames);
}

main();
