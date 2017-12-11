$(document).ready(function(){
	alert("This page has loaded!");

	//Below is code which hides a paragraph when the button is clicked
	$("button").click(function(){
        $("p").hide("slow", function(){
            alert("The paragraph is now hidden");
        });
    });

	let height = $(window).height();
	let width = $(window).width();
	let $img = $('img') //save it in memory so we don't call the function over and over again.

	//Below is code which allows for the character to move - why not try craft your own version?
	$(document).keydown(function(key) {


        switch(parseInt(key.which,10)) {
			// Left arrow key pressed
			case 37:
                if($img.position().left > 0){
				    $img.animate({left: "-=20px"}, 'fast');
				}
				break;

			// Right Arrow Pressed
			case 39:
				if($img.position().left + $img.width() < width){ //add width to the calc
					$img.animate({left: '+=20px'},'fast');}
				break;

			// Up Arrow Pressed
			case 38:
				$img.animate({top: '-=20px'},'fast');
				break;

			// Down Arrow Pressed
			case 40:
				$img.animate({top: '+=20px'},'fast');
				break;
		}
	});
});
