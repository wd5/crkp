$(function(){

    $('.fancybox').fancybox();

    $('div.faq').live('click',function(){
        $(this).toggleClass('faq_curr')

    });

    $('area').mouseenter(alert('ok!')).mouseleave(alert('foo!'));

});
