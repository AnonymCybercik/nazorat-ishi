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
        if ( msLeft < 10 ) {
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

countdown( "ten-countdown", 20, 0 );