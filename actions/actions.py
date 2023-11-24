# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from PyMovieDb import IMDB


class ActionFetchMovieInfo(Action):
    def name(self) -> Text:
        return "action_fetch_movie_info"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        movie_name = tracker.get_slot("movie")
        imdb = IMDB()
        movie_info = imdb.get_by_name(movie_name)

        # You can customize the response based on the movie_info received from IMDb API
        response = f"Here is the information about {movie_name}: {movie_info}"
        dispatcher.utter_message(response, movie_info=movie_info)

        return []
