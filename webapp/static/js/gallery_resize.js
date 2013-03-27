$(document).ready(function() {

    var imageRatio = 0.67,
        imageRatioh = 0.435;

    resize();

    $(window).resize(function() {
        resize();
    });

    function resize() {
        var containerWidth = $('.regiongreyg').width(),
            imageWidth = containerWidth * imageRatio,
            containerHeight = (imageWidth * imageRatioh) + 230; 

        $('.gallery img').width(imageWidth),
        $('.regiongreyg').height(containerHeight),
        $('.greybackground2').height(containerHeight - 152),
        $('.greybackground3').height(containerHeight - 152);

    }

});