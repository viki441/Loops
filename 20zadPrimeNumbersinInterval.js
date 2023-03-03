let number = 2;
let numberTo = 20;
let counter = 0;
for(number; number<numberTo; number++){

for(i=1;i<=number;i++){
    if(number/i == Math.trunc(number/i)){
        counter++;
    }
}
if(counter > 2 || number === 1){
    //ne e prosto
    counter = 0;
}
else{
    //prosto
    console.log(number);
    counter = 0;
}
}