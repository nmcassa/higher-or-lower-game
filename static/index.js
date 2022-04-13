eLeft = document.getElementById('left');
eRight = document.getElementById('right');

document.getElementById('high-score').innerHTML = "High Score: " + localStorage.getItem("highScore");
document.getElementById('score').innerHTML = "Score: 0";

listOfRLTeams = [];
teamIndex = 0;
score = 0;

function storageCheck() {
  if (localStorage.getItem("highScore") == null) {
    localStorage.setItem("highScore", 0);
  }
}

fetch('/test')
      .then(function (response) {
        if (!response.ok) {
          throw new Error("HTTP error, status = " + response.status);
        }
        return response.json();
      }).then(function (text) {
          console.log('GET response:');
          console.log(text.message);
          myDisplayer(text.message);
      });

async function myDisplayer(some) {
  listOfRLTeams = await some;

  //splits the list into a 2D array with 
  //each row containing [name][winnings]
  for (let i = 0; i < listOfRLTeams.length; i++) {
    listOfRLTeams[i] = listOfRLTeams[i].split(":");
  }

  //shows first two teams
  eLeft.innerHTML = listOfRLTeams[teamIndex][0];
  document.getElementById('left-winnings').innerHTML = listOfRLTeams[teamIndex++][1];
  eRight.innerHTML = listOfRLTeams[teamIndex][0];
}

function button_clicked(choice) {
  //choice = 0 if higher, choice = 1 if lower
  leftPrice = parseInt(listOfRLTeams[teamIndex-1][1].replace(/\$|,/g, ''));
  rightPrice = parseInt(listOfRLTeams[teamIndex][1].replace(/\$|,/g, ''));
  if ((choice == 0 && (leftPrice < rightPrice)) || (choice == 1 && (leftPrice > rightPrice))) {
    eLeft.innerHTML = eRight.innerHTML;
    document.getElementById('left-winnings').innerHTML = listOfRLTeams[teamIndex++][1];
    eRight.innerHTML = listOfRLTeams[teamIndex][0];
    document.getElementById('score').innerHTML = "Score: " + ++score;
  } else {
    loser();
  }
}

function loser() {
  document.getElementsByClassName("higher")[0].remove();
  document.getElementsByClassName("lower")[0].remove();

  para = document.createElement("p");
  para.classList.add("winnings");
  para.innerHTML = listOfRLTeams[teamIndex][1];
  document.getElementById("right-div").appendChild(para);

  para2 = document.createElement("p");
  para2.classList.add("winnings", "loser");
  para2.innerHTML = "You Lost!";
  document.getElementById("right-div").appendChild(para2);

  if (localStorage.getItem("highScore") < score) {
    localStorage.setItem("highScore", score);
  }
}