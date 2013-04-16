$(document).ready(function(){
    $(".bandsingle a").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href');

        $.get(url, function(data){
            var closestAjax = $this.closest('.bandsingle').nextAll('.ajaxbands').first();
           
            closestAjax.html(data).hide().slideDown(300);

            $('.bandclose').on('click', function(event){
                closestAjax.slideUp(300);
            });
        });
    });
});