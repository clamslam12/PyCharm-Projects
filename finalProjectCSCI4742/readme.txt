This program will generate all possible permutations of a given input string. The running time of the program is n! 
so longer strings may take a long time. After printing the results/permutations to the console, the program will write all permutations to a textfile.
Menu options: 
1) Help- this mode explains information about normal and custom brute force method and their inputs. 
2) Normal Brute Force- the user will enter a string and the program will find all possible permutations of it. If string inputs contain
duplicate characters, the program will dynamically delete any duplicate results, print them on to the console, and write them to a textfile.
3) Custom Brute Force- the user will enter a string, a custom string, and placement of custom string and the program will find all possible 
permutations of it. A custom string can be placed in front or back of a permutation string. For example if the user wanted to place the string '123' in front of 
each permutation, the custom string input will be '123' and placement input will be 'f'. If string inputs contain duplicate characters, 
the program will dynamically delete any duplicate results, print them on to the console, and write them to a textfile. 
4) Exit- will exit the program.

Link to Youtube video demonstration = https://youtu.be/J9plnosYotQ

Example Input/Output for Normal Brute Force
********* Brute Force for Wordlists/Passwords **********
1. Help
2. Normal Brute Force w/ output to file
3. Custom Brute Force w/ output to file
4. Exit
Enter an option: 2
Enter your string: abc
abc
acb
bac
bca
cba
cab

Example Input/Output for Custom Brute Force
********* Brute Force for Wordlists/Passwords **********
1. Help
2. Normal Brute Force w/ output to file
3. Custom Brute Force w/ output to file
4. Exit
Enter an option: 3
Enter your string: abc
Enter your custom string: 123
Enter your custom string placement (f for front, b for back): f
123abc
123acb
123bac
123bca
123cba
123cab

	 