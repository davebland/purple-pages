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