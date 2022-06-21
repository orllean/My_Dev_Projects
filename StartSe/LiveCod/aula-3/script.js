const mario = document.querySelector(".super-mario");
const pipe = document.querySelector(".pipe-game");

const jump = () => {
	mario.classList.add("jump-mario");
	setTimeout(() => {
		mario.classList.remove("jump-mario");
	}, 500);
};

document.addEventListener("keypress", jump);

const loopGame = setInterval(() => {
	const pipePosition = pipe.offsetLeft;
	const marioPosition = +window
		.getComputedStyle(mario)
		.bottom.replace("px", "");

	if (pipePosition <= 120 && pipePosition > 0 && marioPosition < 80) {
		pipe.style.anination = "none";
		pipe.style.left = `${pipePosition}px`;

		mario.style.anination = "none";
		mario.style.botton = `${marioPosition}px`;
		mario.src = "./assets/mario-game-over.png";
		mario.style.width = "75px";
		mario.style.marginLeft = "45px";

		clearInterval(loopGame);
	}
}, 10);
