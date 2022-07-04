**Disclaimer: professionalism has been thrown out the window.**

### Introduction
Hi, My name is Abe, I am taking The CodeCademy Computer Science Course (I am 2 months into it as of writing this) and this is my CS101 Final Project, also literally just Tic Tac Toe.

### Why?
alright, at first, it was going to be a deeply personal project that I wanted to do for my first final project. However, like most people (probably), I realized that what I was going for was far too ambitious and I still have a lot to learn about python before I make a text rpg game of my own that doesn't make me want to pull my hairs out.. so instead, I went for one of the suggested projects on CodeCademy, Tic Tac Toe.. because I thought it'd be easy, ok? I was being lazy! Unfortunately, I also lacked mutliple chromosomes and braincells but that didn't stop me from learning python apparently.

I am warning you, the code is an overcomplicated mess, I don't want you reading it, and I don't want to rewrite anything because it's not that important, and also because I want to have something to laugh at later in my career, shove this in my face 5 years later on my birthday, Databases and Algorithms will already kick my ass after this, I just want to start on those. 

Yes, I know, better to write this file WHILE I am working on the project, but I just never felt like it, and I am only doing it now because it's a habit I need to start working on too. I'll go through every function I made and tell you what it does and why I made it at first.

**In order, Starting With..**
### print_board(board):
the parameter is completely unnecessary, I simply didn't know how to call my variable inside a function without having to add it as a parameter, so forgive me there.
Anyway, I made a local variable that I will use to return a string at the end, in the middle of it all, I wrote in a for loop, every third index will have a new line command after it, and that's it!
That was already overcomplicated, it would have just been easier to write print three times.

### reset_board(board):
as mentioned before above, I didn't know how to call a variable inside a function yadda yadda, I simply wanted to assign the board to its original state again, but because I am an idiot it wasn't done in a simple manner. So guess what? a FOR LOOP happened!
had *i* as my counting variable, and iterated through every index using the count variable, if it wasn't this piece of shit [\_\_] then it will become that piece of shit! What I forgot to account for was stopping the iteration from continuing after count had reached 9, but thankfully python knows how to handle stupid mistakes like these, I personally wish it didn't.

### help_me():
simply prints where your number of choice would go on the board when you play.
it's not a cry for help, I promise.

### place_symbol(symbol):
take the player's input, check if the tile they chose is empty, if not, let them choose again and call the help_me() function, ***BUT*** if so, place it in that spot and let it rot.
You probably noticed the Try/Except statement in there, Python here didn't like empty strings, so I had to put it in with flavor text.

### win_pattern(symbol, num1, num2, num3):
check if the symbol in the three board indexes (num parameters), and if they are, return True! that is it. Written to make writing the next function easier.

### is_it_over(char):
char is symbol, I changed it to that because I realized too late it was easier and faster to write, I'm SORRY!
anyway, I used the win_pattern() function 8 times. two to check the diagonals, three for horizontal, and three for vertical, return true if ANY of them are true.

I wrote it in a different way before, but it threw an 
*Attribute Error: \_\_enter\_\_* at me! The audacity! my code was perfect, yup.. totally.
I still don't understand the error very well as of writing this. which in turn made me rewrite the whole function and win_pattern() was born because of it.
The old function is still in the file but just as a comment, I left it there for you to spit at when you can, you're welcome.

### game_loop(board):
HERE WE GO, BABY FUNCTIONS START WORKING! 
made two local variables which are either true or false, player 1 and player 2, I didn't write any AI since I haven't gone insane yet.
Anyway, WHILE there is still an EMPTY TILE in my BOARD, check whose turn is it, starting with player 1, both players share the same functions inside their respective if statements, which means I should've made a new function to make this process a little more readable, but naw.
So What happens during each player's turn?
1. play until place_symbol() returns True. (take the player's input until they submit to the numbers.)
2. check if is_it_over() (yes.. even on the first 4 turns, which is completely redundant and BAD, one my friends pointed this out to me afterwards, thank you Mr.B)
	1. IF the game IS over, and winning pattern was found for player's specific symbol, return the end() function and print that the player won.
	2. IF not, change the next player to True, then the current Player to False. 
3. if the while loop breaks because the condition is not met, check if the empty tile is no longer in board.. YES, the IF statement was completely UNNECESSARY too and I could literally get rid of it and nothing would change but I'd still keep the last three functions used inside it.

And that's it! Oh that's weird, I haven't talked about the end() function yet, ya know, I was surprised to see it was legal to call a function that didn't exist yet inside a function, and then still be able to write that function after it. So, that's cool.

### end():
ask the player if he wants to play again, if he doesn't exit the game and say bye.
If he does, reset the board and return game_loop(). Done.

### main_menu():
The first thing you see running this disaster, me pointing out the obvious, and greeting you. You get three choices, and you can't use numbers here because I for some reason gave up on that, bad design on my part. 
1. Play calls the game_loop() function and recommends you find a loved one to play with other than yourself.
2. Help just calls the help_me() function and then returns the main_menu() after three seconds, literally the only reason why I imported the sleep function from the time module lmao.
3. Quit exits after saying bye.

### Final Thoughts
At least I finished it, right? I give you the right to shoot me if I ever cause an apocalypse with my code in the future. Or have your favorite ice cream shop explode somehow, which is just another apocalypse in of itself now that I think about it.. regardless, thank you for your time, bye now, don't run my code again.