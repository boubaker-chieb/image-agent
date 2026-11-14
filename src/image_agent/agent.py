from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

from image_agent.generate_image import GenerateImage

from dotenv import load_dotenv

load_dotenv()


def run_agent(request: str, use_case: GenerateImage) -> str:
    @tool(return_direct=True)
    def generate_img(prompt:str) -> str:
        """Generate an png image from a visual text description and return it's path"""
        return str(use_case.execute(prompt))
    
    model = ChatOpenAI(
        model="gpt-5-mini",
        model_kwargs={"parallel_tool_calls": False}
    )

    tools = [generate_img]

    system_prompt=(
            "You help users design images. When they ask to create an image, "
            "call generate_image with a clear description that preserves their "
            "constraints. When they ask only for ideas or feedback, answer in text."
        ),

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt
    )

    result = agent.invoke({"messages": [{"role": "user", "content": request}]})

    return result["messages"][-1].text