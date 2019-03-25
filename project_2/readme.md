Generate Text documentation
We have to go through the file and remove commas.
We form dictionary of word pairs and dictionary of probabilites
We have to place for first words, second words, and words before a new line 
because they will not have key value pairs.
Once we iterate through our data and form these dictionaries, we then normalize them.
We then choose to grab a random first word from our first word list.
The generate text will take ta random first word and then a random secondword based on 
the first word.  Our function then predicts the next words before a new line.  
We use our transition dictionary to use probablilites from one word to the next and we 
pick the highest probablity.  We then repeat for the next line.
