import os
import re

from dotenv import load_dotenv
from flask import Flask, request
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
import requests

import food_theory.blocks
import meow

load_dotenv()

COUNTRY_SONG_URL = 'https://y7j5u0qt6f.execute-api.us-east-1.amazonaws.com/dev'
DM_CHANNEL = 'UG9RLD8FL'
FOOD_THEORY_URL = 'https://foodtheory.tkinvt.com/categorize'

app = Flask(__name__)

bolt_app = App(
    token=os.getenv("BOT_TOKEN"),
    signing_secret=os.getenv("SIGNING_SECRET")
)

handler = SlackRequestHandler(bolt_app)


# Slack Bolt Handlers
@bolt_app.action('food_options')
def handle_food_options(ack):
    ack()


@bolt_app.action('submit_food')
def submit_food(body, ack, respond):
    ack()

    category = body['state']['values']['options']['food_options']['selected_option']['value']
    text = body['message']['text']
    # The best way I can find of passing the queried food is parsing the text and searching and transforming it
    food_name = re.search("\*.*\*", text)
    food_name = food_name.group()
    food_name = food_name.replace('*', '')
    food_name = food_name.lower()

    respond(delete_original=True)
    requests.post(FOOD_THEORY_URL, data={'food': food_name, 'category': category})


@bolt_app.action('cancel_food')
def cancel_food(ack, respond):
    ack()
    respond(delete_original=True)


@bolt_app.command('/country-song')
def country_song(ack, respond):
    ack('Cooking up a song...')
    song = requests.get(COUNTRY_SONG_URL)
    respond(f"```{song.text}```")


@bolt_app.command('/oscar')
def oscar(ack, respond):
    ack()
    respond(meow.meow())


# Flask Routes
@app.route('/slack/events', methods=['POST'])
def slack_events():
    return handler.handle(request)


@app.route('/food', methods=['POST'])
def food():
    food_name = request.form['food']
    blocks = food_theory.blocks.food_question(food_name)
    bolt_app.client.chat_postMessage(channel=DM_CHANNEL, blocks=blocks, text=f"Categorize *{food_name}*")
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
