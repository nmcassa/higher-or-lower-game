eLeft = document.getElementById('left');
eRight = document.getElementById('right');

fetch('/test')
      .then(function (response) {
          return response.json();
      }).then(function (text) {
          console.log('GET response:');
          console.log(text.left); 
          console.log(text.right);
          eLeft.innerHTML = text.left;
          eRight.innerHTML = text.right;
      });