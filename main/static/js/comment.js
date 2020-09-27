$(document).ready(function () {
    $("#commentBtn").click(function () {
        var serializedData = $("#commentForm").serialize();
        $.ajax({
            url: $("commentForm").data('url'),
            data: serializedData,
            type: 'post',
            dataType: 'json',
            success: function (data) {
                console.log(data);
                console.log(data.comment.post)
                $('.comments').load('post_comments/' + data.comment.post);
                $('textarea').val('');
            }
        })
    });
});