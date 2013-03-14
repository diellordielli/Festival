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

    $(window).on('resize', function(event) {
        console.log(this, event, $(".container").width());
    });

    $dot.addClass('active');

    $(".scroller").width(totalWidth);

    $('.greybackground3').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.scroller').get(0).offsetLeft - visibleWidth;

        if (newLeft <= -totalWidth) {
            newLeft = 0;
        }
        var navpos = -newLeft / visibleWidth;

        $('.dot').removeClass('active');
        $('.dot:eq('+navpos+')').addClass('active');

        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
    });

    $('.greybackground2').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.scroller').get(0).offsetLeft + visibleWidth;

        if (newLeft > 0) {
            newLeft = -separators * visibleWidth;
        }
        var navpos = -newLeft / visibleWidth;

        $('.dot').removeClass('active');
        $('.dot:eq('+navpos+')').addClass('active');

        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
    });


    $('.dot').on('click', function(event) {
        var dotindex = $(this).data('dotindex');
        var dotplace = dotindex * visibleWidth;
        var newLeft = -dotplace;
        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
        $('.dot').removeClass('active');
        $(this).addClass('active');
    });

    $('.galleryall').on('mouseenter', function(event) {
        $('#navlefticon').show();
        $('#navrighticon').show();
        $('.greybackground2').css({'opacity': '0.6'});
        $('.greybackground3').css({'opacity': '0.6'});
    });
    $('.galleryall').on('mouseleave', function(event) {
        $('#navlefticon').hide();
        $('#navrighticon').hide();
        $('.greybackground2').css({'opacity': '1'});
        $('.greybackground3').css({'opacity': '1'});
    });

    $('.helfercircle').on('click', function(event) {
        $('.mail1').fadeIn("slow");
    });

    $('.goennercircle').on('click', function(event) {
        $('.mail2').fadeIn("slow");
    });

    $('.pressecircle').on('click', function(event) {
        $('.mail3').fadeIn("slow");
    });

    $('.sponsoringcircle').on('click', function(event) {
        $('.mail4').fadeIn("slow");
    });

    $('.mailclose').on('click', function(event) {
        $('.mail1').fadeOut("slow");
    });
    $('.mailclose').on('click', function(event) {
        $('.mail2').fadeOut("slow");
    });
    $('.mailclose').on('click', function(event) {
        $('.mail3').fadeOut("slow");
    });
    $('.mailclose').on('click', function(event) {
        $('.mail4').fadeOut("slow");
    });



    $('.newstitle').on('click', function(event) {
        $('.newsshow').fadeIn("slow");
    });

    $('.newstitle').on('click', function(event) {
        $('.newsshow').fadeOut("slow");
    });

});