// https://learn.nucamp.co/mod/page/view.php?id=5548
// https://eloquentjavascript.net/3rd_edition/03_functions.html#h_XqQR5FlX+8
let x = 10;
if (true) {
  let y = 20;
  var z = 30;
  console.log(x + y + z);
  // → 60
}
// y is not visible here
console.log(x + z);
// → 