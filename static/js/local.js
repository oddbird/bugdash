function showBugs() {
    $('.weekview .weektitle').click(function() {
        $(this).parent().toggleClass('open').toggleClass('closed');
    });

    $('.dayview .daytitle').click(function() {
        $(this).parent().toggleClass('open').toggleClass('closed');
    });
}

function bugToggle() {
    $('.bugtoggle').click(function() {
        $(this).toggleClass('open');
        if ($(this).hasClass('open')) {
            $('.weekview .week, .dayview .day').addClass('open').removeClass('closed');
            $(this).text('« hide bugs');
        } else {
            $('.weekview .week, .dayview .day').removeClass('open').addClass('closed');
            $(this).text('show bugs »');
        }
        return false;
    });
}

function viewToggle() {
    $('.showweek').click(function() {
        $(this).addClass('active');
        $('.showday').removeClass('active');
        $('body').removeClass('dayview').addClass('weekview');
        showBugs();
        return false;
    });
    $('.showday').click(function() {
        $(this).addClass('active');
        $('.showweek').removeClass('active');
        $('body').removeClass('weekview').addClass('dayview');
        showBugs();
        return false;
    });
}

$(function() {
    $('#hcard-client-name .email').defuscate();
    $('input[placeholder], textarea[placeholder]').placeholder();
    $('.details:not(html)').html5accordion('.summary');
    $('#messages').messages({handleAjax: true});
    showBugs();
    bugToggle();
    viewToggle();
});
