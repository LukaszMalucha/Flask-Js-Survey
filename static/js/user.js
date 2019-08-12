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
            console.log(data);
            var confirmation = data.confirmation
            window.location.href = "/confirmation_email/" + confirmation
        });
        event.preventDefault();
    });
// CONFIRM REGISTRATION
    $('#confirmationLink').click(function(){
        var link = $(this).attr('value');
        console.log(link),

    event.preventDefault();
    });

});

