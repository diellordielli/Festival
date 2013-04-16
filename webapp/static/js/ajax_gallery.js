$(document).ready(function(){
    $(".gallery img").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href');

        $.get(url, function(data){
            var closestAjax = $this.closest('.bandsingle').nextAll('.ajaxgallery').first();
           
            closestAjax.append(data).hide().slideDown(300);
        });
    });
});