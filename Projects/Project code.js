effect = document.getElementById("effect").innerHTML;

effect.addEventListener("mouseover", mouseOver );
effect.addEventListener("mousedown", mouseDown);
effect.addEventListener("mouseup", mouseUp);

function mouseOver() {
    effect.style.backgroundColor = 'grey';
}
function mouseDown() {
    effect.style.backgroundColor = 'green';
}
function mouseUp() {
    effect.style.backgroundColor = 'blue';
}
