setInterval(function() {
	var donghua = document.querySelector(".huadong");
	var sel = document.querySelector("#sel");
	if(sel.nextElementSibling != null) {
		sel.id = "";

		sel.nextElementSibling.id = "sel";
		var tup = sel.nextElementSibling.getAttribute("data");
		console.log(tup)
		sel.parentNode.parentNode.parentNode.firstElementChild.style.left = tup + "px";
		console.log(sel.parentNode.parentNode.parentNode.firstElementChild)

	} else {
		sel.id = "";
		sel.parentNode.firstElementChild.id = "sel";
		var tup1 = sel.parentNode.firstElementChild.getAttribute("data");
		console.log(tup1)
		sel.parentNode.parentNode.parentNode.firstElementChild.style.left = tup1 + "px";
	}
}, 3000)

// 这是打印机效果
var s = 'I want to join your company';
var con = document.querySelector('.slider2');
var index = 0;
var length = s.length;
var tId = null;

function start() {
	con.innerText = "";

	tId = setInterval(function() {
		con.append(s.charAt(index));
		if(index++ === length) {
			clearInterval(tId);
			index = 0;
			start()
		}
	}, 100);
}

start();
