$(window).load(function() {

    var sponsorscroller = $('.sponsorks').length * $('.sponsorks').outerWidth(true) * 2;
    
    $('.sponsorinner').width(sponsorscroller);

    var clone = $('.sponsorks').clone();

    $('.sponsorinner').append(clone);

    function animate() {

        $('.sponsorinner').css('left', 0);
        $('.sponsorinner').animate({'left': -sponsorscroller / 2}, 25000, 'linear', animate);

    }

    var checkResponsiveSlider = function() {
        console.log('checkResponsiveSlider', $(window).width());

        var sponsorscrollerresponsive = $('.sponsorinner').css({'max-width': '660px'});

        if ($(window).width() < 660) {
            $('.sponsorinner').stop(true, false).animate({ left: 0 });
            $('.sponsorinner').css({'max-width': sponsorscrollerresponsive});
            $('.sponsorinner').css({'width':'100%'})
            clone.hide();
        } else if ($(window).width() > 660) {
            $('.sponsorinner').css({'max-width': 'none'});
            $('.sponsorinner').width(sponsorscroller);
            $('.sponsorinner').animate({'left': -sponsorscroller / 2}, 25000, 'linear', animate);
            clone.show();
        }
    };

    $(window).resize(checkResponsiveSlider);

    animate();
    checkResponsiveSlider();

});