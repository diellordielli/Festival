$(document).ready(function(){
    $(".bandsingle a").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href');

        $.get(url, function(data){
            var closestAjax = $this.closest('.bandsingle').nextAll('#ajaxbands').first();
           
            closestAjax.html(data).slideDown(300);

            target = $('#bandsingleimg');
            scroll_to_target(target);

            $('.bandclose').on('click', function(event){
                closestAjax.slideUp(300);
            });
        });

        function scroll_to_target(target){
           $('html,body').animate({
                 scrollTop: target.offset().top - 160
            }, 1000);
        }
    });
});