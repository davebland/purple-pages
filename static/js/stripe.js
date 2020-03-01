// Stripe elements for subscription payments

// Create Stripe payment elements in payment form when subscription form submitted
$('#subscription-form').submit(function(subscriptionForm) {
    // Collect form data
    let subscriptionFormData = $(this).serializeArray();   
    // Disable subscription form and display spinner
    subscriptionForm.preventDefault();
    $('#subscription-form :input').prop('disabled', true);
    $('#subscribe-button').addClass('is-loading');
    // Request payment intent and setup a payment form
    $.post(subscriptionFormData[0].value, subscriptionFormData)
    .done(function(response) {
        // Create and display stripe payment elements
        console.log(response)
        let stripe = Stripe('pk_test_Tgy18iERVA1liKcyrLebR4sN00fdlqLNY0');
        let stripeElements = stripe.elements();
        let stripeStyle = {
        };
        let stripePaymentElements = stripeElements.create("card", {style:stripeStyle});
        stripePaymentElements.mount("#stripe-card-element");
        $('#stripe-payment-form').show(ANIMATION_DURATION);

        // Listen for stripe input validation errors and display  
        stripePaymentElements.addEventListener('change', ({error}) => {
            if (error) {
                $('#stripe-card-errors').text(error.message);
                $('#stripe-card-errors').show(ANIMATION_DURATION);
            } else {
                $('#stripe-card-errors').hide(ANIMATION_DURATION);
                $('#stripe-card-errors').empty();
            }        
        });

        // Make a stripe payment when form submitted
        $('#stripe-payment-form').submit(function(stripePaymentForm) {
            // Disable subscription form and display spinner   
            stripePaymentForm.preventDefault();
            $('#stripe-payment-form :input').prop('disabled', true);
            stripePaymentElements.update('disabled', true);
            $('#stripe-submit').addClass('is-loading');
        })
    })
    .fail(function(error) {
        // Show unable to request payment error        
        $('#stripe-connection-error').show(ANIMATION_DURATION)
    })
    .always(function() {
        // Clear loading spinner
        $('#subscribe-button').removeClass('is-loading');
    });
});