// Load Payment modal if user has donated 
$(window).on('load', function () {
    if ($('#paymentModal')) {
        $('#paymentModal').modal('show');
    }
});