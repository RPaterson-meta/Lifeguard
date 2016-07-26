var team = [
    "NJ2",
    "SL",
    "TPR",
    "NB",
    "RJP"
];

$(document).ready(function(){
    $("#initials_box").focusin(function(){
    $("#initials_box").removeClass("has-success has-feedback");
    $("#initials_box_input_field").removeClass("form-control-success")
    $("#initials_box").removeClass("has-warning has-feedback");
    $("#initials_box").removeClass("form-control-warning");
    });
    $("#initials_box").focusout(function(){
        var initials = $("input").val();
        if(team.indexOf(initials) > -1){
            $("#initials_box").addClass("has-success has-feedback");
            $("#initials_box_input_field").addClass("form-control-success")
        }
        else {
            $("#initials_box").addClass("has-warning has-feedback");
            $("#initials_box").addClass("form-control-warning");
        }
    });
});
