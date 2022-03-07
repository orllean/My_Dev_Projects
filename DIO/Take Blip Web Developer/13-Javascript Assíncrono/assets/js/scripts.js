const BASE_URL = "https://thatcopy.pw/catapi/rest/";
const btCat = document.getElementById("change-cat");
const imgCat = document.getElementById("cat");

const getCats = async () => {
	try {
		const data = await fetch(BASE_URL);
		const json = await data.json();

		return json.webpurl;
	} catch (e) {
		console.log(e.mensage);
	}
};

const loadImg = async () => {
	imgCat.src = await getCats();
};

btCat.addEventListener("click", loadImg);

loadImg();
