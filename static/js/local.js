function showbugs() {
    $('.weekview .weektitle').click(function() {
        $(this).parent().toggleClass('open').toggleClass('closed');
    });

    $('.bugtoggle').click(function() {
        $(this).toggleClass('open');
        if ($(this).hasClass('open')) {
          $('.weekview .week, .dayview .day').addClass('open').removeClass('closed');
        } else {
          $('.weekview .week, .dayview .day').removeClass('open').addClass('closed');
        }
        return false;
    });
}

$(function() {
    $('#hcard-client-name .email').defuscate();
    $('input[placeholder], textarea[placeholder]').placeholder();
    $('.details:not(html)').html5accordion('.summary');
    $('#messages').messages({handleAjax: true});
    showbugs();
});
