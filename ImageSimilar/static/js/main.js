function preview() {
    fileUploadControl.src=URL.createObjectURL(event.target.files[0]);
}

$(document).ready(function(){
    $("#close_anounce").click(function(){
        $("#alert").fadeOut("slow");
    });
    $("#input_btn").click(function(){
        $("#input").hide();
    })
});