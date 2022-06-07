eLeft = document.getElementById('left');
eRight = document.getElementById('right');

document.getElementById('high-score').innerHTML = "High Score: " + localStorage.getItem("highScore");
document.getElementById('score').innerHTML = "Score: 0";

teamIndex = 0;
score = 0;

function storageCheck() {
  if (localStorage.getItem("highScore") == null) {
    localStorage.setItem("highScore", 0);
  }
}