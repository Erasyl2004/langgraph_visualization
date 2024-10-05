import os
from dotenv import load_dotenv
from typing import Annotated, Literal, TypedDict
from pydantic import BaseModel, Field
from my_graph.utils.state import MoodClassifierState

async def mood_happy_executer_node(state: MoodClassifierState) -> MoodClassifierState:
    happy_based_description = """
    The person is experiencing positive emotions, feeling cheerful, and likely satisfied with the current situation. 
    Their message may contain optimistic, joyful, or friendly expressions.
    """

    return {"mood_based_description": happy_based_description}

async def mood_angry_executer_node(state: MoodClassifierState) -> MoodClassifierState:
    angry_based_description = """
    The person is feeling irritated or angry. 
    Their message may include aggressive, harsh, or rude language, indicating frustration or dissatisfaction.
    """

    return {"mood_based_description": angry_based_description}

async def mood_uncertain_executer_node(state: MoodClassifierState) -> MoodClassifierState:
    uncertain_based_description = """
    The person is unsure or experiencing doubt.
    Their message may be vague, contain questions, hesitations, or indicate uncertainty in their thoughts or actions.
    """

    return {"mood_based_description": uncertain_based_description}

async def mood_sad_executer_node(state: MoodClassifierState) -> MoodClassifierState:
    sad_based_description = """
    The person is feeling sadness or sorrow.
    Their message may contain expressions of loss, disappointment, or regret, indicating an emotional downturn.
    """

    return {"mood_based_description": sad_based_description}

async def determine_mood(state: MoodClassifierState) -> str:
    return state["mood"]

async def end_and_return_state(state: MoodClassifierState):
    return state