# -*- coding: utf-8 -*-
# vim: noai:ts=4:sw=4:expandtab:syntax=python

class BotIO:
    def __init__(self, bot):
        self.bot = bot

    def read(self, client, event):
        for i, elem in enumerate(self.bot.modules.modules['privmsg']):
            self.bot.modules.modules['privmsg'][elem][0](self.bot, event, event.arguments[0].split(), "")

        if event.arguments[0].startswith(self.bot.prefix):
            args = event.arguments[0][1:]
            commands = [s.strip() for s in args.split("|")]
            buf = ""

            for command in commands:
                cmdargs = [s.strip() for s in command.split()]
                command = cmdargs[0]
                cmdargs = cmdargs[1:]

                if self.bot.modules.modules['command'][command][1] == "admin":
                    if event.source.nick.lower() not in self.bot.config.get("bot", "owner").lower():
                        buf = "%s: Not authorized." % command
                        continue

                buf = self.bot.modules.modules['command'][command][0](self.bot, event, cmdargs, buf)

            self.bot._log("%s -> %s" % (event.target, buf), "out")
            for line in buf.split("\n"):
                client.privmsg(event.target, line)

