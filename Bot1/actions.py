# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



data = {
    "Pakistan":"South Asia",
    "Turkey":"West Asia",
    "Iran":"Middle East",
    "Russia":"South Asia"
}

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        val = tracker.get_slot("country")
        dt = data.get(val)
        if val == "":
            output = "No Country Provided"
        else:
            output = "The Location of Country in Asia is {}".format(dt)

        dispatcher.utter_message(text=output)

        return []
