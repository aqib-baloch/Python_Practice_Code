const arr = [1, 2, 3, 4, 18, 6, 7, 8, 9, 10];

const largestInteger = () => {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  console.log(max);
  return max;
};
// Call the function to print the largest element
largestInteger();
