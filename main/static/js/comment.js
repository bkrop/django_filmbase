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
                $('#comments').html(data['comment']);
                $('textarea').val('');
            }
        })
    });
});