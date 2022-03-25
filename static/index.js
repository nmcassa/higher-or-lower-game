eLeft = document.getElementById('left');
eRight = document.getElementById('right');
eLeftW = document.getElementById('left-winnings');
listOfRLTeams = [];
teamIndex = 0;

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
  eLeftW.innerHTML = listOfRLTeams[teamIndex++][1];
  eRight.innerHTML = listOfRLTeams[teamIndex][0];
}

function button_clicked(choice) {
  //choice = 0 if higher, choice = 1 if lower
  eLeft.innerHTML = eRight.innerHTML;
  eLeftW.innerHTML = listOfRLTeams[teamIndex++][1];
  eRight.innerHTML = listOfRLTeams[teamIndex][0];
}