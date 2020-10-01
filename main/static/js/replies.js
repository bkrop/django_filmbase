$(document).ready(function () {
    $(".showReplies").click(function () {
        let id = $(this).attr('id');
        let div = $(`#${id}.replies`)
        let text = $(`#${id}.showReplies`).text();
        div.toggle();})})