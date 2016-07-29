$(document).ready(function(){
    $("[id^=cc_deployment_button]").click(function(){
        $("#deployment_buttons").addClass("hidden");
        var id=$(this).attr("id");
        var deployment=id.split('-')[1];
        var form_id = "#release_form-".concat(deployment);
        $(form_id).removeClass("hidden");
        $("#node_screen_back_button").removeClass("hidden")
        $("#toggle_div").removeClass("hidden");
        $("#release_book_toggle").attr("deployment", deployment);

    });
    $("#node_screen_back_button").click(function(){
        $("#deployment_buttons").removeClass("hidden");
        $("[id^=release_form-]").addClass("hidden");
        $(this).addClass("hidden");
        $("#toggle_div").addClass("hidden");
    });
    $('#release_book_toggle').change(function(){
        var deployment = $("#release_book_toggle").attr("deployment")
        if($(this).prop('checked')){
            $('#release_form-'+deployment).removeClass('hidden');
            $('#book_form-'+deployment).addClass('hidden');
        }
        else {
            $('#release_form-'+deployment).addClass('hidden');
            $('#book_form-'+deployment).removeClass('hidden');
        }   
    });

});
