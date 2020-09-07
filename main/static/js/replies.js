$(document).ready(function () {
    $(".showReplies").click(function () {
        let id = $(this).attr('id');
        $(`#${id}.replies`).toggle();
        $.ajax({
            url: $(this).attr("data-href"),
            type: 'get',

            success: function (data) {
                console.log(data);
                $(`#${id}.replies`).html(data);
                let text = $(`#${id}.showReplies`).text()
                if (text == 'Pokaż odpowiedzi') {
                    text = 'Ukryj'
                    $(`#${id}.showReplies`).text(text)
                } else {
                    text = 'Pokaż odpowiedzi'
                    $(`#${id}.showReplies`).text(text)
                }
            }
        })
    });
});