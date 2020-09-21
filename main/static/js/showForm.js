$(document).ready(function(){
    $(".showForm").click(function(){
        let id = $(this).attr('id');
        let div = $(`#${id}.replyFormDiv`);
        console.log(div);
        div.toggle();
    });
});