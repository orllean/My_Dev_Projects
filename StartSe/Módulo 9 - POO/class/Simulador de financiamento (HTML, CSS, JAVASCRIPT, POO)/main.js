import { installments } from "./installments.js";
import { financing } from "./financing.js";

const listPeriod = document.querySelector("#listPeriod");
const chkPeriod = document.querySelector("#chkPeriod");

chkPeriod.addEventListener("change", function () {
	if (this.checked) {
		listPeriod.removeAttribute("hidden");
	} else {
		listPeriod.setAttribute("hidden", "hidden");
	}
});
