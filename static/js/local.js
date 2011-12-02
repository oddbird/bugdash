function showbugs() {
    $('.weekview .weektitle').click(function() {
        $(this).parent().toggleClass('open').toggleClass('closed');
    });
}

$(function() {
    $('#hcard-client-name .email').defuscate();
    $('input[placeholder], textarea[placeholder]').placeholder();
    $('.details:not(html)').html5accordion('.summary');
    $('#messages').messages({handleAjax: true});
    showbugs();
});
