var carouselOptions = {
    speed: 400,
    imageRatio: 0.67,
    imageRatioH: 0.435
}

$(document).ready(function() {
    // gets updated on resize and on page load
    var totalWidth, totalImages, stepWidth, navpos = 0,
        $newsdot = $('.newsdot');

    resize();

    $(window).resize(function() {
        resize();
    });

    function resize() {
        var regionGrey = $('.regiongrey').width(),
            newsWidth = Math.round(regionGrey * carouselOptions.imageRatio);
            hrnews = newsWidth + 0.7

        $('.hrnews').width(hrnews);
        $('.newsonly').width(newsWidth);

        var marginleft = (regionGrey - newsWidth) / 2;
        $('.newsonly').css('margin-left', marginleft + 'px');

        var marginright = (regionGrey - newsWidth) / 2;
        $('.newsonly').css('margin-right', marginright + 'px');

        // set superscope totalWidth
        stepWidth = $(".newsscroller > .newsonly:first").outerWidth(true);
        totalImages = $(".newsscroller > .newsonly").length;
        totalWidth = (stepWidth * totalImages);

        $(".newsscroller").width(totalWidth);

        $('.newsscroller').css('margin-left', - navpos * stepWidth);
    }

    for (var i = 1; i < totalImages; i++){
        $newsdot.clone().data('newsdotindex', i).appendTo('.slider-newsdots'); 
    }

    $newsdot.addClass('active');
    

    $('.greybackground5').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.newsscroller').get(0).offsetLeft - stepWidth;

        if (newLeft <= -totalWidth) {
            newLeft = 0;
        }

        navpos = -newLeft / stepWidth;

        $('.newsdot').removeClass('active');
        $('.newsdot:eq('+navpos+')').addClass('active');

        $('.newsscroller').animate({'margin-left': newLeft}, carouselOptions.speed);
    });

    $('.greybackground4').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.newsscroller').get(0).offsetLeft + stepWidth;

        if (newLeft > 0) {
            newLeft = -(totalImages -1) * stepWidth;
        }
        
        navpos = -newLeft / stepWidth;

        $('.newsdot').removeClass('active');
        $('.newsdot:eq('+navpos+')').addClass('active');

        $('.newsscroller').animate({'margin-left': newLeft}, carouselOptions.speed);
    });


    $('.newsdot').on('click', function(event) {
        navpos = $(this).data('newsdotindex');
        var dotplace = navpos * stepWidth;
        var newLeft = -dotplace;
        $('.newsscroller').animate({'margin-left': newLeft}, carouselOptions.speed);
        $('.newsdot').removeClass('active');
        $(this).addClass('active');
    });

    $('.regiongrey').on('mouseenter', function(event) {
        $('#navlefticon2').show();
        $('#navrighticon2').show();
        $('.greybackground4').css({'background-color': '#e8e8e8'});
        $('.greybackground5').css({'background-color': '#e8e8e8'});
    });

    $('.regiongrey').on('mouseleave', function(event) {
        $('#navlefticon2').hide();
        $('#navrighticon2').hide();
        $('.greybackground4').css({'background-color': '#dcdcdc'});
        $('.greybackground5').css({'background-color': '#dcdcdc'});
    });

});