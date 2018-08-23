// Change the color of each of the headers
function smoothScroll(target, duration) {
    var target = document.querySelector(target)
    console.log(target);
    console.log(duration);
}

smoothScroll('#outreach', 1000)

const adoptableHeaders = document.getElementsByClassName('adopt-header')

let count = 0
Array.prototype.forEach.call(adoptableHeaders, e => {
    const colors = ["primary", "success", "info", "warning", "danger", "rose"]
    // add class to each element
    e.classList.add(`card-header-${colors[count]}`);
    count++
    //start at the beginning of the color list if at the end
    if (count >= colors.length) {
        colors.reverse()
        count = 0
    }
});