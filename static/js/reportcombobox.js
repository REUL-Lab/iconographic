$(document).ready(function(){
    $('#reportbox').load('/reports #content').hide();

    $('#reportbox').on('click', '#reportCancel', function(){
      $("#reportbox").dialog('close');
    });

    $('#reportbox').on('click', '#reportSubmit', function(){
      $("#reportbox").dialog('close');
    });

    $('#reportbutton').click(function() {
        $('#reportbox').dialog({
            modal:true,
            width:600,
            height:600
        });
        $('#reportbox').show();
    })
})
