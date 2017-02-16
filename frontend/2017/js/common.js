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


    var owl = $('.feedback');
    owl.owlCarousel({
        items: 1,
        center: true,
        loop: true,
        autoplay: true,
        autoplayTimeout: 15000,
        autoplayHoverPause: true
    });

    $('section.feedbacks .chevrone.right').click(function () {
        owl.trigger('next.owl.carousel');
    });
    $('section.feedbacks .chevrone.left').click(function () {
        owl.trigger('prev.owl.carousel');
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
    
});





