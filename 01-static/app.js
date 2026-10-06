let clicks = 0;

const counter = document.getElementById("counter");
const button = document.getElementById("bump");

button.addEventListener("click", () => {
  clicks += 1;
  counter.textContent = `Clicks: ${clicks}`;
});
