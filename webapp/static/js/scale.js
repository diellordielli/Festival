$(document).ready(function() {
    var maxWidth = parseInt($('.page').css('max-width'), 10),
        moodHigh = $('.mood img').height(),
        newsPush = parseInt($('#news').css('top'), 10);

    resize();

    $(window).resize(function() {
        resize();
    });

    function resize() {
        var currentWidth = $('.page').width(),
            currentMoodTop = parseInt($('.mood').css('top')),
            scaleHight = newsPush - currentMoodTop,
            scale = currentWidth / maxWidth,
            newPush = 256 - (moodHigh - moodHigh * scale);

        $(".mood").css({ scale: scale });
        $('#news').css({ top: newPush, marginBottom: newPush });
    }
});