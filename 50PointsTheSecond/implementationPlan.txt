1. Set up News API

Sign up for a free account at https://newsapi.org/ and obtain your API key.
Install the News API Python library:
 
pip install newsapi-python
Use code with caution
2. Retrieve News Data

 
from newsapi import NewsApiClient

# Replace with your API key
newsapi = NewsApiClient(api_key='YOUR_API_KEY')

# Fetch top headlines (customize query as needed)
top_headlines = newsapi.get_top_headlines(q='technology', language='en')

# Extract relevant information
articles = top_headlines['articles']
news_data = []
for article in articles:
    news_data.append({
        'title': article['title'],
        'description': article['description'],
        'url': article['url'],
        'source': article['source']['name']
    })
Use code with caution
3. Install AutoGen

 
pip install autogen
Use code with caution
4. Set up AutoGen Group Chat

 
from autogen import UserProxyAgent, AssistantAgent, GroupChat, GroupChatManager

config_list = [
    {"model": "gpt-3.5-turbo", "api_key": "YOUR_OPENAI_API_KEY"},
]  # Add more configs if needed

# Initialize agents
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "autogen"})
critic = AssistantAgent("critic", llm_config={"temperature": 0.1})
writer = AssistantAgent("writer")
planner = AssistantAgent("planner", llm_config={"temperature": 0.1})

# Create group chat
groupchat = GroupChat(agents=[user_proxy, critic, writer, planner], messages=[], max_round=12)
manager = GroupChatManager(groupchat=groupchat, llm_configs=config_list)
Use code with caution
5. Define User Request

 
user_request = (
    "Write a concise and informative news article summarizing the following information:\n\n"
    + "\n".join([f"**{item['title']}** ({item['source']}): {item['description']}" for item in news_data])
    + "\n\nEnsure the article is well-structured, objective, and covers the key points from the provided news."
)
Use code with caution
6. Initiate Conversation

 
user_proxy.initiate_chat(manager, message=user_request)
Use code with caution
7. Retrieve the Article

The final summarized article will be present in the groupchat.messages list. Extract and display it.
