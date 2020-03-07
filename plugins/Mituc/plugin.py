###
# Copyright (c) 2020, George-Cristian Bîrzan
# All rights reserved.
#
#
###
import pathlib
import random
import re

import markovify
from supybot import utils, plugins, ircutils, callbacks, world
from supybot.commands import *
from supybot.ircmsgs import privmsg

try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Mituc')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

import supybot.schedule as schedule

class Mituc(callbacks.Plugin):
    def __init__(self, irc):
        super().__init__(irc)
        self.network = irc.network
        self.schedule = schedule.schedule
        current_path = pathlib.Path(__file__).parent.absolute()
        with open(current_path / "corpus.txt") as f:
            text = f.read()

        self.text_model = markovify.NewlineText(text, state_size=3)
        try:
            schedule.removeEvent('mituc')
        except:
            pass
        schedule.addPeriodicEvent(self.random_mituc, 120, name='mituc')

    def random_mituc(self):
        try:
            rand_value = random.random()
            print(rand_value)
            if rand_value > .99:
                irc_obj = world.getIrc(self.network)
                num_sentences = random.randint(1, 3)
                for x in range(num_sentences + 1):
                    sentence = self.generate_mituc()
                    irc_obj.sendMsg(privmsg('#mumu', sentence))
        except Exception as e:
            print(e)

    def generate_mituc(self, text=None):
        for x in range(2000):
            sentence = self.text_model.make_sentence(tries=150)
            sentence = re.sub('[^ ]*?:? *', '', sentence)

            match = True

            if text:
                lower_sentence = sentence.lower()
                words = text.lower().split()
                for word in words:
                    if word not in sentence:
                        match = False
                        break
            if match:
                return sentence

    @wrap([optional('text', )])
    def mituc(self, irc, msg, args, text):
        """mituc"""
        sentence = self.generate_mituc(text)
        if sentence:
            irc.reply(sentence, prefixNick=False)
        else:
            irc.reply("Could not generate a Mituc")



Class = Mituc


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
