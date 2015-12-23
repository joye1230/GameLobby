# event flags
INVALID_FLAG = 'invalid'
LOGIN = 'login'
LOGOUT = 'logout'
ACCOUNT = 'account'
CHAT_ALL = 'chatAll'
CHAT_ROOM = 'chatRoom'
CHAT = 'chat'
CREATE_ROOM = 'cr'
ENTER_ROOM = 'er'
FIND_ROOMS = 'find'
QUIT_ROOM = 'qt'
GAME = '21game'
READY_START = 'start'
MSG = 'msg'

# responses
INVALID_COMMAND = 'Invalid command!'
ALREADY_ONLINE = 'Already online.'
SUCCESS_LOGIN = 'Successful login. Now you\'ve in the 21 points game lobby.'
SUCCESS_LOGOUT = 'Successful logout.'
INCORRECT_PWD = 'Incorrect user name or password!'
CONFIRM_PWD = 'The passwords are not the same.'
EXIST_ACCOUNT = 'The user name has already exists.'
NEW_ACCOUNT = 'New account created. Now login again.'
SUCCESS_CROOM = 'Successful creating room! Now you can play game in the room.\n' \
                'You can chat with others or input "start" to wait for the game, it\'ll start half-hourly...'
FAIL_CROOM = 'The room already exists! Please change the room name.'
SUCCESS_EROOM = 'Successful entering room! Now you can play game in the room.\n' \
                'You can chat with others or input "start" to wait for the game, it\'ll start half-hourly...'
FAIL_EROOM = 'No such room exists!'
SUCCESS_QROOM = 'Successful quiting room!'
FAIL_QROOM = 'You are not in this room!'
CURRENT_ROOMS = 'Current Rooms:'
DISMISS_ROOM = 'The room has been dismissed!'
WIN_GAME = 'Congratulations! You are the winner!'
LOSE_GAME = 'Sorry! You lose the game.'
START_GAME = 'Game starts! There are four numbers below,\n' \
             'by using "+ - * / ( )" to get the result be close to 21.\n' \
             'please write the answer like "21game ANSWER" in 15s.'
READY_GAME = 'Ready for game. Waiting for others...'
CONTINUE_GAME = 'Please wait, it\'ll start half-hourly...'
WRONG_EXPRESSION = 'Wrong expression!'
DEALED_MSG = 'Already done.'
CHAT_MSG = 'Chatting...'
NO_MSG = 'No message now.'

# database
DATABASE = 'database.dat'
