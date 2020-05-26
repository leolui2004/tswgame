# Try to write a Tower of the Sorcerer game using only Python Django and Dash
This is my second project, I tried to use purely Python Django and Dash (django-plotly-dash) to create a game like Tower of the Sorcerer. To be more precise, it is a kind of template rather than a game. As I mainly wants to try if all of the game functions can be achieved on Dash.

Feel free to leave any comments, I just learned Python for two months and I am now concentrating on data analysis and web presentation.

## Features
* By clicking button(image) on the screen to move, select, use items, save, load
![image](https://github.com/leolui2004/tswgame/blob/master/pic/mota1.gif)

* When entering selection mode, other buttons are hided (easier for processing game logic)
![image](https://github.com/leolui2004/tswgame/blob/master/pic/mota2.gif)

* Items like teleport, pickaxe(destroy a wooden wall), book of monster(check status of monster on that floor)
![image](https://github.com/leolui2004/tswgame/blob/master/pic/mota3.png)
![image](https://github.com/leolui2004/tswgame/blob/master/pic/mota4.png)

* Save and load game data(stored as a kind of variable)
![image](https://github.com/leolui2004/tswgame/blob/master/pic/mota5.png)

## Methodology
### Data and game logic
Mainly using dictionary to store game data, it would be easier for code writing if using dataframe, but it is not locally supported by Python, thus dictionary is used. For a bigger project, database should be more suitable.

Game data are stored as dictionary and set as read only. Player data are stored through dictionary update during the game, and a separate dictionary is for save data.

The most tricky part may be the button and callback, Dash cannot set different callbacks sharing same output, thus all inputs and outputs are in one callback function. To distinguish which button is being clicked, variables storing number of click (e.g. n_click_store) of different buttons are set. When a button was clicked,  the n_click_input of that specific button would be larger than the n_click_store by 1, after that the n_click_store is set to equal n_click_input thus next time when other buttons are clicked, this button will not be triggered.

### Display
All text and images except buttons are appended to a list and then wrapped in a Div Children and return to the layout. For Dash, because buttons need to be defined first otherwise the callback function will show an error, thus buttons are first defined but some of them are hided using CSS(display: ‘none’), and change its visibility when necessary.

Maps, monsters, items or other stuff on the map are all tiles, the tiles are arranged by each having an ID which can be recognized by CSS style written on HTML file.

As said above because all inputs and outputs are in one callback function, during the game there is a chance that some buttons have been clicked accidentally(e.g. clicked on a save button where the game is asking you to select to pay gold for upgrade). Errors can be prevented by setting IF statement to determine each time but as the number of button grows that would be extremely troublesome, a better method is to make some buttons hidden when they are not necessary for user to click, it is also more easy for user to understand what they should do at that moment.

## Difficulties
1 Dash does not support keypress event locally - there may be some tricky method (e.g. a hidden textbox act as an input) but actually it can still be achieved by simply adding jQuery
2 Dash does not support time interval event locally - Time interval event is important for displaying things like battle scene, again there may be some tricky method but that would be somehow out of the scope for this project

### Why I use Dash
There is also a module named Pygame which should be more suitable for creating a mini game, however as I am concentrating on learning data analysis and web presentation. I would like to use Dash to create a game as to explore deeper on how Dash can interact with user. At the end it is only a kind of experiment, I personally do not think that Dash is efficient for creating a game.
