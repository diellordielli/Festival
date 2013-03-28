var carouselOptions = {
    speed: 400
}

$(document).ready(function() {

    var totalNews = $(".newsscroller > .newsonly").length,
        newsWidth = $(".newsscroller > .newsonly:first").outerWidth(true),
        visibleNews = Math.floor($(".newsbg").width() / newsWidth),
        separators = Math.floor(totalNews / visibleNews), 
        totalWidth = (newsWidth * totalNews) + (separators * 50),
        visibleWidth = (visibleNews * newsWidth) + 50,
        $dot = $('.dot'),
        newsDots = Math.ceil(totalNews/visibleNews);

    for (var i = 1; i < newsDots; i++){
        $dot.clone().data('dotindex', i).appendTo('.slider-dots'); 
    }

    $(window).on('resize', function(event) {
        console.log(this, event, $(".newsbg").width());
    });

    $dot.addClass('active');

    $(".newsscroller").width(totalWidth);

    $('.greybackground5').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.newsscroller').get(0).offsetLeft - visibleWidth;

        if (newLeft <= -totalWidth) {
            newLeft = 0;
        }
        var navpos = -newLeft / visibleWidth;

        $('.dot').removeClass('active');
        $('.dot:eq('+navpos+')').addClass('active');

        $('.newsscroller').animate({'left': newLeft}, carouselOptions.speed);
    });

    $('.greybackground4').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.newsscroller').get(0).offsetLeft + visibleWidth;

        if (newLeft > 0) {
            newLeft = -separators * visibleWidth;
        }
        var navpos = -newLeft / visibleWidth;

        $('.dot').removeClass('active');
        $('.dot:eq('+navpos+')').addClass('active');

        $('.newsscroller').animate({'left': newLeft}, carouselOptions.speed);
    });


    $('.dot').on('click', function(event) {
        var dotindex = $(this).data('dotindex');
        var dotplace = dotindex * visibleWidth;
        var newLeft = -dotplace;
        $('.newsscroller').animate({'left': newLeft}, carouselOptions.speed);
        $('.dot').removeClass('active');
        $(this).addClass('active');
    });

    $('.newsall').on('mouseenter', function(event) {
        $('#navlefticon2').show();
        $('#navrighticon2').show();
        $('.greybackground4').css({'opacity': '0.6'});
        $('.greybackground5').css({'opacity': '0.6'});
    });

    $('.newsall').on('mouseleave', function(event) {
        $('#navlefticon2').hide();
        $('#navrighticon2').hide();
        $('.greybackground4').css({'opacity': '1'});
        $('.greybackground5').css({'opacity': '1'});
    });
});