from enum import Enum 
from pydantic import BaseModel, Field
from typing import Annotated
from dotenv import load_dotenv
import instructor
import os 
from groq import AsyncGroq
import asyncio

load_dotenv()

client = instructor.from_groq(
    AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))
)

class Confidence(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Answer(BaseModel):
    summary: Annotated[str, Field(min_length=10, max_length=100)]
    key_points: Annotated[list[str], Field(min_length=3, max_length=7)]
    confidence: Confidence
    next_step: Annotated[str, Field(min_length=10, max_length=500)]

async def ask_structured_question(user_question: str):
    data = await client.create(
        response_model=Answer,
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI Agent Expert. Your sole purpose is to extract structured data to facilitate the development of autonomous agents. STRICT ADHERENCE TO THE JSON SCHEMA IS MANDATORY. Ensure 'key_points' is always a list of strings. Maintain lowercase for 'confidence' and ensure 'next_step' is a brief, actionable instruction. Do not include any conversational filter."
                )
            },
            {
                "role": "user",
                "content": f'Extract: {user_question}' 
            }
        ]
    )
    
    print('Summary:', data.summary)

    if data.key_points:
        print('Key Points:')
        for point in data.key_points:
            print(f'. {point}')
    else:
        print('No key points extracted.')
    
    print('Confidence:', data.confidence.value)
    print('Next Step:', data.next_step)

if __name__ == "__main__":
    question = 'What are the best ways for a beginner Python developer in India to build their first AI agent product in 2026?'
    asyncio.run(ask_structured_question(question))