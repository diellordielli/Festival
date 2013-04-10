$(document).ready(function() {
    var initSize = $('body').css("font-size"),
        mapAspectRatio = 0.45;

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

        } else {
            $('body').css("font-size", initSize);
        }
    }
});