import os
from pydantic import BaseModel, Field
from typing import List
from groq import Groq
import instructor

os.environ["GROQ_API_KEY"] = "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"

class SubjectInfo(BaseModel):
    title: str
    details: List[str] = Field(..., description="A list of facts about the subject")

def get_topic():
    return input("Enter a topic to learn about (or 'exit' to quit): ")

def fetch_info(subject):
    api_client = Groq(
        api_key=os.environ.get(
            os.environ.get("GROQ_API_KEY"),
        ),
    )

    api_client = instructor.from_groq(api_client, mode=instructor.Mode.TOOLS)

    response = api_client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "user",
                "content": f"Tell me about {subject}",
            }
        ],
        response_model=SubjectInfo,
    )
    print(response.model_dump_json(indent=2))

if __name__ == "__main__":
    while True:
        topic_input = get_topic()
        if topic_input.lower() == 'exit':
            break
        fetch_info(topic_input)
