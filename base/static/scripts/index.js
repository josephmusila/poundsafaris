$(document).ready(function () {

  var showDesc=$('show-det');
  showDesc.html("Show Less..");

  var imageSection = $('.image-section');
  NavBarActiveCheck();
  setInterval(changeBackgroundSlider, 3000);
  setInterval(sidePosterSlider, 3000);

  removeBreaks();
});



var navbar = document.getElementById('navbar');
var aboutHeader = document.getElementById('about-header');
var topImage=document.getElementById('top-image');
var imageSection = document.getElementById('image-section');


var sticky = navbar.offsetTop;

window.onscroll = function () {
  stickNavbar();
};

function getRandomSlide(index) {
  var imageSlider =[
    "https://c4.wallpaperflare.com/wallpaper/967/938/472/rock-atlantic-ocean-rugged-miradouro-da-ponta-do-rosto-wallpaper-preview.jpg",
    "https://c4.wallpaperflare.com/wallpaper/878/61/227/landscape-nature-rice-paddy-terraces-wallpaper-preview.jpg",
    "https://c4.wallpaperflare.com/wallpaper/781/184/27/national-park-south-america-el-chalten-chile-wallpaper-preview.jpg",
    "https://c4.wallpaperflare.com/wallpaper/92/481/105/lion-lion-cub-family-cub-wallpaper-preview.jpg"
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

    navbar.classList.add('sticky');
    imageSection.style.marginTop = '10rem';
    aboutHeader.style.marginTop = '10rem';
    topImage.style.marginTop='10rem';
    if (window.innerWidth < 800) {
      imageSection.style.marginTop = '0rem';
      topImage.style.marginTop='0rem';
    }
    // imageSection.classList.add('add-margin') ;
  } else {
    navbar.classList.remove('sticky');
    // imageSection.classList.add('marg');
  }
}

function changeBackgroundSlider() {
  var randomNumber = Math.floor(Math.random() * 4);
  var imageURL = getRandomSlide(randomNumber);
  // $('.image-content-title').text(imageURL.title);
  // console.log(imageURL);
  $('.image-section').css('background-image', 'url(' + imageURL + ')');
}


function sidePosterSlider() {
  var posters = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5uXNhsYWP2uCbR0qBlWwPjqJo-Bt2XUaqfw&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUfmWAbCzJyBHwS90VHLPKFmaxted6b761lvG0WZi8TS1fnjqXzmTDtVfNlDc1HE8Esow&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKBIh1MCdlgDadkLJFSEE7b4G3BjBeXQHp_Q&usqp=CAU"
  ];
  var randomNumber = Math.floor(Math.random() * 3);
  $('.side-poster-placeholder').css('background-image', 'url(' + posters[randomNumber] + ')');
}


function removeBreaks(){
  var pBreaks = $(".desc-wrapper").find("br");
  var lineBreak = $("<br>");
  
  pBreaks.remove();
  console.log(pBreaks.length);
}

function NavBarActiveCheck() {
  // nav titles
  var home = $("#home");
  var about = $("#about");
  var safari = $("#safari");
  var deals = $("#hot-deals");
  var visa = $("#visa");
  var blog = $('#blog');
  var contact = $('#contact');

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
      isActive: false
    };
    Items.push(NavItem);
  });

  Items.forEach((element, index, array) => {
    element.subTitle === emptySubMenu ? $(menuCarets[index]).remove() : $(menuCarets[index]).html(careRight);
    $(element.title).on('click', function () {
      element.isActive = true;
      submenu.html(element.subTitle);
    });

    $(element.title).mouseover(function () {
      submenu.html(element.subTitle);

      element.subTitle === emptySubMenu ? $(menuCarets[index]).remove() : $(menuCarets[index]).html(caretDown);
    }).mouseout(function () {
      element.subTitle === emptySubMenu ? $(menuCarets[index]).remove() : $(menuCarets[index]).html(careRight);
      $(menuCarets[index]).html(careRight);
    });

  });

}


