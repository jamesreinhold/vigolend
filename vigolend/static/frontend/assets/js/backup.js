<script type="text/javascript">

    $(document).ready(function () {
   
      $("div#makeMeScrollable").smoothDivScroll({
        autoScrollingMode: "onStart"
      });

      $('.testimonials').slick({
    dots: true,
    arrows: false,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay:true,
    
  });


 $('#success').hide();
        $('#wrong').hide();
    });


$(function() { //shorthand document.ready function
    $('#lead_form').on('submit', function(e) { //use on if jQuery 1.7+
        e.preventDefault();  //prevent form from submitting
       
        $('#btnSubmitM').attr("disabled", false);
        var user_data = {
            firstname : $('input[name="firstname"]').val(),
            email : $('input[name="email"]').val(),
            phone : $('input[name="phone"]').val(),
            message : $('textarea[name="message"]').val(),
        };
        console.log(user_data); //use the console for debugging, F12 in Chrome, not alerts
        $.ajax({
            type:'POST',
            url: 'post.php',
            data:user_data,
            success:function(res){
                if(res === '1'){
                    $("#success").show();
                    $('#btnSubmitM').removeAttr("disabled");
                }else if(res === '2'){
                    $('#wrong').show();
                    $('#btnSubmitM').removeAttr("disabled");
                }
            }
        });
    });
});

function goToByScroll(e) { $("html,body").animate({ scrollTop: $(e).offset().top }, 1e3, "", function () { $(this).stop(true, true) }) }

  </script>