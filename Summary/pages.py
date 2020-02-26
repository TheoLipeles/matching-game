from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random, json


payment_values = [0.50,0.75,1.00,1.25,1.50,1.75,2.00,2.25,2.50]

class Summary(Page):
    def vars_for_template(self):
        payment_game = random.randint(1,5)
        self.participant.vars['payment_game'] = payment_game
        self.participant.vars['game_4_score'] = self.participant.vars['game_1_score']
        score = 0
        scheme = ''
        payment = 0
        payment_value = 0.5
        win = 1

        score = self.participant.vars['game_%d_score' % payment_game]
        if payment_game == 1:
            scheme = 'Piece Rate'
        elif payment_game == 2:
            scheme = 'Tournament'
            payment_value = random.choice(payment_values)
        elif payment_game == 3 or payment_game == 4:
            payment_value = float(self.participant.vars['game_%d_value' % payment_game])
            if float(self.participant.vars['game_%d_value' % payment_game]) < float(self.participant.vars['game_%d_switch' % payment_game]):
                scheme = 'Piece Rate'
            else:
                scheme = 'Tournament'
        elif payment_game == 5:
            scheme = 'Tournament'
            payment_value = 0.04 * json.loads(self.participant.vars['game_5_values'].replace("'",'"'))['Points_B']
            payment = 0.01 * json.loads(self.participant.vars['game_5_values'].replace("'",'"'))['Points_A'] * score
        if scheme == 'Tournament':
            for player in self.player.get_others_in_group():
                player_score = 0
                try:
                    player_score = player.participant.vars['game_%d_score' % payment_game]
                except:
                    player_score = random.randint(2,8)
                if player_score > score:
                    win = 0
                    break
                if player_score == score:
                    win += 1
            if win:
                win = random.random() < (1/win) # Randomly select on tie
        payment += payment_value * score * win
        payout = payment + 2
        return {
            'payment_game': payment_game,
            'scheme': scheme,
            'score': score,
            'win': win,
            'payment': payment,
            'payout': payout,
            'payment_value': payment_value,
            'participant_vars': str(self.participant.vars)
        }


page_sequence = [Summary]
