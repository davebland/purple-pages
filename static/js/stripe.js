/** PURPLE PAGES STRIPE ELEMENTS JS FOR SUBSCRIPTION PAYMENTS **/

// Create Stripe payment elements in payment form when subscription form submitted
$('#subscription-form').submit(function(subscriptionForm) {
    // Collect form data
    let subscriptionFormData = $(this).serializeArray();   
    // Disable subscription form and display spinner
    subscriptionForm.preventDefault();
    $('#subscription-form :input').prop('disabled', true);
    $('#subscribe-button').addClass('is-loading');
    // Request payment intent and setup payment form
    $.post(subscriptionFormData[0].value, subscriptionFormData)
    .done(function(paymentIntentData) {
        // Display subscription payment info
        let paymentAmount = (paymentIntentData.paymentAmount / 100).toFixed(2);
        $('#stripe-payment-information').text(`Make a payment of £${paymentAmount} to subscribe to Purple Pages for ${paymentIntentData.subscriptionPeriod} days`);
        // Create and display stripe payment elements     
        let stripe = Stripe(paymentIntentData.stripePublicKey);
        let stripeElements = stripe.elements();
        let stripeStyle = {
            base: {               
                color: '#363636',
            }
        };
        let stripePaymentElements = stripeElements.create("card", {style:stripeStyle});
        stripePaymentElements.mount("#stripe-card-element");
        $('#stripe-payment-information').show(ANIMATION_DURATION);
        $('#stripe-payment-form').show(ANIMATION_DURATION);
        $('#payment-control-buttons button').show(ANIMATION_DURATION);

        // Listen for stripe input validation errors and display  
        stripePaymentElements.addEventListener('change', ({error}) => {
            if (error) {
                // Show error and disable submit button
                $('#stripe-card-errors').text(error.message);
                $('#stripe-card-errors').show(ANIMATION_DURATION);
                $('#stripe-submit').prop('disabled', true);
            } else {
                // Hide error and enable submit button
                $('#stripe-card-errors').hide(ANIMATION_DURATION);
                $('#stripe-card-errors').empty();
                $('#stripe-submit').prop('disabled', false);
            }        
        });

        // Make a stripe payment when form submitted
        $('#stripe-payment-form').submit(function(stripePaymentForm) {
            // Disable payment for imputs and buttons and display spinner   
            stripePaymentForm.preventDefault();
            $('#payment-cancel-button').prop('disabled', true);
            $('#stripe-submit').prop('disabled', true);
            stripePaymentElements.update({'disabled': true});
            $('#stripe-submit').addClass('is-loading');
            
            //Make a payment request
            stripe.confirmCardPayment(paymentIntentData.stripeClientSecret, {
                payment_method: {
                    card: stripePaymentElements
                }
            })
            .then(function(paymentResult) {
                // Handle the payment result from stripe
                if (paymentResult.error) {
                    // Show error and re-enable form
                    $('#stripe-card-errors').text(paymentResult.error.message);
                    $('#stripe-card-errors').show(ANIMATION_DURATION);
                    $('#payment-cancel-button').prop('disabled', false);
                    $('#stripe-submit').prop('disabled', false);
                    stripePaymentElements.update({'disabled': false});
                    $('#stripe-submit').removeClass('is-loading');
                } else {
                    // Successfull payment, show message then re-load page
                    $('#stripe-payment-success').show(ANIMATION_DURATION);
                    $('#stripe-payment-form').hide(ANIMATION_DURATION);
                    $('#payment-control-buttons button').hide(ANIMATION_DURATION);
                    window.setTimeout("location.reload(true)", 10000);
                }
            })                
        })
    })
    .fail(function(error) {
        // Show unable to request payment error        
        $('#stripe-connection-error').show(ANIMATION_DURATION);
        window.setTimeout("location.reload(true)", 20000);
    })
    .always(function() {
        // Clear loading spinner
        $('#subscribe-button').removeClass('is-loading');
    });
});