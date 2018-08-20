// Change the color of each of the headers
let colors = ["primary", "success", "info", "warning", "danger", "rose"]
const adoptableHeaders = document.getElementsByClassName('adopt-header')

let count = 0
Array.prototype.forEach.call(adoptableHeaders, e => {
    // add class to each element
    e.classList.add(`card-header-${colors[count]}`);
    count++
    
    //start at the beginning of the color list if at the end
    if(count >= colors.length){
        colors.reverse()
        count=0
    }
  });
