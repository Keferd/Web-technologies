$(document).ready(function() {
$(".main__two-column__element p").hide();
});
$(".main__two-column__element p").click(function () {
$(this).hide("slow");
});
$(".main__two-column__element h3").click(function () {
$(this).next("p").show("slow");
});
