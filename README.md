# algorithms_find_pairs
function that finds pairs of integers from a list that sum to a given value. The function will take as input the list of numbers as well as the target sum.

# inputs
there is an input.json file where the input data is located. there you can enter the numbers that you want to evaluate, they must be entered as a string and separated by commas, and a target that will be the result of the sum of the two values that we want

Example:
{
    "list_of_integers": "1,9,5,0,20,-4,12,16,7",
    "target": 12
}

# run
launch python in cmd, and import the file app.

>> import app
>> app.launchApp()

the function returns an array with the possible values for the target

Output:
[[-4, 16], [0, 12], [5, 7]]

# test
You can validate the app using the pytest library, and it can be run from the console in the test_app.py file path

>> pytest