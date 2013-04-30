$(document).ready(function(){
    $(".bandsingle a").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href');

        $.get(url, function(data){
            var closestAjax = $this.closest('.bandsingle').nextAll('#ajaxbands').first();
           
            closestAjax.hide().html(data).slideDown(300);

            target = $(closestAjax);
            scroll_to_target(target);

            $('.bandclose').on('click', function(event){
                closestAjax.slideUp(300).html("");

                target = $('#bands');
                scroll_to_target(target);

            });
        });

        function scroll_to_target(target){
           $('html,body').delay('300').animate({
                 scrollTop: target.offset().top - 170
            }, 1000);
        }
    });
});