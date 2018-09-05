document.addEventListener("DOMContentLoaded", () => {
    // On page statup log if the page has supports the file API
    console.log("page ready");
    if (window.File && window.FileReader && window.FileList && window.Blob) {
        console.log("The File API is supported in this browser");
    } else {
        console.log("The File API is not supported in this browser");
    }
    

  // Using a standard <input type="file"> element. JavaScript returns the list of selected File objects as a FileList.
  // Handle the selection of files

  //toggle visibility
  const toggle = elem => {
      elem.classList.toggle('hidden')
  }

  // generate a preview image on file load
  const previewImage = () => {
      const preview = document.getElementById('preview');
      const file = document.getElementById('id_image').files[0];
      const reader = new FileReader();

      reader.addEventListener('load', () => {
          preview.src = reader.result;
          console.log(preview.classList)
          if (preview.classList.contains('hidden')){
              toggle(preview)
          }

      });
    
      reader.readAsDataURL(file);
  }

  document.getElementById('id_image').addEventListener('change', previewImage);
});
