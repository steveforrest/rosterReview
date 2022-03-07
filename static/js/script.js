document.addEventListener("DOMContentLoaded", changeBackgroundImage());


function changeBackgroundImage() {
    // document.getElementById("background").style.backgroundImage = "url('static/img/index.jpeg')";
    if ( window.location.href == ' ' ){ 
        document.getElementById("background").style.backgroundImage = "url('static/img/index.jpeg')";
     }
    }

