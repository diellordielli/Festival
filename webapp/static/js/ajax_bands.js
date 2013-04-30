$(document).ready(function(){
    $(".bandsingle a").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href'),
            closestAjax = $this.closest('.bandsingle').nextAll('.ajaxbands').first();

        $.get(url, function(data){
            closestAjax.hide().html(data).slideDown(1500, function() {
                closestAjax.get(0).style.display='none';
                closestAjax.get(0).offsetHeight;
                closestAjax.get(0).style.display='block';
            });

            scroll_to_target(closestAjax);

            // force redraw hack: http://stackoverflow.com/questions/3485365/how-can-i-force-webkit-to-redraw-repaint-to-propagate-style-changes
            closestAjax.get(0).style.display='none';
            closestAjax.get(0).offsetHeight;
            closestAjax.get(0).style.display='block';

            $('.bandclose').on('click', function(event){
                closestAjax.slideUp(300);

                target = $('#bands');
                scroll_to_target(target);

            });
        });

        function scroll_to_target(target){
           $('body').delay('300').animate({
                 scrollTop: target.offset().top - 170
            }, 1000);
        }
    });
});