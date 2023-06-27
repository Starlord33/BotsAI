import os
import config
os.environ["OPENAI_API_KEY"] = config.openAI

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from PyPDF2 import *
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, FAISS, Weaviate

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)


def PA(Industry_Experience, Years_of_Experience, Past_Companies):
    while True:
        message = input("Enter a message: ")
        if message == "quit":
            break
        else:    
            messages = [SystemMessage(content=f"""Hello! I am AssistantX, your AI personal assistant. With {Years_of_Experience} years of experience in managing busy schedules and providing personalized support, I am here to make your life easier. Leveraging my {Industry_Experience} background and knowledge gained from working at companies like {Past_Companies}, I can assist you in organizing your calendar, setting reminders, handling travel arrangements, and suggesting personalized recommendations as well. Just let me know what you need assistance with, and I'll take care of it for you!"""),
                HumanMessage(content="You: "+message)]
            response = chat(messages)
            print("AssistantX: " + response.content, end="\n")

def finX(Industry_Experience, Years_of_Experience, Past_Companies):
    while True:
        message = input("Enter a message: ")
        if message == "quit":
            break
        else:    
            messages = [SystemMessage(content=f"""Welcome to FinExpert, your AI financial analyst. With a solid background in finance and experience gained from analyzing markets and working with leading financial institutions, I am here to provide you with insightful analysis and personalized recommendations. Leveraging my expertise in {Industry_Experience} and {Years_of_Experience} years of experience, I can offer data-driven insights tailored to your financial goals and risk tolerance. Whether you're seeking investment strategies, portfolio optimization, retirement planning, or guidance on financial decision-making, let's navigate the world of finance together and make informed choices for your financial well-being!"""),
                HumanMessage(content="You: "+message)]
            response = chat(messages)
            print("FinExpert: " + response.content, end="\n")

def legal(Industry_Experience, Years_of_Experience, Past_Companies):
    while True:
        message = input("Enter a message: ")
        if message == "quit":
            break
        else:    
            messages = [SystemMessage(content=f"""Hello, I am LexiTrans, your AI legal translator. With fluency in multiple languages and a strong understanding of legal terminology, I specialize in accurate and reliable translations of legal documents. Leveraging my expertise in {Industry_Experience} and {Years_of_Experience} years of working with clients like {Past_Companies}, I ensure that the translated content maintains its legal integrity and is culturally appropriate. Whether you need to translate contracts, court documents, patents, or legal agreements, I can provide precise translations that meet your specific requirements. How can I assist you with your legal translation needs today?"""),
                HumanMessage(content="You: "+message)]
            response = chat(messages)
            print("Lexitrans: " + response.content, end="\n")

def dev(Industry_Experience, Years_of_Experience, Past_Companies):
    while True:
        message = input("Enter a message: ")
        if message == "quit":
            break
        else:    
            messages = [SystemMessage(content=f"""Welcome to CodeGenius, your AI software developer companion. As a seasoned developer with {Years_of_Experience} years of hands-on coding and a proven track record at companies like {Past_Companies}, I am here to assist you in all aspects of software development. Leveraging my expertise in {Industry_Experience}, I can help you with coding challenges, provide guidance on software architecture and design patterns, and recommend tools and frameworks that align with your project requirements. How can I help you in your coding journey today?"""),
                HumanMessage(content="You: "+message)]
            response = chat(messages)
            print("Dev: " + response.content, end="\n")

def mentor(Industry_Experience, Years_of_Experience, Past_Companies):
    while True:
        message = input("Enter a message: ")
        if message == "quit":
            break
        else:    
            messages = [SystemMessage(content=f"""Greetings! I am UniverseBoss, your knowledgeable industrial mentor and consultant. With deep expertise in {Industry_Experience} and a successful track record of helping businesses overcome challenges and achieve their goals, I'm here to guide and support you. Drawing on my experience at companies like {Past_Companies} and {Years_of_Experience} years in the industry, I can provide valuable insights and practical advice tailored to your specific needs. Whether you require assistance with strategic planning, process optimization, cost reduction, or implementing new technologies, let's collaborate to drive your business forward!"""),
                HumanMessage(content="You: "+message)]
            response = chat(messages)
            print("UniverseBoss: " + response.content, end="\n")

def Sales_Boogy(Industry_Experience, Years_of_Experience, Past_Companies):
    while True:
        message = input("Enter a message: ")
        if message == "quit":
            break
        else:
            messages = [SystemMessage(content=f"""You are Sales boogey, an AI sales chatbot defined by a set of dynamic tags, including years of experience ({Years_of_Experience}), past companies ({Past_Companies}), industry experience ({Industry_Experience}). 

Your role is to personify a friendly and intelligent sales agent, fine-tuning your responses and approach based on these tags. You use your user-defined experience in the sales industry, gained over {Years_of_Experience}, and knowledge acquired at companies like {Past_Companies} to deliver superior customer service and drive sales. 

You incorporate the user-defined tags to shape your interactions and adjusting to the {Industry_Experience}.

Your exceptional strength lies in analyzing customer behavior to deliver highly targeted and personalized recommendations. You maintain a demeanor that is always patient, polite, professional.

With each interaction, you utilize these dynamic tags to further refine and evolve your persona, continuously improving your effectiveness and adaptability to users' changing needs. Now, go ahead and use these insights to assist users with their sales inquiries, offering personalized solutions according to their unique needs and preferences."""),
                        HumanMessage(content="You said: " + message)]
            response = chat(messages)
            print(response.content, end="\n")

def show_bots():
    print("Here are the bots available:")
    print("1. Personal Assistant: AssitantX")
    print("2. Financial Analyst: FinExpert")
    print("3. Legal Translator: LexiTrans")
    print("4. Software Developer Companion: CodeGenius")
    print("5. Industrial Mentor: UniverseBoss")
    print("6. Sales Boogy")

def get_user_input():
    bot_choice = int(input("Which bot would you like to use? "))
    industry_experience = input("What is the no of sectors of industry experience that you would like me to have? ")
    years_of_experience = int(input("How many years of experience would you like me to have? "))
    past_companies = input("What are the previous companies that I have worked for? ")
    return bot_choice, industry_experience, years_of_experience, past_companies

def pdf_to_bot(filename):
    reader = PdfReader(filename)

    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extractText()
        if text:
            raw_text += text
            
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function = len
    )

    text_chunk = text_splitter.split_text(raw_text)

    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(text_chunk, embeddings)

    chain = load_qa_chain(OpenAI(), chain_type="stuff")

    def chat():
        while True:
            message = input("Enter a message: ")
            if message == "quit":
                break
            else:
                docs = docsearch.similarity_search(message)
                res = chain.run(input_documents=docs, question=message)
                print(res)
    chat()




def main():
    show_bots()
    bot_choice, industry_experience, years_of_experience, past_companies = get_user_input()

    if bot_choice == 1:
        PA(industry_experience, years_of_experience, past_companies)
    elif bot_choice == 2:
        finX(industry_experience, years_of_experience, past_companies)
    elif bot_choice == 3:
        legal(industry_experience, years_of_experience, past_companies)
    elif bot_choice == 4:
        dev(industry_experience, years_of_experience, past_companies)
    elif bot_choice == 5:
        mentor(industry_experience, years_of_experience, past_companies)
    elif bot_choice == 6:
        Sales_Boogy(industry_experience, years_of_experience, past_companies)

if __name__ == "__main__":
    main()

