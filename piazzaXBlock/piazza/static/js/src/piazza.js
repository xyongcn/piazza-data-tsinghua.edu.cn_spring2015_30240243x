/* Javascript for PiazzaXBlock. */
function PiazzaXBlock(runtime, element) {



}
function button_fullscreen() {
    var frame = document.getElementById("iframepage");
    if (frame.requestFullscreen) {
        frame.requestFullscreen();
    }
    else if (frame.mozRequestFullScreen) {
        frame.mozRequestFullScreen();
    }
    else if (frame.webkitRequestFullscreen) {
        frame.webkitRequestFullscreen();
    }
}