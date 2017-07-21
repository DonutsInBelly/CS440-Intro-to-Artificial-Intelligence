var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
var boxSize = 20;
var boxes = Math.floor(1000/boxSize);
canvas.addEventListener('click', handleClick);
canvas.addEventListener('click', handleClick);
//ctx.fillStyle = 'green';
//ctx.fillRect(10, 10, 100, 100);

function drawBox() {
  ctx.beginPath();
  ctx.fillStyle = "white";
  ctx.lineWidth = 3;
  ctx.strokeStyle = 'black';
  for (var row = 0; row < boxes; row++) {
    for (var column = 0; column < boxes; column++) {
      var x = column * boxSize;
      var y = row * boxSize;
      ctx.rect(x, y, boxSize, boxSize);
      ctx.fill();
      ctx.stroke();
    }
  }
  ctx.closePath();
}

function handleClick(e) {
  ctx.fillStyle = "black";

  ctx.fillRect(Math.floor(e.offsetX / boxSize) * boxSize,
    Math.floor(e.offsetY / boxSize) * boxSize,
    boxSize, boxSize);
}

drawBox();
