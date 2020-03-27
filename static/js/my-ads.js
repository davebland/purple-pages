// Advert delete modal
$('.advert-delete-button').click(function() {
    // Update the delete URL to reference the selected advert
    let selectedAdvertPk = parseInt($(this).attr('data-advertpk'))
    let advertDeleteUrlSpecific = advertDeleteUrl.replace(9999, selectedAdvertPk);    
    $('#advert-delete-link').attr('href', advertDeleteUrlSpecific);
    // Show the modal
    $('#advert-delete-modal').addClass('is-active');    
})

$('.modal-close, #advert-delete-modal-cancel').click(function() {
    // Reset delete URL        
    $('#advert-delete-link').attr('href', advertDeleteUrl);
    // Hide the modal
    $('#advert-delete-modal').removeClass('is-active');
})

/* Create/Edit Form */
$('#id_image').change(function() {
    // Update filename box when file selected  
    $('#id_filename').text($(this)[0].files[0].name);
    $('#id_filename').addClass('has-background-primary');
})

$('#advert-add-edit-form').submit(function() {
    // Add loading spinner when form submitted
    $('#advert-create-update-submit-button').addClass('is-loading').prop('disabled', true);
})