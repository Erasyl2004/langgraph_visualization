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
    The mood is classified as "uncertain" because the message lacks enough clear emotional cues to determine a specific state.
    This can occur when the message is neutral, ambiguous, or does not provide sufficient information for a classification as "happy," "angry," or another defined mood.
    Messages in this category may express uncertainty, vagueness, or hesitancy, often containing questions or neutral statements.
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