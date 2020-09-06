$(document).ready(function () {
    $(".showReplies").click(function () {
        let id = $(this).attr('id');
        $.ajax({
            url: $(this).attr("data-href"),
            type: 'get',

            success: function (data) {
                console.log(data);
                console.log(id)
                $(`#${id}.replies`).html(data);
            }
        })
    });
});