$(document).ready(function(){
    $("#commentBtn").click(function(){
        var serializedData = $("#commentForm").serialize();
        $.ajax({
            url: $("commentForm").data('url'),
            data: serializedData,
            type: 'post',
            dataType: 'json',
            success: function(data){
                console.log(data);
                $('.comments').append('<p>' + data.comment.content + '</p><small>' + data.comment.author +  '/' + data.comment.date_of_create + '</small>');
                $('textarea').val('');
            }
        })
    });
});