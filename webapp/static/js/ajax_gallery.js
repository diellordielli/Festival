$(document).ready(function(){
    $(".gallery a").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href');

        $.get(url, function(data){
            var galleryContent = $('#ajaxgallery');
           
            galleryContent.html(data).hide().slideDown(300);

            target = $(galleryContent);
            scroll_to_target(target);

            $('.galleryclose').on('click', function(event){
                galleryContent.slideUp(300);

                target = $('#gallery');
                scroll_to_target(target);

            });

            $('.bandchoice').click(function(event){
                event.preventDefault();
                $('.categoryfestival').slideUp();
                $('.categorybands').slideDown();
                $('.bandchoice').css({'color': '#06ddb7'});
                $('.festivalchoice').css({'color': '#000'});
            });

            $('.festivalchoice').click(function(event){
                event.preventDefault();
                $('.categorybands').slideUp();
                $('.categoryfestival').slideDown();
                $('.festivalchoice').css({'color': '#06ddb7'});
                $('.bandchoice').css({'color': '#000'});
            });
        });

        function scroll_to_target(target){
            $('html,body').animate({
                 scrollTop: target.offset().top - 155
            }, 1000);
        }
    });

    $(".fancybox").fancybox();

});