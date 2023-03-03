let reminder = 0;
let sum = 0;
let m = 200;
let tmp = 0;

for(n = 1; n <= m; n++){
    tmp = n;
    while(tmp > 0){
        //shrink number
        reminder = tmp % 10;
        //factorial
        fact = 1;
        for(let i = 2; i <= reminder; i++){
            fact *= i
        }
        //add factorial to sum
        sum += fact
        tmp = Math.trunc(tmp/10)
    }

    //check sum
    if(sum == n){
        console.log(n + " is a strong num");
        sum = 0;
    }
    else{
        sum = 0;
    }
}