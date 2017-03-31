$(document).ready(function () {
    $('.main_slider').slick({
        arrows: false,
        dots: true,
        fade: true,
        speed: 1000,
        cssEase: 'linear',
        autoplay: true

    });

    $('.video1_slider').slick({
        arrows: true,
        dots: true,
        fade: true,
        speed: 1000,
        cssEase: 'linear',
        autoplay: true

    });


    $('.photo_slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        fade: true,
        autoplay: true,
        asNavFor: '.slider-nav'
    });
    $('.slider-nav').slick({
        slidesToShow: 10,
        slidesToScroll: 1,
        asNavFor: '.photo-slider',
        dots: true,
        centerMode: true,
        focusOnSelect: true
    });
});