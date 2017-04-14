$(document).ready(function () {
    var radioButtons = $('.dropdown-menu');

    function resetAllRadioButtons() {
        $(radioButtons).each(function (i, obj) {
            var li = $('li', $(obj));
            $(li).attr('data-value', false);
        });

    }

    $('.language_list').on('click', function () {
        resetAllRadioButtons();
        $(this).attr('data-value', true);
        var imgsrc = $('img', this).attr('src');
        $('.language_select img').attr('src', imgsrc);
    });
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
    if ($(window).width() > 768) {
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
    var blockHeight=$('.bio_concepts').height();
    $('.bio_concepts_after').height(blockHeight)
});
$(window).resize(function () {
    var blockHeight=$('.bio_concepts').height();
    $('.bio_concepts_after').height(blockHeight)
})