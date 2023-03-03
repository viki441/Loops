let number = 8;
let counter = 0;

for(i=1;i<number;i++){
    if(number/i == Math.trunc(number/i)){
        counter++;
    }
}
if(counter > 2 || number === 1){
    console.log('not prime');//ne e prosto
}
else{
    console.log('prime');//prosto
    
}
