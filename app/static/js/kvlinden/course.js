// Course functions
function addConstructionBanner(flag) {
	if (flag) {
		var constructionBanner = document.createElement("div");
		constructionBanner.id = "construction";
		constructionBanner.innerHTML = "<img src=\"/images/kvlinden/icons/construction.gif\" valign=\"middle\" /> This page is not finalized.";
		var header = document.getElementById("header");
		header.parentNode.insertBefore(constructionBanner, header.nextSibling);
	}
}

function hideClassExercises(flag) {
	if (flag) {
		var exercises = document.querySelectorAll(".exercise-hidden");
		for (var i = 0; i < exercises.length; i++) {
			console.log(exercises[i]);
			document.body.removeChild(exercises[i]);
		}
	}
}

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

