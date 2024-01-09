const txt1 = document.getElementById('discription');
const btn1 = document.getElementById('button1');
const out1 = document.getElementById('output1');

// 1. to submit image discription on button1 click
function func1(event){
  event.preventDefault();
  out1.innerHTML = txt1.value;
}
btn1.addEventListener('click',func1);

// 2. to upload image to s3 butcket


//3. Display the image

const imgInput = document.querySelector("#photo1");
var uploaded_img = " ";

imgInput.addEventListener("change",function(){
  const reader = new FileReader();
  reader.addEventListener("load", ()=>{
    uploaded_img = reader.result;
    document.querySelector("#row1").style.backgroundImage = "url("+uploaded_img+")";
  });
  reader.readAsDataURL(this.files[0]);
})

function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}