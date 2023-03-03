//enter values
let number =232434;
let digitNum = 0;
while(number>0){
     number = Math.trunc(number/10);
     digitNum = digitNum + 1;
}
console.log(digitNum);