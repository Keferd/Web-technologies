$(document).ready(function() {
$(".main__two-column__element p").hide();
});
$(".main__two-column__element p").click(function () {
$(this).hide("slow");
});
$(".main__two-column__element h3").click(function () {
$(this).next("p").show("slow");
});

$(".main__two-column__element img").hover(
				function() {
					$(this).animate({
						width: "36px",
						height: "36px",
						borderRadius: "2%"
					}, "slow");
				}, function() {
					$(this).animate({
						width: "32px",
						height: "32px",
						borderRadius: "10%"
					}, "slow");
				});
