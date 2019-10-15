document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("mainHeader").onclick = function() {
      this.style.color = 'orange'
    }
  })

  $( document ).ready(function() {
    $( "#bio" ).click(function() {
      $( "#bio" ).fadeOut( "slow", function() {
      });
    });
  });