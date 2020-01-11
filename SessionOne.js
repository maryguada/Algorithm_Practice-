// Back to Basics. Basic 13 Algorithms. 

// Q1) print 1 - 255 

// function print255(arr) {
//     for (i = 0 ; i < 256; i++){ 
//         console.log(i)
//     }
// }
// print255()

// ___________________________________________

// Q2) print sum 0 - 255 
// function printSum(arr){
//     var sum = 0; 
//     for (var i=0; i<arr.length; i++){
//         sum += arr[i]; 
//     }
//     console.log(sum);
//     return sum;
// }

// printSum([100,200,-100])

// ___________________________________________

//Q3) find and print max 
// function findMax(arr){
//     var max = arr[0]; 

//     for (var i = 0; i < arr.length; i ++){
//         if (max < arr[i]){
//             max = arr[i]
//         }
//     }
//     console.log(max);
//     return max; 
// }
// findMax([33,22,0,77])
// ___________________________________________

//Q4) array with odds 
// function printOdds(arr){
//     var odds_arr = []; 

//     for (var i = 0; i < 256 ; i++) {
//         if( i % 2 === 1){
//             odds_arr.push(i)
//         }
//     }
//     console.log(odds_arr);
//     return(odds_arr)
// }
// printOdds()
// ___________________________________________

//Q5) Greater than Y. 
// function greaterThanY(Y,arr){
//     var count = 0;
//     for (var i = 0; i < arr.length; i++){
//         if (arr[i] > Y){
//             count ++
//         }
//     } 
//     console.log(count);
//     return count;
// }
// greaterThanY(2,[2,2,3,4,5,60])
// greaterThanY(-10,[-9,-8,-2])
// ___________________________________________

//Q6) Find the Max, Min, and Average
// function maxMinAve(arr){
//     var max = arr[0];
//     var min = arr[0];
//     var sum = 0

//     for (var i =0; i < arr.length; i++){
//         if(min < arr[i]){
//             min = arr[i];
//         }
//         if (arr[i]>max){
//             max =arr[i];
//         }
//         sum += arr[i];
        
//     }

//     var avg = sum / arr.length
//     console.log("The minimum is " +min+ "," +"The max is " +max+ "," + "The Average is "+avg)
// }
// maxMinAve([10,1,2,3])
// ___________________________________________

//Q7) Swap string for array negative values 
// function swapNegatives(arr){
//     var newArr = [];
//     for (var i = 0; i<arr.length; i++){
//         if (arr[i] > 0){
//             newArr.push(arr[i]); 
//         }
//         else{
//             newArr.push('dojo')
//         }
//     }
//     return newArr
// }
// console.log(swapNegatives([-2,-3,1,1,1]))

// function swapNegNums(arr){
//     for (var i = 0; i<arr.length; i++){
//         if (arr[i] < 0){
//             arr[i] = "dojo";
//         }
//     }
//     return arr;
// }
// console.log(swapNegNums([-1,-1,-2,0,0,-2]))

// ___________________________________________

//Q8) Print Odds 1 - 255 
// function printOdds255(arr){
    
//     for(var i =0; i<256; i++){
//         if (i % 2 === 1){
//             console.log(i);
//         }
//     }
//     return i;
//     // console.log(i)
// }
// console.log(printOdds255())
// ___________________________________________

//Q9) Iterate and Print Array 
// function printarr(arr){
//     for (var i = 0; i < arr.length; i++){
//         console.log(i);
//     }
//     return i;
// }
// console.log(printarr([1,2,3]))

// ___________________________________________
// Q10) Get and Print Ave 
// function getAve(arr){
//     var sum = 0; 
//     for(var i=0; i<arr.length ;i++){
//         sum += arr[i];
//     }
//     var ave = sum/arr.length
//     return ave;
// }
// console.log(getAve([1,2,3,4,5]))

// ___________________________________________
//Q11) Square the Values in a given array
// function squareVal(arr){
//     for(var i = 0; i <arr.length; i++){
//         arr[i] = arr[i] * arr[i];
//     }
//     return arr;
// }
// y = squareVal([2,5,6])
// console.log(y)

// ___________________________________________
//Q12) Zero out negative numbers in an array 
// function ZeroOut(arr){
//     for (var i =0 ; i<arr.length; i++){
//         if(arr[i] < 0){
//             arr[i] = 0;
//         }
//     }
//     return arr; 
// }

// y = ZeroOut([1,1,-1,-5,-7])
// x = ZeroOut([2,-3,-3,-100])

// console.log(y)
// console.log(x)

// ___________________________________________
//Q13) Shift Array Values 
// Given an array, move all values forward by one index,
// dropping the first and leaving a '0' value at the end. 

function ShiftVals(arr, start, end){
    for(var i = 0; i<arr.length; i++){
        
    }
}







