/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    stack = []
    for (let i=0; i<nums.length; i++){
        if (nums[i]%2==0){
            stack.unshift(nums[i])
        } else {
            stack.push(nums[i])
        }
    }
    return stack
};