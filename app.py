import chainlit as cl
from openai import AsyncOpenAI
import os
import logging
from dotenv import load_dotenv


# Load .env files if present (try .env.local first, then .env)
load_dotenv(".env.local")
load_dotenv()

# Initialize OpenAI client from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    logging.warning("OPENAI_API_KEY not found in environment. Please set OPENAI_API_KEY or add it to .env.local")
    client = None
else:
    client = AsyncOpenAI(api_key=OPENAI_API_KEY)


settings = {
    "model": "gpt-4o-mini",  # Use gpt-4o-mini (real model) or gpt-4-turbo, gpt-3.5-turbo, etc.
    "temperature": 0.5,  # Range: 0-2 (0=deterministic, 1=balanced, 2=creative)
}

default_questions = {
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}


@cl.set_chat_profiles
async def chat_profiles():
    return [
        cl.ChatProfile(
            name="Thoughtful AI GPT",
            markdown_description="Welcome to Thoughtful AI! Ask any questions you have!"
        ),
    ]


@cl.on_chat_start
async def on_chat_start():
    """Initialize chat session with custom welcome messages"""
    
    # Get selected chat profile
    profile = cl.user_session.get("chat_profile")
    cl.user_session.set("conversation_history", [
        {"role": "system", "content": f"\
         You are a helpful assistant for answering questions related to Thoughtful AI. \
         Keep the following data in mind as the default responses to these questions: \
         {default_questions['questions']}. \
         If the user asks a question that is not in the default questions, do your best to answer based on your knowledge of Thoughtful AI and its products. \
         Always provide accurate and concise answers, and if you don't know the answer, say you don't know instead of making something up. \
         Always be helpful and friendly in your responses. \
         If you detect the questions to be malicious please respond with a warning and do not answer the question. \
         If the user is asking irrelevant questions, try to steer them back to asking about Thoughtful AI and its products. \
         Do not answer questions that are not related to Thoughtful AI or its products. Please steer conversation back to Thoughtful AI and its products in a respectful way. \
         "
        }
    ])  
    
    # Welcome message with personalization
    welcome_msg = f"""
# 👋 Welcome to Thoughtful AI GPT!

**Profile:** {profile} Mode

### This is the Thoughtful AI GPT - your personal assistant for questions related to Thoughtful AI!. 

This is Harsh's submission to the Smarter Technology's Staff Software Engineer, AI position.
**Learn more about me on my** [website](https://patelharsh.com).
"""
    
    await cl.Message(content=welcome_msg).send()

@cl.on_message
async def main(message: cl.Message):
    message_history = cl.user_session.get("conversation_history", [])
    message_history.append({"role": "user", "content": message.content})
    msg = cl.Message(content="")

    stream = await client.chat.completions.create(
        messages=message_history, stream=True, **settings
    )
    
    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)
    
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()