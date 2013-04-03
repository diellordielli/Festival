(function(window, $){
    $(window).load(resize);
    $(window).resize(resize);

    function resize() {
        var navleftpos = $('.greybackground2').outerHeight(),
            navrightpos = $('.greybackground3').outerHeight(),
            navleftpos2 = $('.greybackground4').outerHeight(),
            navrightpos2 = $('.greybackground5').outerHeight();

        var margintop = (navleftpos - $('#navlefticon').height()) / 2;
        $('#navlefticon').css('top', margintop + 'px');

        var margintop = (navrightpos - $('#navrighticon').height()) / 2;
        $('#navrighticon').css('top', margintop + 'px');

        var mtop = (navleftpos2 - $('#navlefticon2').height()) / 2;
        $('#navlefticon2').css('top', mtop + 'px');

        var mtop = (navrightpos2 - $('#navrighticon2').height()) / 2;
        $('#navrighticon2').css('top', mtop + 'px');
    }
})(window, jQuery);
