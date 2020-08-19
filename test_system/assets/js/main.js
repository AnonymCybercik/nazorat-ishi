const startingMinutes = 1;
let time = startingMinutes * 60;

var element = document.getElementById("time")

setInterval(update,1000)

let counter = true;

function update(){
	const minutes = Math.floor(time / 60)
	let seconds = time % 60;

	seconds = seconds < 10 ? '0' + seconds:seconds;

	element.innerHTML = `${minutes}:${seconds}`;

	if (minutes == '0' && seconds =='00'){
		counter = false;
	}
	if (counter == true){
		time--;
	}
	if (counter == false){
		
		var a = document.getElementById('btn')

		a.click()
	}
	
}


