
$('.dropdown-trigger').dropdown();

$(".alert-success").delay(3000).fadeOut(300, function() {
    $(this).alert('close');
});


$(document).ready(function() {
    $('.sidenav').sidenav();

    $('.delete-button').on('click', function(){

         var algorithm_id = $(this).attr('algorithm_id');

         req = $.ajax({
            url : '/delete',
            type : 'DELETE',
            data : {id : algorithm_id }
         });

         $('#algorithmRow'+algorithm_id).remove();


    });

});