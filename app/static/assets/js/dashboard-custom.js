/*************************************
@@File: Job Stock  Template Custom Js

**************************************/

(function($){
"use strict";

	/*---Bootstrap wysihtml5 editor --*/	
	$('.about').wysihtml5();
	
	/*---Bootstrap wysihtml5 editor --*/	
	$('.resume').wysihtml5();

	// Category
	$('#jb-category').select2();
	
	// Category
	$('#jb-type').select2();
	
	// Category
	$('#jb-level').select2();
	
	// Skills
	$(".multiple-skill").select2({
		placeholder: "Choose Skills"
	});
	
	// language
	$(".language").select2({
		placeholder: "Choose language"
	});
	
	// Job Filter
	$('#jb-filter').select2();
	
	// Job Filter
	$('#jb-filter-date').select2();
	
	// Application Filter
	$('#application-status').select2();
	
	$('[data-toggle="tooltip"]').tooltip();
			
})(jQuery);