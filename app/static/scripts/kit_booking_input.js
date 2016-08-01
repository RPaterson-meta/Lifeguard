var team = [
    "NJ2",
    "SL",
    "TPR",
    "NB",
    "RJP"
];

$(document).ready(function(){
    $("[id^=initials_box-]").focusin(function(){
        var id=$(this).attr("id");
        var release_or_book = id.split('-')[1]
        var deployment=id.split('-')[2]
        $(this).removeClass("has-success has-feedback");
        $("#initials_box_input_field-".concat(release_or_book).concat('-').concat(deployment)).removeClass("form-control-success")
        $(this).removeClass("has-warning has-feedback");
        $("#initials_box_input_field-".concat(release_or_book).concat('-').concat(deployment)).removeClass("form-control-warning");
        $("#initials_box_glyph-".concat(release_or_book).concat('-').concat(deployment)).removeClass("glyphicon-ok")
        $("#initials_box_glyph-".concat(release_or_book).concat('-').concat(deployment)).removeClass("glyphicon-warning-sign")
    });
    $("[id^=initials_box-]").focusout(function(){
        var id=$(this).attr("id");
        var release_or_book = id.split('-')[1];
        var deployment=id.split('-')[2];
        var initials = $("#initials_box_input_field-".concat(release_or_book).concat('-').concat(deployment)).val();
        if(team.indexOf(initials.upper()) > -1){
            $(this).addClass("has-success has-feedback");
            $("#initials_box_input_field-".concat(release_or_book).concat('-').concat(deployment)).addClass("form-control-success")
            $("#initials_box_glyph-".concat(release_or_book).concat('-').concat(deployment)).addClass("glyphicon-ok");
        }
        else {
            $(this).addClass("has-warning has-feedback");
            $("#initials_box_input_field-".concat(release_or_book).concat('-').concat(deployment)).addClass("form-control-warning");
            $("#initials_box_glyph-".concat(release_or_book).concat('-').concat(deployment)).addClass("glyphicon-warning-sign");
        }
    });
    $("[id^=select_all_button-]").click(function(){
        var id=$(this).attr("id");
        var release_or_book=id.split('-')[1];
        var deployment=id.split('-')[2];
        var button_category="[id^=checkbox_button-".concat(release_or_book).concat('-').concat(deployment).concat("-]");
        var checkbox_category="[id^=checkbox-".concat(release_or_book).concat('-').concat(deployment).concat("-]");
        $(checkbox_category).each(function(i,obj){
            var id=$(this).attr("id");
            // equal as checkbox not yet js'd
            if ($('#select_all_checkbox-'+release_or_book+'-'+deployment).is(':checked') == $(this).is(':checked')) {
                var node=id.split('-')[3];
                var button="#checkbox_button-".concat(release_or_book).concat('-').concat(deployment).concat("-").concat(node);
                $(button).click();
            }
        });  
    });
});
