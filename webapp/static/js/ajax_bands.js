$(document).ready(function(){
    $(".bandsingle a").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href');

        $.get(url, function(data){
            var closestAjax = $this.closest('.bandsingle').nextAll('.ajaxbands').first();
           
            scroll_to_target(closestAjax);

            closestAjax.hide().html(data).slideDown(1500);
            closestAjax.get(0).offsetHeight

            $('.bandclose').on('click', function(event){
                closestAjax.slideUp(300).html("");

                target = $('#bands');
                scroll_to_target(target);

            });
        });

        function scroll_to_target(target){
           $('html,body').delay('300').animate({
                 scrollTop: target.offset().top - 170
            }, 800);
        }
    });
});