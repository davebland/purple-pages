let ANIMATION_DURATION = 800

// Show and hide menu on mobile
$('.navbar-burger').click(function() {
    $('.navbar-burger').toggleClass('is-active');
    $('.navbar-menu').toggleClass('is-active');
})

// Hide notifications when clicked
$('.delete').click(function() {
    $(this).parent().hide(ANIMATION_DURATION);
})