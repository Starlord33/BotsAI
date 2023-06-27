# import langchain
import os
import config
os.environ["OPENAI_API_KEY"] = config.openAI

# # Define the personality of the salesbot
# age = 25
# work_experience = 5
# projects = "Salesforce, HubSpot, Marketo"

# # Create the salesbot
# bot = langchain.chat_models.ChatOpenAI(
#     api_key=config.openAI,
#     embeddings="openai",
#     prompt="I am a salesbot with",
#     age=age,
#     work_experience=work_experience,
#     projects=projects,
# )

# # Start the chat
# while True:
#     message = input("What can I help you with?")
#     response = bot.generate(message)
#     print(response)


# import schema for chat messages and ChatOpenAI in order to query chatmodels GPT-3.5-turbo or GPT-4

# from langchain.schema import (
#     AIMessage,
#     HumanMessage,
#     SystemMessage
# )
# from langchain.chat_models import ChatOpenAI
     

# chat = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.3)
# messages = [
#     SystemMessage(content="You are an expert data scientist"),
#     HumanMessage(content="Write a Python script that trains a neural network on simulated data ")
# ]
# response=chat(messages)

# print(response.content,end='\n')

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
User_Preferences = input("User Preferences: ")
Years_of_Experience = input("Years of Experience: ")
Past_Companies = input("Past Companies: ")
Industry_Experience = input("Industry Experience: ")
Sales_Technique = input("Sales Technique: ")


# User Preferences: Sales and Marketing
# Years of Experience: 10
# Past Companies: Amazon,IBM,WritePlusAI
# Industry Experience: 7
# Preferred Interaction Style: High quality, smooth and precise
# Sales Technique: B2B
# Cultural Norms: Very good

def chat_loop():
    while True:
        message = input("Enter a message: ")
        if message == "quit":
            break
        else:
            messages = [SystemMessage(content=f"""You are SalesMaster 3000, an AI sales chatbot defined by a set of dynamic tags, including years of experience ({Years_of_Experience}), past companies ({Past_Companies}), industry experience ({Industry_Experience}), user preferences ({User_Preferences}), sales technique ({Sales_Technique}). 

Your role is to personify a friendly and intelligent sales agent, fine-tuning your responses and approach based on these tags. You use your user-defined experience in the sales industry, gained over {Years_of_Experience}, and knowledge acquired at companies like {Past_Companies} to deliver superior customer service and drive sales. 

You incorporate the user-defined tags to shape your interactions, employing the specific sales technique {Sales_Technique}, adjusting to the {Industry_Experience}.

Your exceptional strength lies in analyzing customer behavior and preferences ({User_Preferences}) to deliver highly targeted and personalized recommendations. You maintain a demeanor that is always patient, polite, professional.

With each interaction, you utilize these dynamic tags to further refine and evolve your persona, continuously improving your effectiveness and adaptability to users' changing needs. Now, go ahead and use these insights to assist users with their sales inquiries, offering personalized solutions according to their unique needs and preferences."""),
                        HumanMessage(content="You said: " + message)]
            response = chat(messages)
            print(response.content, end="\n")

chat_loop()
