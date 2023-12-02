

document.addEventListener('DOMContentLoaded', function () {
    
  });

  document.addEventListener('DOMContentLoaded', function () {
    new bootstrap.Carousel(document.getElementById('myCarousel'));
  });


  // carousel slider text animations
  const carouselCaptions = document.querySelectorAll('.carousel-caption');

  carouselCaptions.forEach((caption) => {
    caption.addEventListener('focus', function () {
      var headerText=document.getElementById("#carousel-text");
      headerText.innerHTML="Changed Text";
    });
  });

  
  function selectImage(imageUrl) {
    // Update the carousel to display the selected image
    $('#myCarousel .carousel-inner').find('.carousel-item').removeClass('active');
    $('#myCarousel .carousel-inner').find(`[src="${imageUrl}"]`).parent().addClass('active');
  }