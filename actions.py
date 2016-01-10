#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex8955'


class action(object):
    """base class for all actions"""
    def __init__(self, name, desc, helpTxt, effect = None):
        self.name = name
        self. desc = desc
        self.helpTxt = helpTxt
        self.effect = effect

    def __str__(self):
        if self.name == "help":
            return self.desc
        else:
            return self.desc + "See help {} for more details.".format(self.name)

class help(action):
    def __init__(self, topic):
        action.__init__(
            name = "help",
            desc = "Display help for a topic, or the general help file.",
            helpTxt = """The basic commands in Pygame are:
                help <topic>: display help on a specific command or topic. help with no argument displays this help file.
                [enter] <#>: enter the door associated with the number. The word enter is optional. ex: enter 1 OR 1
                """)



def main():
    print help()


if __name__ == "__main__":
    main()