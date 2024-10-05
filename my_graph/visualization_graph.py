import os
from dotenv import load_dotenv
from langgraph.graph import END, START, StateGraph
from my_graph.utils.state import MoodClassifierState
from my_graph.utils.nodes.prompt_executer_node import mood_classifier_prompt_executer_node
from my_graph.utils.nodes.mood_response_executer_nodes import (
    mood_happy_executer_node,
    mood_angry_executer_node,
    mood_uncertain_executer_node,
    mood_sad_executer_node,
    determine_mood,
    end_and_return_state
)
import asyncio

load_dotenv()

workflow = StateGraph(MoodClassifierState)

workflow.add_node("MoodClassifier", mood_classifier_prompt_executer_node)
workflow.add_node("MoodHappyExecuter", mood_happy_executer_node)
workflow.add_node("MoodAngryExecuter", mood_angry_executer_node)
workflow.add_node("MoodUncertainExecuter", mood_uncertain_executer_node)
# workflow.add_node("MoodSadExecuter", mood_sad_executer_node)
workflow.add_node("EndAndReturnState", end_and_return_state)

workflow.add_edge(START, "MoodClassifier")

workflow.add_conditional_edges(
    "MoodClassifier",
    determine_mood,
    {
        "MoodHappyExecuter": "MoodHappyExecuter",
        "MoodAngryExecuter": "MoodAngryExecuter",
        "MoodUncertainExecuter": "MoodUncertainExecuter",
    },
)

workflow.add_edge("MoodHappyExecuter", "EndAndReturnState")
workflow.add_edge("MoodAngryExecuter", "EndAndReturnState")
workflow.add_edge("MoodUncertainExecuter", "EndAndReturnState")
workflow.add_edge("EndAndReturnState", END)


graph = workflow.compile()



# graph_image = graph.get_graph(xray=True).draw_mermaid_png()
# with open("graph_output.png", "wb") as f:
#     f.write(graph_image)

# inputs = MoodClassifierState(
#     message="I am so angry i want to fight!!!!!!!",
# )

# async def run_workflow():
#     config = {"recursion_limit": 50}
#     response = inputs
#     async for event in graph.astream(inputs, config=config):
#         for k, v in event.items():
#             if k != "__end__":
#                 if k == "EndAndReturnState":
#                     response = v
#     print(response)
# asyncio.run(run_workflow())