$(window).resize(function(){
  $('.auth-div').css({
    position:'absolute',
    top: ($(window).height() - $('.auth-div').outerHeight())/2,
    left: ($(window).width() - $('.auth-div').outerWidth())/2
  });
});

// To initially run the function:
$(window).resize();
$(window).resize();

$('input').addClass('form-control');
$('label').addClass('col-sm-4 control-label');