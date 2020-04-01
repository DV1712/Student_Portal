jQuery(function($) {'use strict',

		
	// Page Loader
	jQuery(window).load(function() { 
		$('#loader-container').fadeOut(); 
		$('#pageloader').delay(350).fadeOut('slow'); 
		$('body').delay(250).css({'overflow':'visible'});
	});
	
	
	// sticky menu 
	jQuery(document).scroll(function () {
		var position = jQuery(document).scrollTop();
		var headerHeight = jQuery('#home').outerHeight();
		if (position >= headerHeight - 86){
				jQuery('#navigation .sticky-menu').addClass('sticked');
		} else {
				jQuery('#navigation .sticky-menu').removeClass('sticked');
		}

	});	
	

	//bxSlider 
	$('#main-slider').bxSlider({
	  mode: 'fade',
	  auto: true,
	  autoControls: true,
	  pause: 6000
	});
	
	
	// Flexslider slider
	$('.captions').flexslider({
		animation: "slide",
		selector: ".slide-show .sliding",
		controlNav: false,
		directionNav: false ,
		slideshowSpeed: 4000,  
		direction: "vertical",
		start: function(slider){
			$('body').removeClass('loading'); 
		}
	});
	
	
	// all Parallax Section
	$(window).bind('load', function () {
		parallaxInit();						  
	});
	
	function parallaxInit() {		
		$("#about-us").parallax("50%", 0.3);
		$("#clients").parallax("50%", 0.3);
		$("#contact-details").parallax("50%", 0.3);
	}	
	parallaxInit();	
	
	
	// portfolio filter
	$(window).load(function(){'use strict',
		$portfolio_selectors = $('.portfolio-filter >li>a');
		if($portfolio_selectors!='undefined'){
			$portfolio = $('.portfolio-items');
			$portfolio.isotope({
				itemSelector : '.col-sm-3',
				layoutMode : 'fitRows'
			});
			
			$portfolio_selectors.on('click', function(){
				$portfolio_selectors.removeClass('active');
				$(this).addClass('active');
				var selector = $(this).attr('data-filter');
				$portfolio.isotope({ filter: selector });
				return false;
			});
		}
	});
	
	//Pretty Photo
	 $("a[data-gallery^='prettyPhoto']").prettyPhoto({
	  social_tools: false
	 });


	// Contact form validation
	var form = $('.contact-form');
	form.submit(function () {'use strict',
		$this = $(this);
		$.post($(this).attr('action'), function(data) {
			$this.prev().text(data.message).fadeIn().delay(3000).fadeOut();
		},'json');
		return false;
	});


	// Navigation Scroll
	$(window).scroll(function(event) {
		Scroll();
	});

	$('.navbar-collapse ul li a').click(function() {  
		$('html, body').animate({scrollTop: $(this.hash).offset().top - 79}, 1000);
		return false;
	});
	
	// Scroll To TOP
	$(function() {
		$("#toTop").scrollToTop();
	});

});


	// User define function
	function Scroll() {
		var contentTop      =   [];
		var contentBottom   =   [];
		var winTop      =   $(window).scrollTop();
		var rangeTop    =   200;
		var rangeBottom =   500;
		$('.navbar-collapse').find('.scroll a').each(function(){
			contentTop.push( $( $(this).attr('href') ).offset().top);
			contentBottom.push( $( $(this).attr('href') ).offset().top + $( $(this).attr('href') ).height() );
		})
		$.each( contentTop, function(i){
			if ( winTop > contentTop[i] - rangeTop ){
				$('.navbar-collapse li.scroll')
				.removeClass('active')
				.eq(i).addClass('active');			
			}
		})

	};
	
	
	// Skill bar Function
		
	$(document).ready(function(){
	  "use strict";
	  $('.skillbar').appear(function() {
		$(this).find('.skillbar-bar').animate({
		  width:$(this).attr('data-percent')
		},3000);
	  });
	});

	// Google Map Customization
	(function(){

		var map;

		map = new GMaps({
			el: '#gmap',
			lat: 43.04446,
			lng: -76.130791,
			scrollwheel:false,
			zoom: 12,
			zoomControl : false,
			panControl : false,
			streetViewControl : false,
			mapTypeControl: false,
			overviewMapControl: false,
			clickable: false
		});

		var image = 'images/map-icon.png';
		map.addMarker({
			lat: 43.04446,
			lng: -76.130791,
			icon: image,
			animation: google.maps.Animation.DROP,
			verticalAlign: 'bottom',
			horizontalAlign: 'center',
			backgroundColor: '#3498DB',
		});


		var styles = [ 

		{
			"featureType": "road",
			"stylers": [
			{ "color": "#333333" }
			]
		},{
			"featureType": "water",
			"stylers": [
			{ "color": "#3498DB" }
			]
		}
		,{
			"featureType": "landscape",
			"stylers": [
			{ "color": "#ffffff" }
			]
		},{
			"elementType": "labels.text.fill",
			"stylers": [
			{ "color": "#3498DB" }
			]
		},{
			"featureType": "poi",
			"stylers": [
			{ "color": "#f6f6f6" }
			]
		},{
			"elementType": "labels.text",
			"stylers": [
			{ "saturation": 1 },
			{ "weight": 0.1 },
			{ "color": "#222222" }
			]
		}

		];


		map.addStyle({
			styledMapName:"Styled Map",
			styles: styles,
			mapTypeId: "map_style"  
		});

		map.setStyle("map_style");
	}());


	//Preloader Functions

	var cSpeed=9;
		var cWidth=75;
		var cHeight=75;
		var cTotalFrames=24;
		var cFrameWidth=75;
		var cImageSrc='images/sprites.gif';
		
		var cImageTimeout=false;
		
		function startAnimation(){
			
			document.getElementById('loaderImage').innerHTML='<canvas id="canvas" width="'+cWidth+'" height="'+cHeight+'"><p>Your browser does not support the canvas element.</p></canvas>';
			
			//FPS = Math.round(100/(maxSpeed+2-speed));
			FPS = Math.round(100/cSpeed);
			SECONDS_BETWEEN_FRAMES = 1 / FPS;
			g_GameObjectManager = null;
			g_run=genImage;

			g_run.width=cTotalFrames*cFrameWidth;
			genImage.onload=function (){cImageTimeout=setTimeout(fun, 0)};
			initCanvas();
		}
		
		
		function imageLoader(s, fun)//Pre-loads the sprites image
		{
			clearTimeout(cImageTimeout);
			cImageTimeout=0;
			genImage = new Image();
			genImage.onload=function (){cImageTimeout=setTimeout(fun, 0)};
			genImage.onerror=new Function('alert(\'Could not load the image\')');
			genImage.src=s;
		}
		
		//The following code starts the animation
		new imageLoader(cImageSrc, 'startAnimation()');
			
