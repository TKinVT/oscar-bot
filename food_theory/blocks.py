import json


def food_question(food):
    blocks = [
        {"type": "section",
         "block_id": "text",
         "text": {
             "type": "mrkdwn",
             "text": f"Someone has submitted *{food.upper()}* to be categorized"
         }},
        {"type": "actions",
         "block_id": "options",
         "elements": [{
             "type": "static_select",
             "placeholder": {
                 "type": "plain_text",
                 "text": "Select a category",
                 "emoji": True
             },
             "action_id": "food_options",
             "options": [
                 {"text": {
                     "type": "plain_text",
                     "text": "Atomic Food",
                     "emoji": True
                 },
                     "value": "atomic food"
                 },
                 {"text": {
                     "type": "plain_text",
                     "text": "Salad",
                     "emoji": True
                 },
                     "value": "salad"
                 },
                 {"text": {
                     "type": "plain_text",
                     "text": "Sandwich",
                     "emoji": True
                 },
                     "value": "sandwich"
                 },
                 {"text": {
                     "type": "plain_text",
                     "text": "Soup",
                     "emoji": True
                 },
                     "value": "soup"
                 },
                 {"text": {
                     "type": "plain_text",
                     "text": "Not a food",
                     "emoji": True
                 },
                     "value": "not food"
                 }
             ]
         }]},
        {"type": "actions",
         "elements": [
             {"type": "button",
              "text": {
                  "type": "plain_text",
                  "emoji": True,
                  "text": "Submit"
              },
              "style": "primary",
              "value": "submit",
              "action_id": "submit_food"},
             {"type": "button",
              "text": {
                  "type": "plain_text",
                  "emoji": True,
                  "text": "Cancel"
              },
              "style": "danger",
              "value": "cancel",
              "action_id": "cancel_food"}
         ]}
    ]

    blocks = json.dumps(blocks)

    return blocks
