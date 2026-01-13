import pandas as pd
import pandasai as pai
from pandasai import Agent
from pandasai_litellm.litellm import LiteLLM
import os

llm = LiteLLM(model="gpt-4.1-mini", api_key=os.getenv("OPENAI_API_KEY"))
pai.config.set({"llm": llm})

df = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'revenue': [45000, 52000, 48000, 61000, 58000],
    'expenses': [32000, 38000, 35000, 42000, 40000]
})

agent = Agent(df)

response = agent.chat(
    "Create a bar chart showing revenue and expenses by month. "
    "Save the plot to a file and return only the file path."
)

print(response)