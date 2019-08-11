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
//            window.location.href = "/confirmation_email/"



        });
        event.preventDefault();
    });
});