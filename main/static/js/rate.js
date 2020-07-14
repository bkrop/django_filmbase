$(document).ready(function(){
    $("#rateButton").click(function(){
        var serializedData = $("#rateForm").serialize();
        $.ajax({
            url: $("rateForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function(response){
                console.log(response);
                $('#myRate').html(response);
            }
        })
    });
});