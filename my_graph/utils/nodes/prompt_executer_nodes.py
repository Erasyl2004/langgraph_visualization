import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langfuse import Langfuse
from langfuse.callback import CallbackHandler
from dotenv import load_dotenv
from my_graph.utils.state import MoodClassifierState
import logging

load_dotenv()

os.environ["LANGFUSE_PUBLIC_KEY"] = os.getenv("LANGFUSE_PUBLIC_KEY")
os.environ["LANGFUSE_SECRET_KEY"] = os.getenv("LANGFUSE_SECRET_KEY")
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"
os.environ["OPENAI_API_KEY"] = os.getenv("openai_api_key")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

langfuse = Langfuse()
langfuse_callback_handler = CallbackHandler()

class MoodClassifierResponse(BaseModel):
    mood: Literal["happy", "angry", "uncertain"] = Field(
        description="The emotional state determined from the input message. Must be one of: 'happy', 'angry', or 'uncertain'."
    )

async def mood_classifier_prompt_executer_node(state: MoodClassifierState) -> MoodClassifierState:
    langfuse_prompt = langfuse.get_prompt("mood_classifier_prompt")
    langchain_prompt = ChatPromptTemplate.from_template(langfuse_prompt.get_langchain_prompt())

    model = ChatOpenAI(
        model=langfuse_prompt.config["model"],
        temperature=langfuse_prompt.config["temperature"],
    ).with_structured_output(MoodClassifierResponse)

    chain = langchain_prompt | model
    response = chain.invoke(input={"message": state["message"]}, config={"callbacks": [langfuse_callback_handler]})

    logger.info(f"prompt response:\n{response}")

    return {"mood": response.mood}

class MessageTransformerResponse(BaseModel):
    transformed_message: str = Field(
        description="The modified message adjusted to fit one of the specific moods: 'happy', 'angry', or 'sad'."
    )

async def message_transformer_prompt_executer_node(state: MoodClassifierState) -> MoodClassifierState:
    langfuse_prompt = langfuse.get_prompt("message_transformer_prompt")
    langchain_prompt = ChatPromptTemplate.from_template(langfuse_prompt.get_langchain_prompt())

    model = ChatOpenAI(
        model=langfuse_prompt.config["model"],
        temperature=langfuse_prompt.config["temperature"],
    ).with_structured_output(MessageTransformerResponse)

    chain = langchain_prompt | model
    response = chain.invoke(input={"message": state["message"]}, config={"callbacks": [langfuse_callback_handler]})

    logger.info(f"prompt response:\n{response}")

    return {"message": response.transformed_message}










# на вход дается какое то рандомное сообщение задача промпта определить на его основе при каком настроений оно было написанно на выходе может быть только три варианта ответа: happy, angry, sad, uncertain. У промпта будет только один input variable: message