import os
import google.generativeai as genai

def process_gemini_query(query):
    genai.configure(api_key=os.environ["GEMINI_API"])

    # Create the model
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 100,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-1.5-pro",
      generation_config=generation_config,
 
    )

    chat_session = model.start_chat(
      history=[
      ]
    )

    response = chat_session.send_message(query)

    return response.text