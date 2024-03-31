function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}


document.addEventListener('DOMContentLoaded', function() {

  const imageForm = document.getElementById('imageForm');
  const imgInput = document.getElementById('photo1');


  imageForm.addEventListener('submit', function(event) {
      event.preventDefault();


      if (imgInput.files.length === 0) {
          alert("Please select an image to upload.");
          return;
      }

      const originalImageUrl = URL.createObjectURL(imgInput.files[0]);
      document.getElementById('originalImage').src = originalImageUrl;

      const formData = new FormData();
      formData.append('file', imgInput.files[0]);

      // Replace 'API_ENDPOINT' with the actual endpoint
      fetch('https://16.170.249.188:80/p', { 
          method: 'POST',
          body: formData
          // mode: 'no-cors'
      })
      .then(response => {
          if (!response.ok) {
              throw new Error('Error: Server is down');
          }
          return response.blob();
      })
      .then(colorizedImage => {
          const colorizedImageUrl = URL.createObjectURL(colorizedImage);
          document.getElementById('colorizedImage').src = colorizedImageUrl;

      })
      .catch(error => {
          console.error('Error:', error);
          alert('There is an error processing your image.');
      });
  });

});

