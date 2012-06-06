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

    $('.connect_menu a').live('click',function(){
        $(this).parent().parent().find('li').removeClass('curr');
        $(this).parent().addClass('curr');
        if ($(this).attr('name') == '1')
            {
                $('.ul_2_3').hide();
                $('.ul_4_5').hide();
            }
        if ($(this).attr('name') == 'serv_2_3')
            {
                $('.ul_4_5').hide();
                $('.ul_2_3').show();
                var a = $('.ul_2_3').find('a[name="2"]')
                a.parent().parent().find('li').removeClass('curr');
                a.parent().addClass('curr');
                AjaxLoadSrv('2');
            }
        if ($(this).attr('name') == 'serv_4_5')
            {
                $('.ul_2_3').hide();
                $('.ul_4_5').show();
                var a = $('.ul_4_5').find('a[name="4"]')
                a.parent().parent().find('li').removeClass('curr');
                a.parent().addClass('curr');
                AjaxLoadSrv('4');
            }

        return false;
    });

    $('.status_menu a').live('click',function(){
        $(this).parent().parent().find('li').removeClass('curr');
        $(this).parent().addClass('curr');
        return false;
    });

    $('.load_srv_link').live('click',function(){
        AjaxLoadSrv($(this).attr('name'));
        return false;
    });

    $('#save_serv_request').live('click',function(){
        var data = {
                full_name:$('#id_full_name').val(),
                phonenumber:$('#id_phonenumber').val(),
                email:$('#id_email').val(),
                service:$('#id_service').val(),

                form_type:$('#form_type').val()
                }
        CheckForm(data);
        return false;
    });
});

function CheckForm(data_fields){
    $.ajax({
        url: "/services/checkform/",
        data: data_fields,
        type: "POST",
        success: function(data) {
            if (data=='success')
                {$('.modal').replaceWith("<div align='center'>Заявка отправлена. Мы свяжемся с вами в ближайшее время!</div>");}
            else{
                $('.modal').replaceWith(data);
            }
        }
    });
}

function AjaxLoadSrv(id_srv){
    $.ajax({
        url: "/services/loadsrv/",
        data: {
            id:id_srv
        },
        type: "POST",
        success: function(data) {
            $('.doc_serv_block').replaceWith(data);
        }
    });
}

function SetFancy(){
    $('.fancybox').fancybox();
}