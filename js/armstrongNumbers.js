// How can you make this more scalable and reusable later?

function findArmstrongNumbers(arr) {
    let answer = arr.filter((element) =>{ 
        let arr = element.toString().split('');
        let pwr = arr.length;
        let count = 0;

        arr.map((e) => {
            count += parseInt(e) ** pwr
        })
        if (element == count) {
            return element
        }
    });

    return answer
};


console.log(findArmstrongNumbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 100, 150, 153, 154, 370]))

module.exports = {findArmstrongNumbers}