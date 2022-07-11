var counter;
var n = 0;

var addBtn = document.getElementById("add-btn");
var subBtn = document.getElementById("sub-btn");
var resBtn = document.getElementById("res-btn");
counter = document.getElementById("number");


addBtn.addEventListener("click", add);
subBtn.addEventListener("click", sub);
resBtn.addEventListener("click", res);


counter.innerHTML = n;

function add(){
    n += 1;
    console.log(n);
    counter.innerHTML = n;
}
function sub() {
    n -= 1;
    console.log(n);
    counter.innerHTML = n;
}
function res() {
    n = 0;
    console.log(n);
    counter.innerHTML = n;
}