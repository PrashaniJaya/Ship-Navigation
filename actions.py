# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from numpy import genfromtxt
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
from gensim.models.doc2vec import Doc2Vec
from gensim.parsing.preprocessing import preprocess_string
import requests


class Shipinformation(Action):

    def name(self) -> Text:
        return "action_get_shipdata"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ship = tracker.get_slot('shipname')

        print(ship)

        #file1 = open("C:/Users/prash/Documents/shipdata.txt", "r+")
        file1 = open("C:/Users/prash/Documents/shipdata.txt", "r+")
        # Reading from file
        # print(file1.readlines())
        data = genfromtxt(file1, delimiter=',', dtype=str)
        #print(data[0][0])

        if(data[1][1] != 'Path01'):
            dispatcher.utter_message(template="utter_unimportant")

        elif (data[2][1] == 'Path01'):
            if (data[2][2] == 'Sweden'):
                # response = "We are on the same route to same destination. An alternate path is found that will take 2 additional hours to destination"
                dispatcher.utter_message(template="utter_problemalternate1")

        elif (data[3][1] != 'Path01'):
            if (data[3][2] == 'Sweden'):
                response = "Thank you. We are taking a different path even if the destination is the same"
                dispatcher.utter_message(text=response)
        else:
            response = "We are not in same path. This message is disregarded as it is unimportant to our path"
            dispatcher.utter_message(template="utter_unimportant")

        file1.close()
        return[]