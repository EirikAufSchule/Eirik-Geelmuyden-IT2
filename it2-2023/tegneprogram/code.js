var body = document.querySelector("body")


var width = window.innerWidth

var width_pixels = 300*1.614
var height_pixels = 300
var pixel_side = width/width_pixels

var children = body.children

for(let i = 0; i < height_pixels; i++){
    for(let n = 0; n < width_pixels; n++){
        children.append(document.createElement(class))
    }
}

