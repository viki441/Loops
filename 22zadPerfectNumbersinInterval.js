let total = 0;
for (let n = 1; n <= 100; n++) {
    for (let j = 1; j<= n/2; j++) {
        if (!(n%j)){
           total += j;
        }
    }
    if (n === total) console.log(total +" "+'perfect');
    total=0;
}