$(document).ready(function(){
    $("[id^=cc_deployment_button]").click(function(){
        $("#deployment_buttons").addClass("hidden");
        var id=$(this).attr("id");
        var node=id.split('-')[1]
        var form_id = "#form-".concat(node)
        $(form_id).removeClass("hidden");
        $("#node_screen_back_button").removeClass("hidden")

    });
    $("#node_screen_back_button").click(function(){
        $("#deployment_buttons").removeClass("hidden");
        $("[id^=form-]").addClass("hidden");
        $(this).addClass("hidden")
    });
});
