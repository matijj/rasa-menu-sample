# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher


class ActionHandleOptions(Action):
    def name(self) -> Text:
        return "action_handle_options"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        # The default value is main
        current_menu = tracker.get_slot("current_menu")

        # If the current menu is not set, we assume that the user is in the main menu
        if current_menu is None:
            dispatcher.utter_message(text=f"Mmmmm... I don't know what you mean.")
            return [SlotSet("option", None)]

        menuoptions_to_actionname = {
            "main": {
                "A": "utter_info_enterprise",
                "B": ("utter_turn_options", "turn_options"),
                "C": "action_list_people",
            },
            "turn_options": {
                "A": "action_request_turn",
                "B": "action_list_turns",
                "C": "action_delete_turn",
                "D": ("utter_back_to_main_menu", "main"),
            }
        }
        option = tracker.get_slot("option")
        option = option.upper()

        try:
            next_action = menuoptions_to_actionname[current_menu][option]
        except KeyError:
            dispatcher.utter_message(text=f"This option is not available!")
            return [SlotSet("option", None)]

        dispatcher.utter_message(text=f"You've choosen option {option} !")

        if type(next_action) is tuple:
            return [SlotSet('option', None),
                    SlotSet('current_menu', next_action[1]),
                    FollowupAction(name=next_action[0])]
        else:
            return [SlotSet('option', None),
                    SlotSet('current_menu', None),
                    FollowupAction(name=next_action)]

class ActionClearCurrentMenu(Action):
    def name(self):
        return "action_clear_current_menu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Obtén la última intención del usuario
        latest_intent = tracker.latest_message["intent"]["name"]

        # Verifica si la última intención fue "give_option"
        if latest_intent != "give_option":
            # Si la intención no fue "give_option", establece current_menu en None
            return [SlotSet("current_menu", None)]
        else:
            # Si la intención fue "give_option", no hagas nada con current_menu
            return []

class ActionListPeople(Action):
    def name(self):
        return "action_list_people"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text="List of people")

        return []

class ActionRequestTurn(Action):
    def name(self):
        return "action_request_turn"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text="Request Turn")

        return []


class ActionListTurns(Action):
    def name(self):
        return "action_list_turns"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text="List Turns")

        return []

class ActionDeleteTurn(Action):
    def name(self):
        return "action_delete_turn"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text="Delete Turn")

        return []