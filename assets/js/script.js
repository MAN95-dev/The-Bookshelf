$(function() {
  
  $('#bs-example-navbar-collapse-1')
    .on('shown.bs.collapse', function() {
      $('#navbar-hamburger').addClass('hidden');
      $('#navbar-close').removeClass('hidden');    
    })
    .on('hidden.bs.collapse', function() {
      $('#navbar-hamburger').removeClass('hidden');
      $('#navbar-close').addClass('hidden');        
    }); 
});

/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}