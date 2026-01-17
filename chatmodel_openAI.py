from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize Model
model = ChatOpenAI(model='gpt-4o-mini', temperature=0.7)

# 2. Define a Prompt Template (Professional way to handle inputs)
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert Electronics Engineer. Suggest the best components for the given project requirements."),
    ("user", "I am building a {project_name}. My constraints are: {constraints}. What components should I use?")
])

# 3. Create a Chain (The heart of LangChain)
chain = prompt_template | model

# 4. Run the Chain
result = chain.invoke({
    "project_name": "Raspbrry Pi based ADAS system",
    "constraints": "low power consumption and WiFi connectivity"
})

print(result.content)
