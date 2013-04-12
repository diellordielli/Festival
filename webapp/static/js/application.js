$(document).ready(function() {

    $('.bandclose img').on('click', function(event){
        $('.ajax').css({'display': 'none'});
    });

    $('.helfercircle').on('click', function(event) {
        $('#goenner-form').hide();
        $('#presse-form').hide();
        $('#sponsoring-form').hide();
        $('#helfer-form').fadeIn("slow", function(){
            target = $('#helfer-form');
            scroll_to_target(target);
        });
    });

    $('.goennercircle').on('click', function(event) {
        $('#helfer-form').hide();
        $('#presse-form').hide();
        $('#sponsoring-form').hide();
        $('#goenner-form').fadeIn("slow", function(){
            target = $('#goenner-form');
            scroll_to_target(target);
        });
    });

    $('.pressecircle').on('click', function(event) {
        $('#goenner-form').hide();
        $('#helfer-form').hide();
        $('#sponsoring-form').hide();
        $('#presse-form').fadeIn("slow", function(){
            target = $('#presse-form');
            scroll_to_target(target);
        });    
    });

    $('.sponsoringcircle').on('click', function(event) {
        $('#goenner-form').hide();
        $('#presse-form').hide();
        $('#helfer-form').hide();
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

    $('.mehrinfos').on('click', function(event) {
        var currentHeight,
            newsindex = $('.newsdot.active').data('newsdotindex'),
            $currentNews = $('.newsonly').eq(newsindex);

        $('.newsshow').show();
        currentHeight = $currentNews.height();
        $('.newsshow').hide();

        $('.newsshow').slideDown("slow", function() {
            $(window).trigger('resize');
            $('.newsscroller').animate({'height': currentHeight});
        });

        $('.mehrinfos').css({'display': 'none'});
        
        $('.greybackground5').on('click', function(event) {
            var currentHeight,
                newsindex = $('.newsdot.active').data('newsdotindex'),
                $currentNews = $('.newsonly').eq(newsindex);

            $('.newsshow').show();
            currentHeight = $currentNews.height();
            $('.newsshow').hide();

            $('.newsshow').slideDown("slow", function() {
                $(window).trigger('resize');
                $('.newsscroller').animate({'height': currentHeight});
            });


            $('.mehrinfos').css({'display': 'none'});
        });

        $('.greybackground4').on('click', function(event) {
            var currentHeight,
                newsindex = $('.newsdot.active').data('newsdotindex'),
                $currentNews = $('.newsonly').eq(newsindex);

            $('.newsshow').show();
            currentHeight = $currentNews.height();
            $('.newsshow').hide();

            $('.newsshow').slideDown("slow", function() {
                $(window).trigger('resize');
                $('.newsscroller').animate({'height': currentHeight});
            });


            $('.mehrinfos').css({'display': 'none'});
        });

        $('.newsdot').on('click', function(event) {
            var currentHeight,
                newsindex = $('.newsdot.active').data('newsdotindex'),
                $currentNews = $('.newsonly').eq(newsindex);

            $('.newsshow').show();
            currentHeight = $currentNews.height();
            $('.newsshow').hide();

            $('.newsshow').slideDown("slow", function() {
                $(window).trigger('resize');
                $('.newsscroller').animate({'height': currentHeight});
            });


            $('.mehrinfos').css({'display': 'none'});
        });
    });

    function scroll_to_target(target){
        $('html,body').animate({
                 scrollTop: target.offset().top - 210
            }, 1000);
    }

    $('.navtoggleup').on('click', function(event) {
        $('.navigation a').fadeOut(10);
        $('.navtoggleup').hide();
        $('.navtoggledown').show();
        $('.navigation a').css({'display': 'none'});
        $('.headerbg').css({'height':'94px'});
        $('.hrleftdown').css({'margin-top':'30px'});
    });

    $('.navtoggledown').on('click', function(event) {
        $('.navigation a').fadeIn(10);
        $('.navtoggleup').show();
        $('.navtoggledown').hide();
        $('.navigation a').css({'display': 'block'});
        $('.headerbg').css({'height':'175px'});
        $('.hrleftdown').css({'margin-top':'5px'});
    });

    $('.navigation a').on('click', function(event) {
        if ($(window).width() <= 357) {
           $('.navtoggleup').trigger('click');
        }
    });

    var checkResponsiveNav = function() {
        if ($(window).width() >= 357) {
            $('.headerbg').attr('style', '');
            $('.navigation a').attr('style', '');
            $('.navtoggleup').attr('style', '');
            $('.navtoggledown').attr('style', '');
            $('.hrleftdown').attr('style', '');
        } else if ($(window).width() < 357) {
            $('.navigation a').css({'display': 'block'});
            $('.navtoggleup').css({'display': 'inline'});
            $('.navtoggledown').css({'display': 'none'});
        }
    };

    $(window).resize(checkResponsiveNav);
    checkResponsiveNav();

});