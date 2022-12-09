# gourd_crab_game

#### Description:
This is a Vietnamese traditional game that is played every Lunar New Year.

It is same to dice game but we are going to use 3 dices in our game. Also, instead of dots in each side of a dice, we will use pictures of gourd,
crab, shrimp, fish, deer and chicken. That is also the reason why the game is called as gourd crab game or gourd crab shrimp fish game.

In this game, I used tkinter to create buttons as well as to set background with Lunar New Year's atmosphere.

At the beginning of the game, we are asked to choose 1 of 6 options by clicking on the button with images of gourd, crab, shrimp, fish, deer, and chicken.
In addition, we will have $100 in our pocket as starting game. Besides clicking on button to pick our choice, we also have to enter an amount that we wish to
bet in our game. 

The game will start rolling when we hit 'Roll' button. However, the button will show randomly the result with 3 images only when the bars of choice and 
betting amount are filled. Otherwise, messages will be printed to let us know we have to select our choice and enter a valid betting amount to start game.
(If the amount we enter is larger than the amount we have, or it is not a number, or it is zero, the program will print a message to let us know
we should enter a betting amount that less than or equal to our balance)

How to score in the game?
If our choice is not in the result, we will loose out betting amount. As a result, our balance that is $100 will be decrease by the betting amount.
In the other hand, our choice matches with the result, how many matches, how many times our score will be multiplied.
For example, we choose $10 for 'Gourd' and after hitting 'Roll' button, the result is 'Gourd', 'Fish', 'Gourd', we will earn $10x2 that is $20 because we have got 2 
gourds in result.
After each roll, the balance will be updated and remain new balance for the next roll.

When is game over?
That is when our balance is 'zero'. A message will print out to let us know game is over. Also, a button 'Play again' will show at the same time. 
By clicking on 'Play again' button, our game will restart.
