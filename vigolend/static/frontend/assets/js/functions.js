
     // sticky header
$(window).scroll(function() {    
var scroll = $(window).scrollTop();
//>=, not <=
if (scroll >= 200) {
//clearHeader, not clearheader - caps H
$(".header").addClass("head-tag-sticky");
} else {
$(".header").removeClass("head-tag-sticky");  
}
});
// sticky header end




$(document).ready(function() {

 new WOW().init();
/*mob-menu start*/

$("header .mob-menu-icon").on('click',function(){
    $('body').toggleClass('show-menu');
});

$('.mob-menu .closebtn').on('click',function(){
   $('body').removeClass('show-menu');

});

$('.menu-mobile>ul>li').on('click',function(){
   $(this).children('ul').slideToggle();
   
});

/*mob-menu End*/



/*counter-box start*/
 
$(window).scroll(function() {
   var hT = $('.counterbox').offset().top,
       hH = $('.counterbox').outerHeight(),
       wH = $(window).height(),
       wS = $(this).scrollTop();
    console.log((hT-wH) , wS);
   if (wS > (hT+hH-wH)){
     
$('.counterdigi').each(function() {
        var $this = $(this),
          countTo = $this.attr('data-count');

        $({
          countNum: $this.text()
        }).animate({
            countNum: countTo
          },

          {
            duration: 2000,
            easing: 'linear',
            step: function() {
              $this.text(Math.floor(this.countNum));
            },
            complete: function() {
              $this.text(this.countNum);
            }

          });
    });
   }
});
// counter End




}); //documnet ready end







		
 