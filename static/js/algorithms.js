$(document).ready(function() {
// INSERT ALGORITHM
    $('#formAlgorithm').on('submit', function(event){
        $.ajax({
            type : 'POST',
            url : '/algorithms',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                email: $('#email').val(),
                username: $('#algorithm').val(),
                password: $('#description').val(),
            })
        })
        .done(function(data){
            console.log(data);
//            if (data.status > 299) {
//                $('#messageError').text(data.message).show().fadeOut(5000);
//
//            }
//
//            else if (data.status == 200){
//                var confirmation = data.confirmation
//                window.location.href = "/user_confirmation/" + confirmation
//            }

        });
        event.preventDefault();
    });
});