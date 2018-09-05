document.addEventListener("DOMContentLoaded", () => {
    //Style the Image label to be the button
    const imageLabel = document.querySelector('label[for=id_image]')
    imageLabel.classList.add('btn','btn-danger')

  //toggle visibility
  const toggle = elem => {
      elem.classList.toggle('hidden')
  }

  // generate a preview image on file load
  const previewImage = () => {
      const preview = document.getElementById('preview');
      const file = document.getElementById('id_image').files[0];
      const reader = new FileReader();
      const output = `<li><strong>Preview: ${file.name}</strong></li>` 
      
      // create and insert list into output tag on form
      document.getElementById('imageFileOutput').innerHTML = `<ul>${output}</ul>`
    
      //generate image preview and toggle its visibility if hidden
      reader.addEventListener('load', () => {
          preview.src = reader.result;
          if (preview.classList.contains('hidden')){
              toggle(preview)
          }

      });
    
      reader.readAsDataURL(file);
  }

  document.getElementById('id_image').addEventListener('change', previewImage);
});
