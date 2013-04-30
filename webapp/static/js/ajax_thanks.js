$(document).ready(function(){
    $('form').on('submit', function(event){
        event.preventDefault();

        var $this = $(this),
            url = $(this).attr('action');

        $this.slideUp(100);

        $.post(url, $this.serialize(), function(data){     
            $this.html(data).slideDown(300);
        });
    });
});