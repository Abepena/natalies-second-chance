// Trigger color change on different Donation choices
function clearDonation(){
    var customDonation = document.getElementById('customDonation')
    customDonation.value = '';                 
}

function changeStripeAmount(amount) {
    stripeButton.setAttribute('data-amount', amount)
   
}

// Change Donation Button Color and change stripe payment on button click
$('.donation-button').on('click',function () {
    //Remove custom donation value if any
    clearDonation();
    
    //get the amount that this button represents and change the stripe amount
    amount = $('input', this).val();
    changeStripeAmount(amount)
    
    //Change bootstrap classes for styling
    $('.donation-button').not(this).removeClass('btn-success').addClass('btn-outline-success');
    $(this).removeClass('btn-outline-success').addClass('btn-success');
});


// Clear Button Choice onkeying into the custom donation field
$('#customDonation').keyup(function () {
    if ($(this).val.length != 0) {
        $('.donation-option').prop('checked', false);
        $('.donation-button').removeClass('btn-success, active').addClass('btn-outline-success');
    }
});
