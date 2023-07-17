/*************************************
@@File: Job Stock  Template Custom Js

All custom js files contents are below
**************************************
* 00. Loader
* 01. Company Brand Carousel
* 02. Client Story testimonial
* 03. Bootstrap wysihtml5 editor
* 04 Grid Slider
* 05 Grid Slider 2
* 06. Tab Js
* 07. Add field Script
* 08 Add Field
* 09 Background Image
* 10 City Select
* 11 Styles
**************************************/

(function($){
"use strict";


	$(window).on('load', function() {
		$('.stock-facts li span').counterUp({
			delay: 100,
			time: 800
		});
	});

	/*--- Company Brands --*/
	$("#company-brands").owlCarousel({
		items:5,
		itemsDesktop:[1199,4],
		itemsDesktopSmall:[979,3],
		itemsTablet:[768,3],
		itemsMobile:[480,2],
		pagination: false,
		navigation:false,
		navigationText:["",""],
		autoPlay:true
	});
	
	/*--- Client Story testimonial --*/
	$("#client-testimonial-slider").owlCarousel({
		items:3,
		itemsDesktop:[1199,3],
		itemsDesktopSmall:[979,2],
		itemsTablet:[768,1],
		pagination: false,
		navigation:false,
		navigationText:["",""],
		autoPlay:true
	});
	
	/*---Bootstrap wysihtml5 editor --*/	
	$('.textarea').wysihtml5();
	
	/*------ Grid Slider ----*/
	$('.grid-slide').slick({
	  slidesToShow:3,
	  arrows:false,
	  autoplay:true,
	  infinite: true,
	  responsive: [
		{
		  breakpoint: 768,
		  settings: {
			arrows:false,
			centerMode: true,
			slidesToShow:2
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			arrows: false,
			centerPadding: '0px',
			slidesToShow: 1
		  }
		}
	  ]
	});
	
	/*------ Grid Slider ----*/
	$('.grid-slide-2').slick({
	  slidesToShow:2,
	  arrows:false,
	  autoplay:true,
	  infinite: true,
	  responsive: [
		{
		  breakpoint: 768,
		  settings: {
			arrows:false,
			centerMode: true,
			slidesToShow:1
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			arrows: false,
			centerPadding: '0px',
			slidesToShow: 1
		  }
		}
	  ]
	});
	
	/*---Tab Js --*/
	$("#simple-design-tab a").on('click', function(e){
		e.preventDefault();
		$(this).tab('show');
	});
	
	/*-----Add field Script------*/
	$('.extra-field-box').each(function() {
    var $wrapp = $('.multi-box', this);
    $(".add-field", $(this)).on('click', function() {
        $('.dublicat-box:first-child', $wrapp).clone(true).appendTo($wrapp).find('input').val('').focus();
    });
    $('.dublicat-box .remove-field', $wrapp).on('click', function() {
        if ($('.dublicat-box', $wrapp).length > 1)
            $(this).parent('.dublicat-box').remove();
		});
	});
	
	//   Background image ------------------
		var a = $(".bg");
		a.each(function (a) {
			if ($(this).attr("data-bg")) $(this).css("background-image", "url(" + $(this).data("bg") + ")");
		});
		
		$('.slideshow-container').slick({
        slidesToShow: 1,
        autoplay: true,
        autoplaySpeed:2000,
        arrows: false,
        fade: true,
        cssEase: 'ease-in',
        infinite: true,
        speed:2000
    });
	
	// City Select
	$('#choose-city').select2();
	
	// Category Select
	$('#choose-category').select2();
	
	// Category Select
	$('#choose-category2').select2();
	
	// Category Select
	$('#j-category').select2({
		placeholder: "Choose Category...",
		allowClear: true
	});
	
	// Levels
	$('#levels').select2();
	
	// Types
	$('#types').select2();
	
	// --------- Job List --------
	var options = {
		url: "./assets/js/resources/joblist.json",

		getValue: "name",

		list: {
			match: {
				enabled: true
			}
		}
	};
	
	// --------- Companies --------
	var options = {
		url: "./assets/js/resources/companies.json",

		getValue: "name",

		list: {
			match: {
				enabled: true
			}
		}
	};

	$("#companies").easyAutocomplete(options);
	
	// --------- Location --------
	var options = {
		url: "./assets/js/resources/location.json",

		getValue: "name",

		list: {
			match: {
				enabled: true
			}
		}
	};

	$("#location").easyAutocomplete(options);
		
	// Styles ------------------
    function csselem() {
        $(".slideshow-container .slideshow-item").css({
            height: $(".slideshow-container").outerHeight(true)
        });
        $(".slider-container .slider-item").css({
            height: $(".slider-container").outerHeight(true)
        });
    }
    csselem();	
			
	})(jQuery);