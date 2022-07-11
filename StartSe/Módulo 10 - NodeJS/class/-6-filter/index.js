import { getPeople } from "./starWarsService.js";

async function main() {
	const starWarsPeople = await getPeople(1);
	// console.log(starWarsPeople);
	const starWarsPeopleFiltered = starWarsPeople
		.filter((person) => {
			return person.gender === "female";
		})
		.map((person) => {
			return { name: person.name, gender: person.gender };
		});
	console.log(starWarsPeopleFiltered);
}

main();
