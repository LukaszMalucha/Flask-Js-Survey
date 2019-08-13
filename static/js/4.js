$(document).ready(function() {
// REGISTER USER
    $('#formRegister').on('submit', function(event){
        $.ajax({
            type : 'POST',
            url : '/register',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                email: $('#email').val(),
                username: $('#username').val(),
                password: $('#password').val(),
                confirm: $('#confirm').val()
            })
        })
        .done(function(data){
            console.log(data.status);
            if (data.status > 299) {
                $('#messageError').text(data.message).show().fadeOut(5000);

            }

            else if (data.status == 200){
                var confirmation = data.confirmation
                window.location.href = "/user_confirmation/" + confirmation
            }

        });
        event.preventDefault();
    });



// CONFIRM REGISTRATION
    $('#confirmationLink').click(function(){
        var confirmation = $(this).attr('confirmation');
        var link = $(this).attr('value');
//        $.ajax({
//            type : 'POST',
//            url : '/register',
//            contentType: 'application/json;charset=UTF-8',
//            data: JSON.stringify({
//                email: $('#email').val(),
//                username: $('#username').val(),
//                password: $('#password').val(),
//                confirm: $('#confirm').val()
//            })
//        })



        console.log(confirmation),

    event.preventDefault();
    });

});

