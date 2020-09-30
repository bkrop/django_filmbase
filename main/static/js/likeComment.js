$(document).ready(function () {
    $(".likeBtn").click(function () {
        var serializedData = $("#likeForm").serialize();
        let id = $(this).attr('id');
        let url = $(this).attr('data-url');
        let button = $(this);
        let i = button.children();      
        $.ajax({
            url: url,
            data: serializedData,
            type: 'get',
            dataType: 'json',
            success: function (data) {
                console.log(data);
                $(`#${id}.counter`).html(data.likes_counter);
                if (data.like === true) {
                    i.removeClass('far fa-thumbs-up');
                    i.addClass('fas fa-thumbs-up');
                } else {
                    i.removeClass('fas fa-thumbs-up');
                    i.addClass('far fa-thumbs-up');
                }
            }
        })
    });
});