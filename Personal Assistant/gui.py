from flask import Flask, render_template, request, jsonify

import webbrowser
from flask import Flask, render_template, request, jsonify
from geotext import GeoText

from tokenizer import Tokenizer
from normalization import Normalizer
from tagger import Tagger
from filesearch import FileSearch
from openmedia import OpenMedia
from QuickServiceGui import QuickService
import gui

from weather import WeatherC
import os


app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('chat.html')


def weatherFunction(phrase):
	placeOfWeather = []
	text = phrase.title()
	print(text)
	for word in text.split():
		cities = GeoText(word).cities
		countries = GeoText(word).countries
		if cities != []:
			placeOfWeather.append(cities[0])

		if countries != []:
			placeOfWeather.append(countries[0])
	if 'Of' in placeOfWeather:
		placeOfWeather.remove('Of')
	return placeOfWeather


def brain(command):
	response = ""
	command = command
	# from 0  =>> 15 is verb for search and find
	# from 16 =>> 21 is verb for open
	actions = ["search", "find", "view", "reach", "detect", "get", "catch", "explore"
		, "achieve", "obtain", "pass", "check", "reveal", "expose", "observe"
		, "show", "see", "listen", "hear", "open", "watch"
		, "arise", "awaken", "call", "consciousness", "get up", "stir", "wake", "wake up"]

	tokens = Tokenizer().tokenize(command)

	# call weather function if there is weather word and country or city name
	citiesORcountries = weatherFunction(command)
	if 'weather' in command.split() and citiesORcountries != []:
		return 'the weather in ' + citiesORcountries[0] + ' is ' + WeatherC().weatherForecast(citiesORcountries[0]) + ' today'


	action = None

	fileName = None
	# -----------------------------------<<Variable>>--------------------------------------------
	tagSentence = Tagger().tag(tokens)

	for counter in range(len(tagSentence)):
		# if tagSentence[counter][1] == 'VB' or tagSentence[counter][0] in self.actions:

		if tagSentence[counter][0] in actions:

			action = tagSentence[counter][0]


		elif tagSentence[counter][1] == 'NN':
			fileName = tagSentence[counter][0]

	normlizeAction = Normalizer().snowBallStemmer(action)


	if normlizeAction in actions:
		filePath = FileSearch().search(fileName)  # return list of file shared the same name


		if normlizeAction in actions[:15]:
			# for search about folder or file
			OpenMedia().openFile(filePath[0].split("//")[0])
			response = "i hope you're satisfied with our service"
			return response

		if normlizeAction in actions[15:21]:
			#if he
			if normlizeAction in ['listen','hear','watch'] and filePath[0].split('.')[1] !=['mp3','mp4','mkv']:

				pass
			OpenMedia().openFile(filePath[0])


# --------------------------------<<gui manipulate>>--------------------------



@app.route("/ask", methods=['POST'])
def ask():

	message = str(request.form['messageText'])
# ===========================================================================================

# ===========================================================================================


	if message == "quit":
		exit()

	elif message in ["QS","quick service"]:

		return jsonify({'status': 'OK', 'answer': QuickService().QS() })
	# elif message==

	else:
		# reponse write here and thanks
		bot_response = "wait"
		# print bot_response
		return jsonify({'status': 'OK', 'answer': brain(message)})






if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5006, debug=True)
