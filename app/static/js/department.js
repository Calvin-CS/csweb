// Basic department functions.

$(document).ready(function() {
	$('#splash-description').hide();
	$("#home_splash").hover(function() {
		$(this).find("#splash-description").stop(true, true).animate({
			opacity : "show"
		}, "fast");
	}, function() {
		$(this).find("#splash-description").stop(true, true).animate({
			opacity : "hide"
		}, "slow");
	});
		
  $('#myTabs').on('toggled', function (event, tab) {
    console.log(tab);
  });
	$('#search-alt').hide(); // Hide even though it's already hidden
	$('a.search-items').click(function() {
		$('#search-alt').slideToggle("fast"); // First click should toggle to 'show'
		$(this).toggleClass("active");
		return false; // Apply "active" class to anchor when items are shown
	});


 toggleText();

 });
  
function toggleText(){
	jQuery('.classDescription p').hide();
	jQuery('.classDescription a').click( function() {
		jQuery(this).next().slideToggle();
	});


}

// Google Search

/* old search engine
function loadGoogleCustomSearch(){
google.load('search', '1', {language: 'en', style: google.loader.themes.MINIMALIST});
					google.setOnLoadCallback(function() {
					  var customSearchOptions = {};
					  var orderByOptions = {};
					  orderByOptions['keys'] = [{label: 'Relevance', key: ''} , {label: 'Date', key: 'date'}];
					  customSearchOptions['enableOrderBy'] = true;
					  customSearchOptions['orderByOptions'] = orderByOptions;
					  var imageSearchOptions = {};
					  imageSearchOptions['layout'] = 'google.search.ImageSearch.LAYOUT_POPUP';
					  customSearchOptions['enableImageSearch'] = true;
					  customSearchOptions['overlayResults'] = true;
					  var customSearchControl =   new google.search.CustomSearchControl('014765828617444448285:-dihpvijuni', customSearchOptions);
					  customSearchControl.setResultSetSize(google.search.Search.FILTERED_CSE_RESULTSET);
					  var options = new google.search.DrawOptions();
					  options.setAutoComplete(true);
					  customSearchControl.draw('cse', options);
					}, true);
}

function loadGoogleCustomSearchSmall(){
google.load('search', '1', {language: 'en', style: google.loader.themes.MINIMALIST});
					google.setOnLoadCallback(function() {
					  var customSearchOptions = {};
					  var orderByOptions = {};
					  orderByOptions['keys'] = [{label: 'Relevance', key: ''} , {label: 'Date', key: 'date'}];
					  customSearchOptions['enableOrderBy'] = true;
					  customSearchOptions['orderByOptions'] = orderByOptions;
					  var imageSearchOptions = {};
					  imageSearchOptions['layout'] = 'google.search.ImageSearch.LAYOUT_POPUP';
					  customSearchOptions['enableImageSearch'] = true;
					  customSearchOptions['overlayResults'] = true;
					  var customSearchControl =   new google.search.CustomSearchControl('014765828617444448285:-dihpvijuni', customSearchOptions);
					  customSearchControl.setResultSetSize(google.search.Search.FILTERED_CSE_RESULTSET);
					  var options = new google.search.DrawOptions();
					  options.setAutoComplete(true);
					  customSearchControl.draw('cse-small', options);
					}, true);
}
*/
// Universal Google Analytics

(function(i, s, o, g, r, a, m) {
	i['GoogleAnalyticsObject'] = r;
	i[r] = i[r] || function() {
		(i[r].q = i[r].q || []).push(arguments)
	}, i[r].l = 1 * new Date();
	a = s.createElement(o), m = s.getElementsByTagName(o)[0];
	a.async = 1;
	a.src = g;
	m.parentNode.insertBefore(a, m)
})(window, document, 'script', '//www.google-analytics.com/analytics.js',
		'ga');
ga('create', 'UA-864318-1', 'calvin.edu');
ga('send', 'pageview');



/*This function is used for technews article for updating the admin tech_newfeed by calling asyncranysly. */ 
 $(function() {
    $(".updateNews").click(function() {
    	var url = $(this)[0].name;
    	$(this)[0].disabled=true
	  //alert (dataString);return false;
	  $.ajax({
	    type: "GET",
	    url: url,
	    data: "",
	    success: function() {
	      $('#contact_form').html("<div id='message'></div>");
	      $('#message').html("<h2>Contact Form Submitted!</h2>")
	      .append("<p>We will be in touch soon.</p>")
	      .hide()
	      .fadeIn(1500, function() {
	        $('#message').append("<img id='checkmark' src='images/check.png' />");
	      });
	    }
	  });
  return false;
    });
	return false;
  });


