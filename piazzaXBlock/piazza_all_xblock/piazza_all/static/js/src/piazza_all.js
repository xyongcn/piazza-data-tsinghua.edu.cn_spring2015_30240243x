/* Javascript for PiazzaFeedXBlock. */
function PiazzaAllXBlock(runtime, element) {

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

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
