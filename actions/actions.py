# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

from save_gsheet import GsheetDataStore

class ValidateMitaForm(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_mita_form"

    async def validate_confirm_exercise(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Validate if exercise has been performed."""

        if value:
            return {"confirm_exercise": True}
        else:
            return {"exercise": "None", "confirm_exercise": False }

class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        GsheetDataStore(tracker.get_slot("user_name"),
            tracker.get_slot("user_age"),
            tracker.get_slot("user_email"),
            tracker.get_slot("user_run_hist"),
            tracker.get_slot("confirm_exercise"),
            tracker.get_slot("exercise"),
            tracker.get_slot("user_sleep"),
            tracker.get_slot("stress"))
        dispatcher.utter_message(text="Data Stored Successfully.")

        return []