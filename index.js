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
      fetch('http://13.60.20.242:8000/docs', { 
          method: 'POST',
          body: formData
      })
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok');
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

function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}
