$(function(){
    var dh = $('body').height();

    SetFancy();

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
        CheckForm(data,1);
        return false;
    });

    $('#save_first_serv_request').live('click',function(){
        var data = {
            last_name:$('#id_last_name').val(),
            first_name:$('#id_first_name').val(),
            middle_name:$('#id_middle_name').val(),
            passport_series:$('#id_passport_series').val(),
            passport_number:$('#id_passport_number').val(),
            passport_issued:$('#id_passport_issued').val(),
            passport_issued_date:$('#id_passport_issued_date').val(),
            inn:$('#id_inn').val(),
            actual_address_with_index:$('#id_actual_address_with_index').val(),
            object_title:$('#id_object_title').val(),
            object_location:$('#id_object_location').val(),
            earlier_power_kVA:$('#id_earlier_power_kVA').val(),
            earlier_power_kVt:$('#id_earlier_power_kVt').val(),
            additional_power:$('#id_additional_power').val(),
            max_power:$('#id_max_power').val(),
            other_inf:$('#id_other_inf').val(),

            agent_full_name:$('#id_agent_full_name').val(),
            authority_number:$('#id_authority_number').val(),
            authority_date:$('#id_authority_date').val(),
            phone_number:$('#id_phone_number').val(),
            fax:$('#id_fax').val(),
            email:$('#id_email').val(),

            req_attachment1:$('#id_req_attachment1').prop("checked"),
            req_attachment2:$('#id_req_attachment2').prop("checked"),
            req_attachment3:$('#id_req_attachment3').prop("checked"),
            req_attachment4:$('#id_req_attachment4').prop("checked"),
            req_attachment5:$('#id_req_attachment5').prop("checked"),
            req_attachment6:$('#id_req_attachment6').prop("checked"),
            req_attachment7:$('#id_req_attachment7').prop("checked"),
            req_attachment8:$('#id_req_attachment8').prop("checked"),
            req_attachment9:$('#id_req_attachment9').prop("checked"),

            form_type:$('#form_type').val()
            }
        CheckForm(data,2);
        return false;
    });

    $('#save_second_serv_request').live('click',function(){
        var data = {
            last_name:$('#id_last_name').val(),
            first_name:$('#id_first_name').val(),
            middle_name:$('#id_middle_name').val(),
            passport_series:$('#id_passport_series').val(),
            passport_number:$('#id_passport_number').val(),
            passport_issued:$('#id_passport_issued').val(),
            passport_issued_date:$('#id_passport_issued_date').val(),
            inn:$('#id_inn').val(),
            actual_address_with_index:$('#id_actual_address_with_index').val(),
            object_title:$('#id_object_title').val(),
            object_location:$('#id_object_location').val(),

            temp_period:$('#id_temp_period').val(),

            first_earlier_power_kVA:$('#id_first_earlier_power_kVA').val(),
            first_earlier_power_kVt:$('#id_first_earlier_power_kVt').val(),
            first_additional_power:$('#id_first_additional_power').val(),
            first_max_power:$('#id_first_max_power').val(),

            second_earlier_power_kVA:$('#id_second_earlier_power_kVA').val(),
            second_earlier_power_kVt:$('#id_second_earlier_power_kVt').val(),
            second_additional_power:$('#id_second_additional_power').val(),
            second_max_power:$('#id_second_max_power').val(),

            third_earlier_power_kVA:$('#id_third_earlier_power_kVA').val(),
            third_earlier_power_kVt:$('#id_third_earlier_power_kVt').val(),
            third_additional_power:$('#id_third_additional_power').val(),
            third_max_power:$('#id_third_max_power').val(),
            load_type:$('#id_load_type').val(),
            other_inf:$('#id_other_inf').val(),

            agent_full_name:$('#id_agent_full_name').val(),
            authority_number:$('#id_authority_number').val(),
            authority_date:$('#id_authority_date').val(),
            phone_number:$('#id_phone_number').val(),
            fax:$('#id_fax').val(),
            email:$('#id_email').val(),

            req_attachment1:$('#id_req_attachment1').prop("checked"),
            req_attachment2:$('#id_req_attachment2').prop("checked"),
            req_attachment3:$('#id_req_attachment3').prop("checked"),
            req_attachment4:$('#id_req_attachment4').prop("checked"),
            req_attachment5:$('#id_req_attachment5').prop("checked"),
            req_attachment6:$('#id_req_attachment6').prop("checked"),
            req_attachment7:$('#id_req_attachment7').prop("checked"),
            req_attachment8:$('#id_req_attachment8').prop("checked"),
            req_attachment9:$('#id_req_attachment9').prop("checked"),

            form_type:$('#form_type').val()
            }
        CheckForm(data,2);
        return false;
    });

    $('#save_third_serv_request').live('click',function(){
        var data = {
            org_title:$('#id_org_title').val(),
            egrul_number:$('#id_egrul_number').val(),
            actual_address_with_index:$('#id_actual_address_with_index').val(),
            object_title:$('#id_object_title').val(),
            object_location:$('#id_object_location').val(),

            temp_period:$('#id_temp_period').val(),

            first_earlier_power_kVA:$('#id_first_earlier_power_kVA').val(),
            first_earlier_power_kVt:$('#id_first_earlier_power_kVt').val(),
            first_additional_power:$('#id_first_additional_power').val(),
            first_max_power:$('#id_first_max_power').val(),

            second_earlier_power_kVA:$('#id_second_earlier_power_kVA').val(),
            second_earlier_power_kVt:$('#id_second_earlier_power_kVt').val(),
            second_additional_power:$('#id_second_additional_power').val(),
            second_max_power:$('#id_second_max_power').val(),

            third_earlier_power_kVA:$('#id_third_earlier_power_kVA').val(),
            third_earlier_power_kVt:$('#id_third_earlier_power_kVt').val(),
            third_additional_power:$('#id_third_additional_power').val(),
            third_max_power:$('#id_third_max_power').val(),

            load_type:$('#id_load_type').val(),
            other_inf:$('#id_other_inf').val(),

            agent_full_name:$('#id_agent_full_name').val(),
            authority_number:$('#id_authority_number').val(),
            authority_date:$('#id_authority_date').val(),
            phone_number:$('#id_phone_number').val(),
            fax:$('#id_fax').val(),
            email:$('#id_email').val(),

            director_post:$('#id_director_post').val(),
            director_full_name:$('#id_director_full_name').val(),

            agent_inn:$('#id_agent_inn').val(),
            agent_kpp:$('#id_agent_kpp').val(),
            agent_bik:$('#id_agent_bik').val(),
            agent_bank_title:$('#id_agent_bank_title').val(),
            agent_bank_account:$('#id_agent_bank_account').val(),
            agent_correspond_account:$('#id_agent_correspond_account').val(),

            req_attachment1:$('#id_req_attachment1').prop("checked"),
            req_attachment2:$('#id_req_attachment2').prop("checked"),
            req_attachment3:$('#id_req_attachment3').prop("checked"),
            req_attachment4:$('#id_req_attachment4').prop("checked"),
            req_attachment5:$('#id_req_attachment5').prop("checked"),
            req_attachment6:$('#id_req_attachment6').prop("checked"),
            req_attachment7:$('#id_req_attachment7').prop("checked"),
            req_attachment8:$('#id_req_attachment8').prop("checked"),
            req_attachment9:$('#id_req_attachment9').prop("checked"),
            req_attachment10:$('#id_req_attachment10').prop("checked"),
            req_attachment11:$('#id_req_attachment11').prop("checked"),

            form_type:$('#form_type').val()
            }
        CheckForm(data,2);
        return false;
    });

    $('#save_fourth_serv_request').live('click',function(){
        var data = {
            org_title:$('#id_org_title').val(),
            egrul_number:$('#id_egrul_number').val(),
            egrul_date:$('#id_egrul_date').val(),

            actual_address_with_index:$('#id_actual_address_with_index').val(),
            object_title:$('#id_object_title').val(),
            object_location:$('#id_object_location').val(),

            first_earlier_power_kVA:$('#id_first_earlier_power_kVA').val(),
            first_earlier_power_kVt:$('#id_first_earlier_power_kVt').val(),
            first_additional_power:$('#id_first_additional_power').val(),
            first_max_power:$('#id_first_max_power').val(),

            second_earlier_power_kVA:$('#id_second_earlier_power_kVA').val(),
            second_earlier_power_kVt:$('#id_second_earlier_power_kVt').val(),
            second_additional_power:$('#id_second_additional_power').val(),
            second_max_power:$('#id_second_max_power').val(),

            third_earlier_power_kVA:$('#id_third_earlier_power_kVA').val(),
            third_earlier_power_kVt:$('#id_third_earlier_power_kVt').val(),
            third_additional_power:$('#id_third_additional_power').val(),
            third_max_power:$('#id_third_max_power').val(),

            count_conn_points:$('#id_count_conn_points').val(),
            load_type:$('#id_load_type').val(),
            power_distribution:$('#id_power_distribution').val(),
            other_inf:$('#id_other_inf').val(),

            agent_full_name:$('#id_agent_full_name').val(),
            authority_number:$('#id_authority_number').val(),
            authority_date:$('#id_authority_date').val(),
            phone_number:$('#id_phone_number').val(),
            fax:$('#id_fax').val(),
            email:$('#id_email').val(),

            director_post:$('#id_director_post').val(),
            director_full_name:$('#id_director_full_name').val(),

            agent_inn:$('#id_agent_inn').val(),
            agent_kpp:$('#id_agent_kpp').val(),
            agent_bik:$('#id_agent_bik').val(),
            agent_bank_title:$('#id_agent_bank_title').val(),
            agent_bank_account:$('#id_agent_bank_account').val(),
            agent_correspond_account:$('#id_agent_correspond_account').val(),

            req_attachment1:$('#id_req_attachment1').prop("checked"),
            req_attachment2:$('#id_req_attachment2').prop("checked"),
            req_attachment3:$('#id_req_attachment3').prop("checked"),
            req_attachment4:$('#id_req_attachment4').prop("checked"),
            req_attachment5:$('#id_req_attachment5').prop("checked"),
            req_attachment6:$('#id_req_attachment6').prop("checked"),
            req_attachment7:$('#id_req_attachment7').prop("checked"),
            req_attachment8:$('#id_req_attachment8').prop("checked"),
            req_attachment9:$('#id_req_attachment9').prop("checked"),
            req_attachment10:$('#id_req_attachment10').prop("checked"),
            req_attachment11:$('#id_req_attachment11').prop("checked"),
            req_attachment12:$('#id_req_attachment12').prop("checked"),
            req_attachment13:$('#id_req_attachment13').prop("checked"),

            form_type:$('#form_type').val()
            }
        CheckForm(data,2);
        return false;
    });

    $('#save_fifth_serv_request').live('click',function(){
        var data = {
            org_title:$('#id_org_title').val(),
            egrul_number:$('#id_egrul_number').val(),
            egrul_date:$('#id_egrul_date').val(),

            actual_address_with_index:$('#id_actual_address_with_index').val(),
            object_title:$('#id_object_title').val(),
            object_location:$('#id_object_location').val(),

            first_earlier_power_kVA:$('#id_first_earlier_power_kVA').val(),
            first_earlier_power_kVt:$('#id_first_earlier_power_kVt').val(),
            first_additional_power:$('#id_first_additional_power').val(),
            first_max_power:$('#id_first_max_power').val(),

            second_earlier_power_kVA:$('#id_second_earlier_power_kVA').val(),
            second_earlier_power_kVt:$('#id_second_earlier_power_kVt').val(),
            second_additional_power:$('#id_second_additional_power').val(),
            second_max_power:$('#id_second_max_power').val(),

            third_earlier_power_kVA:$('#id_third_earlier_power_kVA').val(),
            third_earlier_power_kVt:$('#id_third_earlier_power_kVt').val(),
            third_additional_power:$('#id_third_additional_power').val(),
            third_max_power:$('#id_third_max_power').val(),

            cnt_pwr_transformers:$('#id_cnt_pwr_transformers').val(),
            cnt_pwr_generators:$('#id_cnt_pwr_generators').val(),

            count_conn_points:$('#id_count_conn_points').val(),

            load_type:$('#id_load_type').val(),

            tech_min_generators:$('#id_tech_min_generators').val(),
            tech_armor_consumer:$('#id_tech_armor_consumer').val(),
            tech_emergency_armor_consumer:$('#id_tech_emergency_armor_consumer').val(),

            power_distribution:$('#id_power_distribution').val(),
            other_inf:$('#id_other_inf').val(),

            agent_full_name:$('#id_agent_full_name').val(),
            authority_number:$('#id_authority_number').val(),
            authority_date:$('#id_authority_date').val(),
            phone_number:$('#id_phone_number').val(),
            fax:$('#id_fax').val(),
            email:$('#id_email').val(),

            director_post:$('#id_director_post').val(),
            director_full_name:$('#id_director_full_name').val(),

            agent_inn:$('#id_agent_inn').val(),
            agent_kpp:$('#id_agent_kpp').val(),
            agent_bik:$('#id_agent_bik').val(),
            agent_bank_title:$('#id_agent_bank_title').val(),
            agent_bank_account:$('#id_agent_bank_account').val(),
            agent_correspond_account:$('#id_agent_correspond_account').val(),

            req_attachment1:$('#id_req_attachment1').prop("checked"),
            req_attachment2:$('#id_req_attachment2').prop("checked"),
            req_attachment3:$('#id_req_attachment3').prop("checked"),
            req_attachment4:$('#id_req_attachment4').prop("checked"),
            req_attachment5:$('#id_req_attachment5').prop("checked"),
            req_attachment6:$('#id_req_attachment6').prop("checked"),
            req_attachment7:$('#id_req_attachment7').prop("checked"),
            req_attachment8:$('#id_req_attachment8').prop("checked"),
            req_attachment9:$('#id_req_attachment9').prop("checked"),
            req_attachment10:$('#id_req_attachment10').prop("checked"),
            req_attachment11:$('#id_req_attachment11').prop("checked"),
            req_attachment12:$('#id_req_attachment12').prop("checked"),
            req_attachment13:$('#id_req_attachment13').prop("checked"),

            form_type:$('#form_type').val()
            }
        CheckForm(data,2);
        return false;
    });

    $('#save_reception').live('click',function(){
        var data = {
            last_name:$('#id_last_name').val(),
            first_name:$('#id_first_name').val(),
            middle_name:$('#id_middle_name').val(),
            phonenumber:$('#id_phonenumber').val(),
            reception_date:$('#id_reception_date').val(),
            reception_time:$('#id_reception_time').val(),

            form_type:$('#form_type').val(),
            id_serv:$('#id_serv').val(),
            pdf_path:$('#pdf_path').val(),
            serv_type:$('#serv_type').val()
            }
        CheckForm(data,1);
        return false;
    });

});

function CheckForm(data_fields,type){
    $.ajax({
        url: "/services/checkform/",
        data: data_fields,
        type: "POST",
        success: function(data) {
            if (type==1)
                {if (data=='success')
                    {$('.modal').replaceWith("<div align='center'>Заявка отправлена. Мы свяжемся с вами в ближайшее время!</div>");}
                else
                    {$('.modal').replaceWith(data);}
                }
            else
                {
                    $('.modal').replaceWith(data);
                    $('.modal').animate({top:"10px"},"slow");
                    $('html').animate({scrollTop:0},"slow");
                }
        },
        error:function(jqXHR,textStatus,errorThrown) {
            $('.modal_in').replaceWith(jqXHR.responseText);
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
    $('.fancybox-big').fancybox({
        'centerOnScroll':true,
        'onComplete': function() {
            var dh = $('body').height();
            $('#fancybox-overlay').height(dh);
            $('#fancybox-wrap').animate({top:"10px"},"slow");
            $('html').animate({scrollTop:0},"slow");
            if ($('.wrapper').height()<$('.modal').height())
                {
                    $('#fancybox-overlay').height($('.modal').height()+100);
                }
        }
    });

}