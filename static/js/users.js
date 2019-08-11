$(document).ready(function() {


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
});