import webbrowser
from flask import Flask, render_template, request, jsonify
from tokenizer import Tokenizer
from normalization import Normalizer
from tagger import Tagger
from filesearch import FileSearch
from openmedia import OpenMedia
import gui

from weather import WeatherC


class Brain :
    def __init__(self,command):
        self.command = command
        # from 0  =>> 15 is verb for search and find
        # from 16 =>> 21 is verb for open
        self.actions = ["search", "find", "view", "reach", "detect", "get", "catch", "explore"
            , "achieve", "obtain", "pass", "check", "reveal", "expose", "observe"
            , "show", "see", "listen", "hear", "open", "watch"
            , "arise", "awaken", "call", "consciousness", "get up", "stir", "wake", "wake up"]

        self.tokens = Tokenizer().tokenize(self.command)

        self.action = None

        self.fileName = None
        # -----------------------------------<<Variable>>--------------------------------------------
    def brn(self):

        tagSentence = Tagger().tag(self.tokens)

        for counter in range(len(tagSentence)):
            # if tagSentence[counter][1] == 'VB' or tagSentence[counter][0] in self.actions:

            if tagSentence[counter][0] in self.actions:

                action = tagSentence[counter][0]


            elif tagSentence[counter][1] == 'NN':
                fileName = tagSentence[counter][0]

        normlizeAction = Normalizer().snowBallStemmer(action)



        if normlizeAction in self.actions:
            filePath = FileSearch().search(fileName)  # return list of file shared the same name

            if normlizeAction in self.actions[:15]:
                # for search about folder or file
                OpenMedia().openFile(filePath[0].split("//")[0])

            if normlizeAction in self.actions[15:21]:

                OpenMedia().openFile(filePath[0])




        else:
            pass
            # return "can you explain more"

# Brain("i wanna open workout").brn()