var carouselOptions = {
    speed: 400
}

$(document).ready(function() {

    var totalImages = $(".scroller > .gallery").length,
        imageWidth = $(".scroller > .gallery:first").outerWidth(true),
        visibleImages = Math.floor($(".container").width() / imageWidth),
        separators = Math.floor(totalImages / visibleImages), 
        totalWidth = (imageWidth * totalImages) + (separators * 50),
        visibleWidth = (visibleImages * imageWidth) + 50,
        $dot = $('.dot'),
        imageDots = Math.ceil(totalImages/visibleImages);

    for (var i = 1; i < imageDots; i++){
        $dot.clone().data('dotindex', i).appendTo('.slider-dots'); 
    }

    $dot.addClass('active');

    $(".scroller").width(totalWidth);

    $('#navrighticon').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.scroller').get(0).offsetLeft - visibleWidth;
        console.log(newLeft, -totalWidth);
        if (newLeft <= -totalWidth) {
            newLeft = 0;
        }

        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
    });

    $('#navrighticon').on('click', function(event) {
        $('.dot').removeClass('active');
        $(this).addClass('active');
    });   

    $('#navlefticon').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.scroller').get(0).offsetLeft + visibleWidth;

        if (newLeft > 0) {
            newLeft = -separators * visibleWidth;
        }

        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
    });

    $('.dot').on('click', function(event) {
        var dotindex = $(this).data('dotindex');
        var dotplace = dotindex * visibleWidth;

        console.log(dotindex);

        var newLeft = -dotplace;
        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
        $('.dot').removeClass('active');
        $(this).addClass('active');

    });

    $('.galleryall').on('mouseenter', function(event) {
        $('#navlefticon').show();
        $('.greybackground2').css({'opacity': '0.6'});
    });
    $('.galleryall').on('mouseleave', function(event) {
        $('#navlefticon').hide();
        $('.greybackground2').css({'opacity': '1'});
    });

    $('.galleryall').on('mouseenter', function(event) {
        $('#navrighticon').show();
        $('.greybackground3').css({'opacity': '0.6'});
    });
    $('.galleryall').on('mouseleave', function(event) {
        $('#navrighticon').hide();
        $('.greybackground3').css({'opacity': '1'});
    });
});