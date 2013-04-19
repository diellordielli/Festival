$(document).ready(function(){
    $(".gallery a").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href');

        $.get(url, function(data){
            var galleryContent = $('.ajaxgallery');
           
            galleryContent.html(data).hide().slideDown(300);

            $('.bandclose').on('click', function(event){
                galleryContent.slideUp(300);
            });
        });
    });

    $(".fancybox").fancybox();

});