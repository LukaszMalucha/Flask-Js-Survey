
$('.dropdown-trigger').dropdown();

$(".alert-success").delay(3000).fadeOut(300, function() {
    $(this).alert('close');
});

$(".alert-warning").delay(3000).fadeOut(300, function() {
    $(this).alert('close');
});


$(document).ready(function() {
    $('.sidenav').sidenav();

    $('.tooltipped').tooltip();
});