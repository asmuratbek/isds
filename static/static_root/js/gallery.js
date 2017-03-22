$(document).ready(function () {
    var Slider = (function () {
        var initSlider = function () {
            var dir = $("html").attr("dir");
            var swipeHandler = new Hammer(document.getElementById("slider"));
            swipeHandler.on('swipeleft', function (e) {
                if (dir == "rtl")
                    $(".arrow-left").trigger("click");
                else
                    $(".arrow-right").trigger("click");
            });

            swipeHandler.on('swiperight', function (e) {
                if (dir == "rtl")
                    $(".arrow-right").trigger("click");
                else
                    $(".arrow-left").trigger("click");
            });

            $(".arrow-right , .arrow-left").click(function (event) {
                var nextActiveSlide = $(".slide_item.active").next();

                if ($(this).hasClass("arrow-left"))
                    nextActiveSlide = $(".slide_item.active").prev();

                if (nextActiveSlide.length > 0) {
                    var nextActiveIndex = nextActiveSlide.index();
                    $(".dots span").removeClass("active");
                    $($(".dots").children()[nextActiveIndex]).addClass("active");

                    updateSlides(nextActiveSlide);
                }
            });

            $(".dots span").click(function (event) {
                var slideIndex = $(this).index();
                var nextActiveSlide = $($(".slider").children()[slideIndex]);
                $(".dots span").removeClass("active");
                $(this).addClass("active");

                updateSlides(nextActiveSlide);
            });

            var updateSlides = function (nextActiveSlide) {
                var nextActiveSlideIndex = $(nextActiveSlide).index();

                $(".slide_item").removeClass("prev-1");
                $(".slide_item").removeClass("next-1");
                $(".slide_item").removeClass("active");
                $(".slide_item").removeClass("prev-2");
                $(".slide_item").removeClass("next-2");

                nextActiveSlide.addClass("active");

                nextActiveSlide.prev().addClass("prev-1");
                nextActiveSlide.prev().prev().addClass("prev-2");
                nextActiveSlide.addClass("active");
                nextActiveSlide.next().addClass("next-1");
                nextActiveSlide.next().next().addClass("next-2");
            }

            var updateToNextSlide = function (nextActiveSlide) {

            }
        }
        return {
            init: function () {
                initSlider();
            }
        }
    })();

    $(function () {
        Slider.init();
    });
});