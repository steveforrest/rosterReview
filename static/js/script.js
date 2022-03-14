document.addEventListener("DOMContentLoaded", changeBackgroundImage());


function changeBackgroundImage() {
    // document.getElementById("background").style.backgroundImage = "url('static/img/index.jpeg')";
    if (window.location.href == ' ') {
        document.getElementById("background").style.backgroundImage = "url('static/img/index.jpeg')";
    }
}

setTimeout(function () {
    msg.style.display = "none";
}, 3000);

displayAlert(function () {
    let msg = document.getElemetById("msg");
    print("msg");
    // let messages = document.getElementsByClassName("message-box");
    msg.style.display = 'flex';
    // setTimeout();

})