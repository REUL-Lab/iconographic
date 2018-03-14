$(document).ready(function(){
    $('#editbox').load('/editicon #content').hide();

    $('#editbox').on('click', '#editCancel', function(){
      $("#editbox").dialog('close');
    });

    $('#editbox').on('click', '#editSubmit', function(){
      $("#editbox").dialog('close');
    });

    $("td button").click(function(){
        $('#editbox').dialog({
            modal:true,
            width:600,
            height:600
        });
        $('#editbox').show();
    });
        
})