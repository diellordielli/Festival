$(document).ready(function() {

    resize();

    $(window).resize(function() {
        resize();
    });

    function resize() {
        var navleftpos = $('.greybackground2').outerHeight(),
            navrightpos = $('.greybackground3').outerHeight(); 

        var margintop = (navleftpos - $('#navlefticon').height()) / 2;
        $('#navlefticon').css('top', margintop + 'px');

        var margintop = (navrightpos - $('#navrighticon').height()) / 2;
        $('#navrighticon').css('top', margintop + 'px');
    }
});