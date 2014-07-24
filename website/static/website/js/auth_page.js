$(window).resize(function(){
    if ($(window).height() <= 600) {
        $('.auth-div').css({
            position:'relative',
            top: 'auto', 
            left: ($(window).width() - $('.auth-div').outerWidth())/2
        });
    } else {
        $('.auth-div').css({
            position:'absolute',
            top: ($(window).height() - $('.auth-div').outerHeight())/2,
            left: ($(window).width() - $('.auth-div').outerWidth())/2
        });
    }
});

//To initially run the function:
$(window).resize();
$(window).resize();

$('input').addClass('form-control');
$('label').addClass('col-sm-4 control-label');
