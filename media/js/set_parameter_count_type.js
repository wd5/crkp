$(function() {
    $('td.count_type').find('select option[value="interval"][selected="selected"]').parent().parent().parent().find('td.count input').hide()
    $('td.count_type').find('select option[value="single"][selected="selected"]').parent().parent().parent().find('td.start_count_interval input, td.end_count_interval input').hide()
    $('td.count_type').live('change',function(){
        if ($(this).find('select option:selected').val()=='interval')
            {
                $(this).parent().find('td.count input').hide()
                $(this).parent().find('td.start_count_interval input').show()
                $(this).parent().find('td.end_count_interval input').show()
            }
        if ($(this).find('select option:selected').val()=='single')
            {
                $(this).parent().find('td.count input').show()
                $(this).parent().find('td.start_count_interval input').hide()
                $(this).parent().find('td.end_count_interval input').hide()
            }
        if ($(this).find('select option:selected').val()=='')
            {
                $(this).parent().find('td.count input').show()
                $(this).parent().find('td.start_count_interval input').show()
                $(this).parent().find('td.end_count_interval input').show()
            }
    });
});