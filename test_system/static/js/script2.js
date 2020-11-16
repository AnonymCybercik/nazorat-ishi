function countdown( elementName, minutes, seconds )
{
    var element, endTime, hours, mins, msLeft, time;

    
    

    function twoDigits( n )
    {
        return (n <= 9 ? "0" + n : n);
    }


    function updateTimer()
    {

        msLeft = endTime - (+new Date);
        if ( msLeft < 20 ) {
            var a = document.getElementById("click");
            a.click()
        } else {
            time = new Date( msLeft );
            hours = time.getUTCHours();
            mins = time.getUTCMinutes();
            element.innerHTML = (hours ? hours + ':' + twoDigits( mins ) : mins) + ':' + twoDigits( time.getUTCSeconds() );
            setTimeout( updateTimer, time.getUTCMilliseconds() + 500 );
        }
    }

    element = document.getElementById( elementName );
    endTime = (+new Date) + 10 * (60*minutes + seconds) + 500;
    updateTimer();
}

var ijtimoiy = ["ona tili","adabiyot","rus tili","ingliz tili","tarix","huquq"];
var aniq = ["algebra","kimyo","informatika","biologiya","fizika","geometriya"];

var name = document.getElementById("test").innerHTML;

for (var i in aniq){

    if (aniq[i]== name.toLowerCase()){

        var a = 6000;
        countdown( "ten-countdown", a, 0 );

    }

}

for (var i in ijtimoiy){

    if (ijtimoiy[i]==name.toLowerCase()){

        var a = 4000;
        countdown( "ten-countdown", a, 0 );

    }

}
