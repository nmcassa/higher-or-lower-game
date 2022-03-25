eLeft = document.getElementById('left');
eRight = document.getElementById('right');
listOfRLTeams = [];

fetch('/test')
      .then(function (response) {
          return response.json();
      }).then(function (text) {
          console.log('GET response:');
          console.log(text.message);
          listOfRLTeams = text.message;
          eLeft.innerHTML = listOfRLTeams[0];
          eRight.innerHTML = text.message[1];
      });
