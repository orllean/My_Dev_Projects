import { getPeople } from "./starWarsService.js";

async function main() {
	const starWarsPeople = await getPeople(1);
	// console.log(starWarsPeople);
	const totalHeight = starWarsPeople.reduce((total, person) => {
		total += Number(person.height);
		return total;
	}, 0);

	console.log("média de altura: ", totalHeight / starWarsPeople.length);
}

main();
