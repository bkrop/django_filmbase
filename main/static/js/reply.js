$(document).ready(function(){
    $(".replyBtn").click(function(){
        let id = $(this).attr('id');
        var serializedData = $(`#${id}.replyForm`).serialize();
        console.log(`button id: ${id}`);
        $.ajax({
            url: $(`#${id}.replyForm`).data('url'),
            data: serializedData,
            type: 'post',
            dataType: 'json',
            success: function(data){
                console.log(data);
                console.log(data.comment.post)
                $('.replies').load("http://127.0.0.1:8000/comment_replies/" + data.comment.comment);
                $('textarea').val('');
            }
        })
    });
});