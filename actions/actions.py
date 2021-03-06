# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
from openpyxl import load_workbook
from datetime import datetime


class ActionFillUnanswered(Action):

    def name(self) -> Text:
        return "fill_unanswered_sheet"

    async def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        path = r"C:\Users\a858082\PycharmProjects\RasaChatBot\assets\Unanswered_questions.xlsx"
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        new_row_data = [dt_string, tracker.latest_message['text']]
        wb = load_workbook(path)
        ws = wb.worksheets[0]
        ws.append(new_row_data)
        wb.save(path)
        return []
