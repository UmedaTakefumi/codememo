var start = new Date("02/05/2014");
var end   = new Date("02/10/2014");

while(start < end){
  console.log(start);

  var newDate = start.setDate(start.getDate() +1);
  start = new Date(newDate);
}


