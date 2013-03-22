$(document).ready(function() {
    var initSize = $('body').css("font-size"),
        mapAspectRatio = 0.45;

    console.log(initSize);

    resize();

    $(window).resize(function() {
        resize();
    });

    function resize() {
        var width = $(window).width(),
            $map = $('.map');


        if (width) {       
            var fontSize = (width / 25) + 'px';
            $map.height($map.width() * mapAspectRatio);
            $('body').css("font-size", fontSize);
            $('.moodtitle').css("font-size", fontSize);
            $('.newstitle').css("font-size", fontSize);

        } else {
            $('body').css("font-size", initSize);
            $('.moodtitle').css("font-size", initSize);
            $('.newstitle').css("font-size", initSize);
        }
    }
});