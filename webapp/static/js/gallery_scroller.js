var carouselOptions = {
    speed: 400,
    imageRatio: 0.67,
    imageRatioH: 0.435
}

$(document).ready(function() {
    // gets updated on resize and on page load
    var totalWidth, totalImages, stepWidth, navpos = 0,
        $dot = $('.dot');

    resize();

    $(window).resize(function() {
        resize();
    });

    function resize() {
        var containerWidth = $('.regiongreyg').width(),
            imageWidth = Math.round(containerWidth * carouselOptions.imageRatio),
            containerHeight = (imageWidth * carouselOptions.imageRatioH) + 230;

        $('.gallery img').width(imageWidth);
        $('.regiongreyg').height(containerHeight);
        $('.greybackground2').height(containerHeight - 152);
        $('.greybackground3').height(containerHeight - 152);

        var regionGrey = $('.regiongreyg').width(),
            galleryImg = $('.gallery img').width();

        var marginleft = (regionGrey - galleryImg) / 2;
        $('.gallery').css('margin-left', marginleft + 'px');

        var marginright = (regionGrey - galleryImg) / 2;
        $('.gallery').css('margin-right', marginright + 'px');

        // set superscope totalWidth
        stepWidth = $(".scroller > .gallery:first").outerWidth(true);
        totalImages = $(".scroller > .gallery").length;
        totalWidth = (stepWidth * totalImages);

        $(".scroller").width(totalWidth);

        $('.scroller').css('left', - navpos * stepWidth);
    }

    for (var i = 1; i < totalImages; i++){
        $dot.clone().data('dotindex', i).appendTo('.slider-dots'); 
    }

    $dot.addClass('active');
    

    $('.greybackground3').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.scroller').get(0).offsetLeft - stepWidth;

        if (newLeft <= -totalWidth) {
            newLeft = 0;
        }

        navpos = -newLeft / stepWidth;

        $('.dot').removeClass('active');
        $('.dot:eq('+navpos+')').addClass('active');

        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
    });

    $('.greybackground2').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.scroller').get(0).offsetLeft + stepWidth;

        if (newLeft > 0) {
            newLeft = -(totalImages -1) * stepWidth;
        }
        
        navpos = -newLeft / stepWidth;

        $('.dot').removeClass('active');
        $('.dot:eq('+navpos+')').addClass('active');

        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
    });


    $('.dot').on('click', function(event) {
        navpos = $(this).data('dotindex');
        var dotplace = navpos * stepWidth;
        var newLeft = -dotplace;
        $('.scroller').animate({'left': newLeft}, carouselOptions.speed);
        $('.dot').removeClass('active');
        $(this).addClass('active');
    });

    $('.regiongreyg').on('mouseenter', function(event) {
        $('#navlefticon').show();
        $('#navrighticon').show();
        $('.greybackground2').css({'background-color': '#e8e8e8'});
        $('.greybackground3').css({'background-color': '#e8e8e8'});
    });

    $('.regiongreyg').on('mouseleave', function(event) {
        $('#navlefticon').hide();
        $('#navrighticon').hide();
        $('.greybackground2').css({'background-color': '#dcdcdc'});
        $('.greybackground3').css({'background-color': '#dcdcdc'});
    });

});