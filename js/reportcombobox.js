$(document).ready(function(){
    $('#reportbox').load('report.html #content').hide();

    $('#reportbox').on('click', '#reportCancel', function(){
      $("#reportbox").dialog('close');
    });

    $('#reportbox').on('click', '#reportSubmit', function(){
      $("#reportbox").dialog('close');
    });
})


function reportIssue() {
    $('#reportbox').dialog({
        modal:true,
        width:600,
        height:600
    });
    $('#reportbox').show();
    
}