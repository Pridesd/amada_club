// var didScroll; 
// var lastScrollTop = 0; 
// var delta = 5; 
// var navbarHeight = $('header').outerHeight(); 

// $(window).scroll(function(event){
//      didScroll = true; 
// }); 
// setInterval(function() {
//      if (didScroll) {
//           hasScrolled();
//            didScroll = false; 
//         } 
// }, 250); 

// function hasScrolled() {
//       var st = $(this).scrollTop();

//      // Make sure they scroll more than delta 
//     if(Math.abs(lastScrollTop - st) <= delta) 
//         return; 
//     // If they scrolled down and are past the navbar, add class .nav-up. 
//     // This is necessary so you never see what is "behind" the navbar. 
//     if (st > lastScrollTop && st > navbarHeight){
//         // Scroll Down 
//         $('header').removeClass('nav-down').addClass('nav-up');
//     } else  { 
//         // Scroll Up
//         if(st + $(window).height() < $(document).height()){
//              $('header').removeClass('nav-up').addClass('nav-down'); 
//         } 
//     }

//     lastScrollTop = st; 
// }

jQuery(window).scroll(function() {    
    var scroll = jQuery(window).scrollTop();
    if (scroll >= 100) {       
        jQuery(".header").addClass("change_background-color");
    } else
    {
        jQuery(".header").removeClass("change_background-color");
    }
}); 

// function addressKindChange(e) {
//     var seoul = ["강남", "홍대", "영등포", "여의도"];
//     var sejong = [];
//     var busan = [];
//     var daegu = [];
//     var kwangju = [];
//     var incheon = [];
//     var daejeon = [];
//     var ulsan = [];
//     var gyeonggi = ["수원", "평택", "용인"];
//     var gangwon = [];
//     var chungcheongnam = ["천안", "세종", "논산"];
//     var chungcheongbuk = [];
//     var 
//     var target = document.getElementById("addressKindD");

//     if(e.value == "a") var d = seoul;
//     else if(e.value == "b") var d = gyeonggi;
//     else if(e.value == "c") var d = chungcheongnam;

//     target.options.length = 0;

//     for (x in d) {
//         var opt = document.createElement("option");
//         opt.value = d[x];
//         opt.innerHTML = d[x];
//         target.appendChild(opt);
//     }   
// }