$(window).load(function() {

    var sponsorscroller = $('.sponsorks').length * $('.sponsorks').outerWidth(true) * 2;

    $('.sponsorinner').width(sponsorscroller);

    var clone = $('.sponsorks').clone();

    $('.sponsorinner').append(clone);

    function animate() {
        $('.sponsorinner').css('left', 0);
        $('.sponsorinner').animate({'left': -sponsorscroller / 2}, 10000, 'linear', animate);

    }

    animate();

});