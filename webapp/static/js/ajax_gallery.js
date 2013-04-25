$(document).ready(function(){
    $(".gallery a").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href');

        $.get(url, function(data){
            var galleryContent = $('#ajaxgallery');
           
            galleryContent.html(data).hide().slideDown(300);

            target = $('#ajaxgallery');
            scroll_to_target(target);

            $('.galleryclose').on('click', function(event){
                galleryContent.slideUp(300);
            });
        });

        function scroll_to_target(target){
           $('html,body').animate({
                 scrollTop: target.offset().top - 150
            }, 1000);
        }
    });

    $(".fancybox").fancybox();

});