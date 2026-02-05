import os 
import shutil 
from openai import OpenAI 

# 1. SETUP: Replace with your actual key starting with sk-or-v1-... 
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="sk-or-v1-61f9054f42a717bbe6518775d006aeeef...", 
) 

def move_screenshots(): 
    source = os.path.expanduser("~/Desktop") 
    target = os.path.expanduser("~/Desktop/My_Screenshot") 
    if not os.path.exists(target): os.makedirs(target) 
    files = [f for f in os.listdir(source) if f.endswith(".png")] 
    for file in files: shutil.move(os.path.join(source, file), os.path.join(target, file)) 
    
    # AI celebration message
    try:
        completion = client.chat.completions.create(
          model="google/gemini-2.0-flash-001",
          messages=[
            {"role": "user", "content": f"I just organized {len(files)} screenshots for my boss. Give me a 1-sentence witty robot celebration message."}
          ]
        )
        return f"Success! {completion.choices[0].message.content}"
    except Exception as e:
        return f"Success! Moved {len(files)} screenshots. (Note: AI celebration failed due to API key issue: {e})"

print("Robot: AI Brain Online. Type 'move' to start.")
user_input = input("You: ")
if "move" in user_input.lower():
    print(move_screenshots())
