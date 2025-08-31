    # Cross Country Ranking
    #### Video Demo:  <https://youtu.be/Kn4mx7tTeNc?si=irDJ9bDjof4031Lk>
    #### Description: My project takes a csv file containing the names, pr's(5K), gender, and grade of high school cross-country  runners as a command line argument

    Explanation of project.py file
    -It then sorts each runners into a few lists(that are stored in respective dict's to make searching easier) based on their gender and grade.
    -Then the program sorts each list individualy by each runner's pr time with index 0 in each list being the fastest of that list
    -The program then presents the user with 4 choices of what they want to do:
        -See a specific number of top runners
        -See what runner is at a specific rank
        -See the stats for a specific runner by name
        -End the program
    -The program will continue to ask that question until the user enter's "4" ending the program
    -If the user chooses options 1 or 2, the program prompts them for the gender and grade they would like to sort by, options being:
        -all, m, f (for gender)
        -all,9,10,11,12 (for grade)
    -Option 1 will then ask for how many runners you want to see then display the runners, similarly but slightly different, option 2 will ask for
    what rank you would like to see and then display it
    -If the user chooses option 3, the program simply prompts for a name, then searches the primary list for that runner by name and if found, the runner's stats will be printed.
    However if the runner does not exist in the data, the program will prompt the user for a name again until a valid name is input.
    -If the user chooses option 4, the program ends and displays a "Program exited" message in the terminal
    -One thing to note is that the program error checks all inputs from the user in the terminal and will prompt the user again if an unexpected input is given.
    -The program will also raise a ValueError if any of the information from the csv file is formatted or input incorrectly

    Explanation of test_project.py file
    -Because my project required so much user input I had to research how to test a function that get's input during its running
    -I ended up deciding to use pytests monkeypatch system to temporarily set a default value to any input that is required in the test
    -The file also tests my read_data function which is what reads all of the data from the csv file to my runners_lists dict and the subsequent dict's inside of it
    -Finally it tests my function that get's a runner's stats when given a rank and sorting specifications by making sure it returned the correct runner or returned that there was no runner


    Explanation of data.csv file
    -This is my csv file that stores the names, pr's, grades, and gender's of as many runners as you want
    -My file had myself + 100 other runners for a total of 101 runners in the file
    -It had about 41 real people's stats(the first 41 in the list) which were from my school
    -the next 60 people were just randomly genertated people that I made up
    -You can tell if it was a real person or not by their last name, real people had a last name, fake people had the first letter of their first name as their last name


    Explanation of planning.txt file
    -This is the file I layed out and planned out everything i was going to do in the project
    -I refered back to it constantly while making my project so I could remeber what I was doing and keep everything a but more organized and easy to follow
    -This definitely helped me a lot because I had never made a program this large and having a way to organize and go about making the project in steps helped me to avoid errors and confusion
    throughout the project


    Explanation of runner.py file
    -This file contains the code for the custom class "Runner" that I made to store each individual person and their information while being read in from the csv file
    -This was was actually the reason I made the planning.txt file
    -As I was making this file i realized it was getting really long and complicated and I was getting confused and I had not even started the actual program yet
    -So I took the code for the class out of the main project.py file and made a seperate file from which I could just import the class to the main file
    -This helped me avoid confusion in my main file and led me to making the planning file which helped me in the future to keep everything understandable

    






