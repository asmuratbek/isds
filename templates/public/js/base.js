function ResizeHeight() {
    var height =$('.bio_concepts').height();
    $('.bio_concepts_after').height(height);
}
$(document).ready(function () {

    var social_hide_off = $('.isds_navigation').offset().top;
    var isSocialLinksShowen = false;

    function initSocialLinks() {
        if ($(document).scrollTop() >= social_hide_off) {
            $('.social_left').css({
                "left": "-60px"
            });
            isSocialLinksShowen = true;
        }
        else {
            $('.social_left').css({
                "left": "-80px"
            });
            isSocialLinksShowen = false;
        }
    }

    $(document).scroll(function () {
        initSocialLinks();
    });
    $(document).ready(function () {
        initSocialLinks();

        if (isSocialLinksShowen) {
            $('.social_left ul li').each(function (i, obj) {
                $(obj).hover(function () {
                    if ($(obj).attr('data-hover') === 'false') {
                        $(this).animate({
                            'margin-left': 60
                        }, 200);
                        $(obj).attr('data-hover', true);
                    }
                }, function () {
                    if ($(obj).attr('data-hover') === 'true') {
                        $(this).animate({
                            'margin-left': 0
                        }, 200);
                        $(obj).attr('data-hover', false);
                    }
                });
            });
        }
    });
    if ($(window).width() > 767) {
        $('.navbar-nav li.resources_link').hover(function () {
                $('.sub_menu').stop(true, true).delay(200).fadeIn(500).css({
                    "visible": "visible",
                    "height": "auto"
                }).animate(), 500;
            }
            ,
            function () {
                $('.sub_menu').stop(true, true).delay(200).fadeOut(500).css({
                    "visible": "hidden"
                }).animate(), 500;

            });
    }
    $('.share_button').on('click', function () {
        if ($('.ya-share2', this).hasClass('showen')) {
            $('.ya-share2', this).removeClass('showen');
        }
        else {
            $('.ya-share2', this).addClass('showen');
        }

    });
    ResizeHeight();


});
$(window).resize(function () {
    ResizeHeight();
})