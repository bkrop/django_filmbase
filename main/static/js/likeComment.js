$(document).ready(function () {
    $(".likeBtn").click(function () {
        var serializedData = $("#likeForm").serialize();
        let id = $(this).attr('id');
        let url = $(this).attr('data-url');
        console.log(id);
        console.log(url);
        $.ajax({
            url: url,
            data: serializedData,
            type: 'get',
            dataType: 'json',
            success: function (data) {
                console.log(data);
                console.log(data.comment.post)
                $(`#${id}.counter`).html(data.likes_counter)
            }
        })
    });
});