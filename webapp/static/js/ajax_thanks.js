$(document).ready(function(){
    $(".submit").click(function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('href');

        $.get(url, function(data){
            var thanks = $('#ajaxthanks');
           
            thanks.html(data).hide().slideDown(300);
        });
    });
});