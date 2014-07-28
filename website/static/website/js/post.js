$(window).resize(function() {
    if ($(window).width() <= 766) {
        $('.content-panel').css('max-width', '425px');
    } else {
        $('.content-panel').css('max-width', '520px');
    }
    if ($(window).width() <= 450) {
        $('.content-panel').css('max-width', '340px');
        $('.radio-btn').removeClass('btn-lg');
    } else {
        $('.radio-btn').addClass('btn-lg');
    }
});
    
//To initially run the function:
$(window).resize();
$(window).resize();

