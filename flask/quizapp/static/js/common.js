window.onload = function() {
    var changeColor = function() {
        var e = document.getElementById('test');
        e.style.color = 'red';
    }
    setTimeout(changeColor, 1000);
}
