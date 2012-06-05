$(function(){

    $('.fancybox').fancybox();

    $('div.faq').live('click',function(){
        $(this).toggleClass('faq_curr')
    });

    $('div.vacancy').live('click',function(){
        $(this).toggleClass('vacancy_curr')
    });

    $('.connect_map area').hover(
      function () {
          $('#cm_'+$(this).attr('alt')).addClass('curr');
      },
      function () {
          $('#cm_'+$(this).attr('alt')).removeClass('curr');
      }
    );

    $('.map_labels a').hover(
      function () {
          $(this).addClass('curr');
      },
      function () {
          $(this).removeClass('curr');
      }
    );

    $('#send_question').live('click',function(){
        $.ajax({
            url: "/faq/checkform/",
            data: {
                question:$('#id_question').val(),
                email:$('#id_email').val()
            },
            type: "POST",
            success: function(data) {
                if (data=='success')
                    {$('.modal').replaceWith("Спасибо за вопрос, мы постараемся ответить на него в самое ближайшее время!");}
                else{
                    $('.modal').replaceWith(data);
                }
            }
        });
        return false;
    });

});