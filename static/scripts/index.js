$(document).ready(function () {
 
  stickyNavbar();
  var showDesc = $("show-det");
  showDesc.html("Show Less..");
  var imageSection = $(".image-section");
  NavBarActiveCheck();
  setInterval(changeBackgroundSlider, 3000);
  setInterval(sidePosterSlider, 3000);
  googleTranslateElementInit();
  removeBreaks();
 
 
});

function stickyNavbar(){
  $(window).scroll(function(){
      if($(this).scrollTop() > 100){
        
          $(".nav-container").addClass("sticky-nav");
          // rotateCards(); 
      }else{
          $(".nav-container").removeClass("sticky-nav");
      }
  })
}

function googleTranslateElementInit() {
  // new google.translate.TranslateElement({ pageLanguage: 'sw', layout: google.translate.TranslateElement.InlineLayout.SIMPLE }, 'google_translate_element');
  // new google.translate.TranslateElement({ pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.VERTICAL }, 'google_translate_element');
  // new google.translate.TranslateElement({ pageLanguage: 'en', autoDisplay: true, gaia: true }, 'google_translate_element');
  new google.translate.TranslateElement(  
    {pageLanguage: 'en'},  
    'google_translate_element'  
);  
}

var navbar = document.getElementById("navbar");
var aboutHeader = document.getElementById("nav-overlay");
var topImage = document.getElementById("top-image");
var imageSection = document.getElementById("image-section");

// var sticky = navbar.offsetTop;
// window.onscroll = function () {
//   stickNavbar();
// };

function getRandomSlide(index) {
  var image = "static/images/madeira.jpg";
  var imageSlider = [
    "static/images/backyard.jpg",
    "static/images/beach.jpg",
    "static/images/elephant.jpg",
    "static/images/nairobi.jpg",
    "static/images/zebra.jpg",
  ];

  var sliderImageTitles = Array.from(imageSlider.keys());
  var sliderImages = Array.from(imageSlider.values());
  // return sliderItem = {
  //   title: sliderImageTitles[index],
  //   image: sliderImages[index]
  // }

  return imageSlider[index];
}

function stickNavbar() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
    imageSection.style.marginTop = "10rem";
    aboutHeader.style.marginTop = "10rem";
    topImage.style.marginTop = "10rem";
    if (window.innerWidth < 800) {
      imageSection.style.marginTop = "0rem";
      topImage.style.marginTop = "0rem";
      aboutHeader.style.marginTop = "0rem";
    }
    // imageSection.classList.add('add-margin') ;
  } else {
    navbar.classList.remove("sticky");
    // imageSection.classList.add('marg');
  }
}

function changeBackgroundSlider() {
  var randomNumber = Math.floor(Math.random() * 5);
  var imageURL = getRandomSlide(randomNumber);
  // $('.image-content-title').text(imageURL.title);
  // console.log(imageURL);
  $(".image-section").css("background-image", "url(" + imageURL + ")");
}

function sidePosterSlider() {
  var posters = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5uXNhsYWP2uCbR0qBlWwPjqJo-Bt2XUaqfw&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUfmWAbCzJyBHwS90VHLPKFmaxted6b761lvG0WZi8TS1fnjqXzmTDtVfNlDc1HE8Esow&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKBIh1MCdlgDadkLJFSEE7b4G3BjBeXQHp_Q&usqp=CAU",
  ];
  var randomNumber = Math.floor(Math.random() * 3);
  $(".side-poster-placeholder").css(
    "background-image",
    "url(" + posters[randomNumber] + ")"
  );
}

function removeBreaks() {
  var pBreaks = $(".desc-wrapper").find("br");
  var lineBreak = $("<br>");

  pBreaks.remove();

}

function NavBarActiveCheck() {
  // nav titles
  var home = $("#home");
  var about = $("#about");
  var safari = $("#safari");
  var deals = $("#hot-deals");
  var visa = $("#visa");
  var blog = $("#blog");
  var contact = $("#contact");

  // nav subtitles
  var safariSubMenu = $("#submenu-item-safari");
  var dealSubMenu = $("#submenu-item-deals");
  var submenu = $(".submenu");
  var emptySubMenu = "";

  var menuCarets = $(".menu-item-wrapper").find(".caret-span");
  var caretDown = '<i class="fa fa-caret-down"></i>';
  var careRight = '<i class="fa fa-caret-right"></i>';

  submenu.html(emptySubMenu);

  var navItems = new Map([
    [home, emptySubMenu],
    [about, emptySubMenu],
    [safari, safariSubMenu],
    [deals, dealSubMenu],
    [visa, emptySubMenu],
    [blog, emptySubMenu],
    [contact, emptySubMenu],
  ]);

  var navItemsKeys = Array.from(navItems.keys());
  var navItemsValues = Array.from(navItems.values());

  var Items = [];

  navItemsKeys.forEach(function (item, index) {
    var NavItem = {
      title: navItemsKeys[index],
      subTitle: navItemsValues[index],
      isActive: false,
    };
    Items.push(NavItem);
  });

  Items.forEach((element, index, array) => {
    element.subTitle === emptySubMenu
      ? $(menuCarets[index]).remove()
      : $(menuCarets[index]).html(careRight);
    $(element.title).on("click", function () {
      element.isActive = true;
      submenu.html(element.subTitle);
    });

    $(element.title)
      .mouseover(function () {
        submenu.html(element.subTitle);

        element.subTitle === emptySubMenu
          ? $(menuCarets[index]).remove()
          : $(menuCarets[index]).html(caretDown);
      })
      .mouseout(function () {
        // element.subTitle === emptySubMenu ? $(menuCarets[index]).remove() : $(menuCarets[index]).html(careRight);
        $(menuCarets[index]).html(careRight);
      });
  });
}

  function toggleMenu() {
    console.log("hello")
    var nav = document.querySelector('.toggle-menu');
    var nav2 = document.querySelector('.navcontainer');
    // nav.style.display = (nav.style.display === 'block') ? 'none' : 'block';
    nav2.style.display = (nav.style.display === 'block') ? 'none' : 'block';
  }