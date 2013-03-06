$(document).ready(function() {
    $('#navrighticon').on('click', function(event) {
        event.preventDefault();
        $('.scroller').animate({'margin-left': '-=740px'}, 400);
    });
    $('#navlefticon').on('click', function(event) {
        event.preventDefault();
        $('.scroller').animate({'margin-left': '+=740px'}, 400);
    });
});
