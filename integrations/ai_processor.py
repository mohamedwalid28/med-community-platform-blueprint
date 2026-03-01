import openai

def generate_video_summary(transcript_text):
    """Uses LLM to summarize medical videos for the community feed"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize this medical lecture: {transcript_text}"}]
    )
    return response.choices[0].message.content