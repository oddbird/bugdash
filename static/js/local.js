function showBugs() {
    $('.weektitle').click(function() {
        if ($('body').hasClass('weekview')) {
            $(this).parent().toggleClass('open').toggleClass('closed');
        };
    });

    $('.daytitle').click(function() {
        if ($('body').hasClass('dayview')) {
            $(this).parent().toggleClass('open').toggleClass('closed');
        };
    });

    $('.overduetitle').click(function() {
        $(this).parent().toggleClass('open').toggleClass('closed');
    });
}

function bugToggle() {
    $('.bugtoggle').click(function() {
        $(this).toggleClass('open');
        if ($(this).hasClass('open')) {
            $('.weekview .week, .dayview .day, .overdue').addClass('open').removeClass('closed');
            $(this).text('« hide bugs');
        } else {
            $('.weekview .week, .dayview .day, .overdue').removeClass('open').addClass('closed');
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
        return false;
    });
    $('.showday').click(function() {
        $(this).addClass('active');
        $('.showweek').removeClass('active');
        $('body').removeClass('weekview').addClass('dayview');
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
