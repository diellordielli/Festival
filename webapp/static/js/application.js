var carouselOptions = {
    speed: 400
}

$(document).ready(function() {

    var totalImages = $(".scroller > .gallery").length,
        imageWidth = $(".scroller > .gallery:first").outerWidth(true),
        visibleImages = Math.floor($(".container").width() / imageWidth),
        separators = Math.floor(totalImages / visibleImages), 
        totalWidth = (imageWidth * totalImages) + (separators * 10),
        visibleWidth = (visibleImages * imageWidth) + 10,
        $dot = $('.dot'),
        imageDots = Math.ceil(totalImages/visibleImages);

    for (var i = 1; i < imageDots; i++){
        $dot.clone().data('dotindex', i).appendTo('.slider-dots'); 
    }

    $(window).on('resize', function(event) {
        //console.log(this, event, $(".container").width());
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
        $('#helfer-form').fadeIn("slow", function(){
            target = $('#helfer-form');
            scroll_to_target(target);
        });
    });

    $('.goennercircle').on('click', function(event) {
        $('#goenner-form').fadeIn("slow", function(){
            target = $('#goenner-form');
            scroll_to_target(target);
        });
    });

    $('.pressecircle').on('click', function(event) {
        $('#presse-form').fadeIn("slow", function(){
            target = $('#presse-form');
            scroll_to_target(target);
        });    });

    $('.sponsoringcircle').on('click', function(event) {
        $('#sponsoring-form').fadeIn("slow", function(){
            target = $('#sponsoring-form');
            scroll_to_target(target);
        });        
    });

    $('.mailclose').on('click', function(event) {
        $('#helfer-form').fadeOut("slow");
    });
    $('.mailclose').on('click', function(event) {
        $('#goenner-form').fadeOut("slow");
    });
    $('.mailclose').on('click', function(event) {
        $('#presse-form').fadeOut("slow");
    });
    $('.mailclose').on('click', function(event) {
        $('#sponsoring-form').fadeOut("slow");
    });

    $('#mehrinfos').on('click', function(event) {
        $('.newsshow').fadeIn("slow");
        $('#mehrinfos').css({'display': 'none'});
    });

    function scroll_to_target(target){
        $('html,body').animate({
                 scrollTop: target.offset().top - 210
            }, 1000);
    }
    
    $('.navtoggleup').on('click', function(event) {
        $('.navigation a').fadeIn("slow");
        $('.navtoggleup').hide();
        $('.navigation a').css({'display': 'block'});
    });

    $('.navtoggleup').on('click', function(event) {
        $('.navtoggledown').show();
    });


});