Vanessa Rychlinski 506 Final Project README “GeniusBook” 12/13/16
1. Describe your project in 1-4 sentences. Include the basic summary of what it does, and the output that it should generate/how one can use the output and/or what question the output answers.

GeniusBook uses words culled from your Facebook wall posts and runs them as keywords through Genius.com’s API. The searches match your words with song lyrics, and the user is given the option of reading the lyrics and viewing associated album art as well. 

2. Explain exactly what needs to be done to run your program (what file to run, anything the user needs to input, anything else) and what we should see once it is done running (should it have created a new text file or CSV? What should it basically look like?).
(Your program running should depend on cached data, but OK to write a program that would make more sense to run on live data and tell us to e.g. use a sample value in order to run it on cached data.)
EXAMPLE: First run python myproject.py Then, when it asks for a 3-letter airport code, type an airport abbreviation. You should type "DTW" to use the cached data. You should have a new file in your directory afterward called airport_info.csv which contains... <explain further> etc.

Run python 506_project.py 
It should run on my cached files I provide; one for my Facebook data, and another from Genius searches resulting from that data. 

3. List all the files you are turning in, with a brief description of each one. (At minimum, there should be 1 Python file, 1 file containing cached data, and the README file, but if your project requires others, that is fine as well! Just make sure you have submitted them all.)

My main project code file is 506_project.py
The Facebook cache is facebook_wall_cache.txt 
The Genius cache made from search terms is genius cache.txt
The output is lyric_profile.csv

4. Any Python packages/modules that must be installed in order to run your project (e.g. requests, or requests_oauthlib, or...):

requests
json
webbrowser
string
unittest


5. What API sources did you use? Provide links here and any other description necessary.

https://docs.genius.com/#search-h2
https://genius.com/api-clients

https://developers.facebook.com/tools/explorer
https://developers.facebook.com/docs/graph-api


6. Approximate line numbers in Python file to find the following mechanics requirements (this is so we can grade your code!):

- Sorting with a key function: - Use of list comprehension OR map OR filter: 123
- Class definition beginning 1: 16
- Class definition beginning 2: 128
- Creating instance of one class: 94
- Creating instance of a second class: 183
- Calling any method on any class instance (list all approx line numbers where this happens, or line numbers where there is a chunk of code in which a bunch of methods are invoked): GeniusHit class 185, FBpost 96 
- (If applicable) Beginnings of function definitions outside classes: create_word_lst 101, non repeat 113, read_lyrics 149 (this one opens a web browser for reading lyrics as well as for viewing related cover art)
- Beginning of code that handles data caching/using cached data: Facebook 78, Genius 161
- Test cases: 236, 238, 240, 242, 244, 246, 248, 250 




7. Rationale for project: why did you do this project? Why did you find it interesting? Did it work out the way you expected?


I decided to do this project because I like music, poetry, and writing. I wanted to do some sort of music recommender and I felt that this was sort of  a strange sidestep but because I like reading song lyrics, here we are. I originally intended the code to create a list of songs for each keyword term, but it turned out with just one which I think is fine also… This project sort of makes a zany mixed-media profile of Facebook user-generated content. One thing I didn’t realize was that some content on Genius is in the form of text from poetry, famous speeches, and even interviews. 

I tried to take out as many non-words as possible and did a fair bit of work on the rmv method of the Facebook class (line 44) to delete instances of punctuation. Using .remove for any words that *contained* the punctuation, did not work for all instances of any such words, thus I settled on going backwards and adding words sanitized of instances of digits or punctuation back into the master list. In the end it was fun for me to get the pieces to work together.