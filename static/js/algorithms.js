$(document).ready(function() {

    $('#DataTable').dataTable();
// INSERT ALGORITHM
    $('#formAlgorithm').on('submit', function(event){
        $.ajax({
            type : 'POST',
            url : '/algorithms',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                name: $('#name').val(),
                description: $('#description').val(),
            })
        })
        .done(function(data){
            console.log(data);
            if (data.status > 299) {
                $('#messageError').text(data.message).show().fadeOut(5000);
            }
            else if (data.status == 200){
                $('td').hide();
                location.reload();

            }
        });
        event.preventDefault();
    });

// DELETE ALGORITHM
    $('.delete-button').on('click', function(){
        var algorithm_name = $(this).attr('algorithm_name');

         req = $.ajax({
            url : '/algorithms',
            type : 'DELETE',
            contentType: 'application/json;charset=UTF-8',
            data : JSON.stringify({name: algorithm_name, })

         });

         $('#algorithmRow_'+algorithm_name).remove();

    });
});
