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
        $dot.clone().appendTo('.slider-dots'); 
    }

    $(".scroller").width(totalWidth);

    $('#navrighticon').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.scroller').get(0).offsetLeft - visibleWidth;

        if (newLeft < -totalWidth) {
            newLeft = 0;
        }

        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
    });

    $('#navlefticon').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.scroller').get(0).offsetLeft + visibleWidth;

        if (newLeft > 0) {
            newLeft = -separators * visibleWidth;
        }

        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
    });

    $('.galleryall').on('mouseenter', function(event) {
        $('#navrighticon').css({'display': 'inline'});
        $('.greybackground3').css({'opacity': '0.5'});
    });
    $('.galleryall').on('mouseleave', function(event) {
        $('#navrighticon').css({'display': 'none'});
        $('.greybackground3').css({'opacity': '1'});
    });

    $('.galleryall').on('mouseenter', function(event) {
        $('#navlefticon').css({'display': 'inline'});
        $('.greybackground2').css({'opacity': '0.5'});
    });
    $('.galleryall').on('mouseleave', function(event) {
        $('#navlefticon').css({'display': 'none'});
        $('.greybackground2').css({'opacity': '1'});
    });
});