$(document).ready(function() {
// INSERT ALGORITHM
    $('#formAlgorithm').on('submit', function(event){
        $.ajax({
            type : 'POST',
            url : '/algorithms',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                algorithm: $('#algorithm').val(),
                description: $('#description').val(),
            })
        })
        .done(function(data){
            console.log(data);
            if (data.status > 299) {
                $('#messageError').text(data.message).show().fadeOut(5000);
            }
            else if (data.status == 200){
                $('#tableBody').append(
                    '<tr class="gradeA odd" id="algorithmRow5d68b8d1e9946962712a9404" role="row">' +
                    '<td class="center sorting_1" id="suggested_algorithm">XXXXXX</td>' +
                    '<td class="center">zxc</td>' +
                    '<td class="center">' +
                    '<button class="btn btn-small delete-button" algorithm_id="5d68b8d1e9946962712a9404">Delete' +
                    '</button></td></tr>'
                )
            }
        });
        event.preventDefault();
    });
});