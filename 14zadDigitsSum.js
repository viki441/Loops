//enter number
let n = 999;
//this is the sum
let sum = 0;
//as long as our number is more than 0:
while (n>0) {
   sum = sum + n%10;
   n = Math.trunc(n/10);
}
//and display
console.log(sum);
