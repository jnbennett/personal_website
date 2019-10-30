$(window).scroll(function() {    
    var scroll = $(window).scrollTop();
    if (scroll >= 64) {
        $(".navbar-lower").addClass("navbar-fixed");
    }
    else {
        $(".navbar-lower").removeClass("navbar-fixed");     
    }
});