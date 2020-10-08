var object1=$('#object1');
var object2=$('#object2');
var object3=$('#object3');
var sunil=$('#sunil');

sunil.mousemove(function(e){
   var valueX=(e.pageX * -1 / 12);
   var valueY=(e.pageY * -1 / 12);

    object1.css({
        'transform':'translate3d('+valueX+'px,'+valueY+'px,0) rotate(20deg)'
    });
});

sunil.mousemove(function(e){
   var valueX=(e.pageX * -1 / 15);
   var valueY=(e.pageY * -1 / 20);

    object2.css({
        'transform':'translate3d('+valueX+'px,'+valueY+'px,0)'
    });
});

sunil.mousemove(function(e){
   var valueX=(e.pageX * -1 / 15);
   var valueY=(e.pageY * -1 / 15);

    object3.css({
        'transform':'translate3d('+valueX+'px,'+valueY+'px,0) rotate(-20deg)'
    });
});
sunil.mousemove(function(e){
   var valueX=(e.pageX * -1 / 12);
   var valueY=(e.pageY * -1 / 12);

    samyakfont.css({
        'transform':'translate3d('+valueX+'px,'+valueY+'px,0) rotate(0deg)'
    });
});
