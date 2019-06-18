# python_challenge
Python homework

Includes PyBank and PyPoll homework for UMN Data Visualization and Analytics boot camp. 

Both projects use os and csv modules. Both projects require opening and reading csv files, creating variables, creating lists using .append, writing for loops, and writing txt files.  

Detailed annotations in both files. 

PyBank was solved by converting csv files into two lists for Date and Profit/Loss. Employed loop to find Monthly Change from data in Profit/Loss. Used index from Monthly Change and index from Date to identify months during which maximum and minimum occured. Caveats included out of range (solved by subtracting one from the length of list) and lack of correspondence between index numbers (solved by adding one to the index). 

PyPoll was solved by using lists and dictionaries. PyPoll does not require use of first two columns from csv file--only the candidate name matters. Made a list of all of the votes, then looped through it to create a dictionary. For each name, I determined whether the name was already in my dictionary. If it was not, I added it to the dictionary as a key (with value 1). If it was, I increased the existing value for that key by one. This gave me the number of times each name appeared in the list (or the number of votes each candidate received). After the dictionary was complete, I created new variables for the winning candidate, the maximum number of votes recieved, each element that I would require in my summary output table (unique candidate names, percent of votes received, votes recieved). I populated a list with all of the elements of the outcome summary. At the same time, I found the maximum votes recieved (and with it, the corresponding candidate). The summary list was structured much in the way that it needed to be for the summary table, but because it was a list, it would print with commas and brackets. To make it more attractive (and easier to input into my table), I converted it into a string using .join and adding line breaks between each of the list entries.

Acknowledgements: I recieved guidance on both projects. 

For PyBank, TA Max Giesler provided guidance that helped me successfully calculate the change in profit or loss for each month. 

For PyPoll, User Honeybear on StackOverflow's response to a question about splitting items in a list into a string (with line breaks) led me to the "\n".join solution that I used in printing my results nicely (the "pretty_outcomeSummary"). My tutor, Brent Hillen, helped me with syntax and introduced me to the very valuable .3f that, when combined with my percent variable, converted my percentages from very long decimals to decimals that displayed only the first three decimal places. 

Additional acknowledgements to my study group, whose support and encouragement helped me persevere.
