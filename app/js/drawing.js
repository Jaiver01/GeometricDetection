var brushWidth = 10;
var color = "#000000";
var drawingcanvas;

(function() {
  var $ = function(id){return document.getElementById(id)};

  drawingcanvas = this.__canvas = new fabric.Canvas('canvas', {
    isDrawingMode: true,
    backgroundColor: "white"
  });

  fabric.Object.prototype.transparentCorners = false;

  if (drawingcanvas.freeDrawingBrush) {
    drawingcanvas.freeDrawingBrush.color = color;
    drawingcanvas.freeDrawingBrush.width = brushWidth;
  }
})();
