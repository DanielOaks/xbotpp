# -*- coding: utf-8 -*-
# vim: noai:ts=4:sw=4:expandtab:syntax=python

from xbotpp.modules import Module

class help(Module):
    def __init__(self):
        Module.__init__(self)

    def action(self, bot, event, args, buf):
        bot_commands = []

        for module in enumerate(self.bot.modules.modules):
            bot_commands.append(module[1])

        return "Available commands: %s" % ", ".join(bot_commands)
