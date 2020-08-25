$(document).ready(function(){
    $("#rateButton").click(function(){
        var serializedData = $("#rateForm").serialize();
        $.ajax({
            url: $("rateForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function(data){
                console.log(data);
                $('#myRate').html(data);
            }
        })
    });
});