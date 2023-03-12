$(".btn_abs").click(function () {
    console.log("abx");
    let src_img = $(this).siblings()[0].src;
    $(".modal_img").modal("show");
    $("#popup-img").attr("src", src_img);
});

$(".update_note").click(function () {
    $("#message-text").val("");
    if ($(this).siblings()[1].tagName == "P") {
        $("#message-text").val($(this).siblings()[1].textContent);
    }
    $("#id-text").val($(this).attr("id"));
    $("#update-note-form").attr("action", `/update-note/${$(this).attr("id")}`);
    $(".modal_update_note").modal("show");
});
