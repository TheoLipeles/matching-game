from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time, random


class Instructions(Page):
    def vars_for_template(self):
        return {
            'participant_vars': str(self.participant.vars)
        }
    pass

class Selection(Page):
    form_model = 'player'
    form_fields = ['attention_check', 'game_3_switch']
    def before_next_page(self):
        self.participant.vars['game_3_switch'] = self.player.game_3_switch
        self.participant.vars['game_3_payment'] = random.choice(Constants.round_values)
        self.participant.vars['game_3_piece_rate'] = float(self.participant.vars['game_3_payment']) < float(self.participant.vars['game_3_switch'])
    def vars_for_template(self):
        return {
            'participant_vars': str(self.participant.vars)
        }

class Selection_Results(Page):
    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 90
    def vars_for_template(self):
        return {
            'participant_vars': str(self.participant.vars),
            'value': self.participant.vars['game_3_payment'],
            'game_1': self.participant.vars['game_3_piece_rate']
        }


page_sequence = [Instructions, Selection, Selection_Results]