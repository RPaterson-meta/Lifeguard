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
        $("#release_book_toggle").bootstrapToggle('on')

    });
    $("#node_screen_back_button").click(function(){
        $("#deployment_buttons").removeClass("hidden");
        $("[id^=release_form-]").addClass("hidden");
        $("[id^=book_form-]").addClass('hidden');
        $("#node_screen_back_button").addClass("hidden");
        $("#toggle_div").addClass("hidden");
        $("[id^=initials_box_input_field-]").val('')
        $("[id^=note-]").val('')
    });
    $('#release_book_toggle').change(function(){
        var deployment = $("#release_book_toggle").attr("deployment");
        $("#release_book_toggle").attr("release_or_book", "release");
        if($(this).prop('checked')){
            $('#release_form-'+deployment).removeClass('hidden');
            $('#book_form-'+deployment).addClass('hidden');
            $("#release_book_toggle").attr("release_or_book", "release");
        }
        else {
            $('#release_form-'+deployment).addClass('hidden');
            $('#book_form-'+deployment).removeClass('hidden');
            $("#release_book_toggle").attr("release_or_book", "book");
        }
    });
});
