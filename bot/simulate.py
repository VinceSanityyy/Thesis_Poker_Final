from api.game import start_poker, setup_config

from bot.callbot import CallBot
from bot.databloggerbot import DataBloggerBot
import numpy as np

if __name__ == '__main__':
    blogger_bot = DataBloggerBot()

    # The stack log contains the stacks of the Data Blogger bot after each game (the initial stack is 100)
    stack_log = []
    for round in range(1000):
        p1, p2 = blogger_bot, CallBot()

        config = setup_config(max_round=5, initial_stack=100, small_blind_amount=5)
        config.register_player(name="Bot 1 ", algorithm=p1)
        config.register_player(name="Bot 2", algorithm=p2)
        game_result = start_poker(config, verbose=1)

        stack_log.append([player['stack'] for player in game_result['players'] if player['uuid'] == blogger_bot.uuid])
        print('Avg. stack:', '%d' % (int(np.mean(stack_log))))