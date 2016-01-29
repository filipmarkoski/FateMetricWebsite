$(function(){

      //nav affix
      $('#BB-nav').affix({
          offset: {
              top: $('header').height()
          }
      });

      //search form
      //close on escape key
      $(document).keyup(function(e) {
          if(e.which === 27){
              closeSearch();
          }
      });

      function closeSearch() {
          $('.search-field').val('');
          $('.search-field').hide();
          $('#search-nav').removeClass('active');
          $('#search-nav button[type="reset"]').hide();
      }

      function openSearch() {
          $('#search-nav').addClass('active');
          $('.search-field').show();
          $('#search-nav button[type="reset"]').show();
      }

      // Show Search if form is not active or input search empty
      $('#search-nav button[type="submit"]').click(function(event) {
          if(!$( "#search-nav" ).hasClass( "active" ) || $('.search-field').val() === '') {
              event.preventDefault();
              openSearch();
          }
      });

      //close form
      $('#search-nav button[type="reset"]').click(function(event) {
          //event.preventDefault();
          closeSearch();
      });
  });