### Introduction
- This the week 4 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Define a function `expo_list(input_list)`  that keeps the first inner list, square the second and cube the last one. 
   - E.g. `L = [[1, 2], [2, 3, 4], [5, 6, 7]]` `expo_list(L) => [[1, 2], [4, 9, 16], [125, 216, 343]]`
2. Write the sql query to do the following. You assume that we have the `customers` table from the lecture
   - Get the customers whose address contain 'TRAIL' or 'AVENUE'
   - Get the top three loyal customers, who have the most points
3. We will be using the same Titanic dataset from [HW3](https://github.com/AC4RM/AC4RM-HW3), but we will train a KNN model this time
   - Follow the same preprocessing steps as HW3
   - Split the data into training and testing set (80/20) and use a random seed of 42
   - For K value in `range(5, 200, 5)`, find the optimal K value that achieve the best accuracy score on the test set.
   - Return the model fitted using the optimal K and the array of all the test scores predicted with different K values.
4. Define a function `extract_date(date)` using regex that will return the date, month and year of the input date in a list.
   - You can assume that the date format follows this pattern: `mm/dd/yyyy`
   - E.g.: `extract_date('Post Date: 05/22/2023')` => `[05, 22, 2023]`
5. Create equal length paths in `simple_bettor_v4(initial_funds, initial_wager, intended_rounds)`.
   - Copy the `play_round` function from the previous homework.
   - Pre-allocate the fund path with zeros. The length of fund path should be equal to `intended_rounds+1`
   - Use for loops to loop through all intended rounds. If the player goes broke, save the final wealth. 
   - It is possible for the player to go into debt in the last bet.
   - Return the path of the player fund.
