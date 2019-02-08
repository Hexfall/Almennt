var num1 = Math.floor(Math.random()*10) + 1;
var num2 = Math.floor(Math.random()*10) + 1;
var oper = Math.floor(Math.random()*3);
if (Math.max(num1, num2) != num1) {
    var temp = num1
    num1 = num2
    num2 = temp
}
if (oper == 0) {
    var operStr = '+';
    var result = num1 + num2;
} else if (oper == 1) {
    var operStr = '-';
    var result = num1 - num2;
} else {
    var operStr = '*';
    var result = num1 * num2;
}
Main();

function evaluateResult() {
    document.getElementById('resultMsg').style = 'Display: block';
    if (result == document.getElementById('mathIn').value) {
        document.getElementById('resultMsg').innerHTML = 'Correct';
        document.getElementById('resultMsg').classList = 'alert alert-success';
    }
    else {
        document.getElementById('resultMsg').innerHTML = 'Incorrect';
        document.getElementById('resultMsg').classList = 'alert alert-danger';
    }
}

function printLoop() {
    document.getElementById('loopOutput').innerHTML = '';
    var i = 1;
    var interval = setInterval(() => {
        if (i < document.getElementById('loopNumber').value) {
            document.getElementById('loopOutput').innerHTML += i + '<br />';
            i++;
        } else {
            document.getElementById('loopOutput').innerHTML += document.getElementById('loopNumber').value;
            clearInterval(interval);
        }
    }, 10);
}

function Main() {
    document.getElementById('taskMsg').innerHTML = "Calculate " + num1 + " " + operStr + " " + num2;
}