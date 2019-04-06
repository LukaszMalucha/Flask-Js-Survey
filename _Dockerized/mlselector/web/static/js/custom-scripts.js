
$('.dropdown-trigger').dropdown();


$(".alert").delay(3000).fadeOut(200, function() {
    $(this).alert('close');
});



$(document).ready(function() {
    $('.sidenav').sidenav();

    $('.deleteButton').on('click', function(){

         var algorithm_id = $(this).attr('algorithm_id');

         req = $.ajax({
            url : '/delete',
            type : 'DELETE',
            data : {id : algorithm_id }
         });

         $('#algorithmRow'+algorithm_id).remove();


    });

});