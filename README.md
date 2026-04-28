For my calorie tracker project, I created a tracker that calculates TDEE as well as logs food calories and macros to a given file. The file is created by a user 
user input is required for the tracker to run properly. The file uses food macros from a csv file that has about 100 different types of food and their data on the 
spreadsheet. 

I faced many difficulties with this project as I had to learn how to use matplotlib for the very first time. This was also my first time coding something this big in 
Python that had many interlinking parts. 

As of right now, while my code is fully functioning, the only problems I cannot seem to find the answer to is how to make my matplotlib graph cleanly show the data for the 
week. For example, when the user inputs food data to file, the data is connected to the bar chart in matplotlib to show the totals for the whole week. The problem I'm 
having is that the bar charts show the food data for everytime the user logs food. So, if the user logs food then closes the program and reopens it to log more food, 
the bar graph displays those entries. So instead, the user would have to log all their food together to get the right amount data. 

Another problem I faced was getting my user's information and connecting it to the TDEE tracker. I realized I would probably have to call the function of the user data 
but that also messed with my code and I would get errors. My TA came up with the idea of making the user data global so that it could apply to the TDEE without having to
be in a weird position and potentially undefined. This also helped the structure of the main set up because TDEE fuction was showing before the main screen. 

Also, as scary as it was using a new coding program like matplotlib, I found it to be quite satisfying once I got the hang of it. I used a basic introductor video to help 
me understand how it works and it wasn't to bad to follow. It took me sooooo long to get the bar graphs to display because I could
