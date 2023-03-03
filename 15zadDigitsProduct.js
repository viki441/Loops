//enter number
let n = 92;
//this is the sum
let sum = 1;
//as long as our number is more than 0:
while (n>0) {
    if(n<=9 && n>0){
        sum = sum * n;
        break;
    }
    sum = sum * n%10;
   n = Math.trunc(n/10);

}
//and display
console.log(sum);
