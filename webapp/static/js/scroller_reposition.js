$(document).ready(function() {

    resize();

    $(window).resize(function() {
        resize();
    });

    function resize() {
        var regionGrey = $('.regiongreyg').width(),
            galleryImg = $('.gallery img').width();

        var marginleft = (regionGrey - galleryImg) / 2;
        $('.gallery').css('margin-left', marginleft + 'px');

        var marginright = (regionGrey - galleryImg) / 2;
        $('.gallery').css('margin-right', marginright + 'px');
    }
});