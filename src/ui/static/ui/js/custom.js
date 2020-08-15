(function ($) {
	"use strict"; // Start of use strict
	/* ---------------------------------------------- /*
	 * Preloader
	/* ---------------------------------------------- */

	$(window).on('load', function () {
		$('#loading').fadeOut();
		$('#preloader').delay(300).fadeOut('slow')
	});
	/*--------------------------
		counter
	---------------------------- */
	// start all the timers
	$('.timer').each(count);

	function count(options) {
		var $this = $(this);
		options = $.extend({}, options || {}, $this.data('countToOptions') || {});
		$this.countTo(options);
	}

	// Fit Text Plugin for Main Header
	$("h1").fitText(
		1.2, {
			minFontSize: '35px',
			maxFontSize: '65px'
		}
	);

	// Offset for Main Navigation
	$('#mainNav').affix({
		offset: {
			top: 100
		}
	})

	/*--------------------------
		Scrolling Animations
	---------------------------- */
	// Initialize WOW.js Scrolling Animations
	new WOW().init();

	// hide #back-top first
	$("#back-top").hide();

	// fade in #back-top
	$(function () {
		$(window).scroll(function () {
			if ($(this).scrollTop() > 100) {
				$('#back-top').fadeIn();
			} else {
				$('#back-top').fadeOut();
			}
		});

		// scroll body to 0px on click
		$('#back-top a').on('click', function () {
			$('body,html').animate({
				scrollTop: 0
			}, 800);
			return false;
		});
	});
	// scroll body to 0px on click		

	// Scroll to a Specific Div
	if($('.scroll-to-target').length){
		$(".scroll-to-target").on('click', function() {
			var target = $(this).attr('data-target');
		   // animate
		   $('html, body').animate({
			   scrollTop: $(target).offset().top
			 }, 1000);
	
		});
	}

	$('a.mouse-icon').on('click', function (event) {
		var $anchor = $(this);
		$('html, body').stop().animate({
			scrollTop: ($($anchor.attr('href')).offset().top - 50)
		}, 1250, 'easeInOutExpo');
		event.preventDefault();
	});


	$('.collapse.in').prev('.panel-heading').addClass('active');
	$('#accordion, #bs-collapse')
		.on('show.bs.collapse', function (a) {
			$(a.target).prev('.panel-heading').addClass('active');
		})
		.on('hide.bs.collapse', function (a) {
			$(a.target).prev('.panel-heading').removeClass('active');
		});
	/*------------------------------------------------
	 * owlCarousel    
	------------------------------------------------*/
	$(function () {
		var owl = $(".owl-carousel");

		owl.owlCarousel({
			autoPlay: 3000,
			items: 4, //10 items above 1000px browser width
			itemsDesktop: [1000, 5], //5 items between 1000px and 901px
			itemsDesktopSmall: [900, 3], // betweem 900px and 601px
			itemsTablet: [600, 2], //2 items between 600 and 0
			itemsMobile: false // itemsMobile disabled - inherit from itemsTablet option
		});
		var owl = $(".owl-carousel2");

		owl.owlCarousel({
			autoPlay: 3000,
			items: 3, //10 items above 1000px browser width     
		});
		var owl = $(".owl-carousel3");

		owl.owlCarousel({
			autoPlay: 3000,
			items: 1, //10 items above 1000px browser width    
		});
		// Custom Navigation Events
		$(".next").on('click', function () {
			owl.trigger('owl.next');
		});
		$(".prev").on('click', function () {
			owl.trigger('owl.prev');
		});
	});

})(jQuery); // End of use strict