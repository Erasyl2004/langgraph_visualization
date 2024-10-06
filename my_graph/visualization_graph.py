import os
from dotenv import load_dotenv
from langgraph.graph import END, START, StateGraph
import asyncio
from my_graph.prompt_solver_compile import build_the_graph_with_solver_prompt

load_dotenv()

workflow = build_the_graph_with_solver_prompt()

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