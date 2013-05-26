$(document).ready(function(){

  $('#myCheckbox').click(function() {
      var checked = $(this).is(':checked');

      $.ajax({
          type: "POST",
          url: 'http://localhost/ci_datepickar/index.php/site/index',
          data: { checked : checked },
          success: function(data) {
              alert('it worked');
          },
          error: function() {
              alert('it broke');
          },
          complete: function() {
              alert('it completed');
          }
      });
  });

});