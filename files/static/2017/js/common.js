$(function () {

    //SVG Fallback
    if (!Modernizr.svg) {
        $("img[src*='svg']").attr("src", function () {
            return $(this).attr("src").replace(".svg", ".png");
        });
    }
    ;


    $("img, a").on("dragstart", function (event) {
        event.preventDefault();
    });

});

$(window).load(function () {

    $(".loader_inner").fadeOut();
    $(".loader").delay(400).fadeOut("slow");

});

function scrollingTo(elem) {
    $('html, body').animate({
        scrollTop: $(elem).offset().top
    }, 1000);
    return false
}

$(document).ready(function () {

    $('.toggle_menu').click(function () {
        $(this).toggleClass('on');
        $('.top_menu').slideToggle();
    });


    $(window).scroll(function () {
        if ($(this).scrollTop() > 600) {
            $('#scroller').fadeIn();
        } else {
            $('#scroller').fadeOut();
        }
    });
    $('#scroller').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 400);
        return false;
    });

    scrollByHrefAnchor();

});


function scrollByHrefAnchor() {
    if (window.location.hash.length > 0 && $(window.location.hash).length > 0) {
        $('html,body').animate({
            scrollTop: $(window.location.hash).offset().top
        });
    }

}

