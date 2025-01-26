# import chainlit as cl
# import ollama
# import asyncio

# @cl.on_chat_start
# async def start_chat():
#     cl.user_session.set("history", [])
#     await cl.Message("Deepseek-R1 Assistant Ready!").send()

# @cl.on_message
# async def main(message: cl.Message):
#     # Get chat history
#     history = cl.user_session.get("history")
#     history.append({"role": "user", "content": message.content})
    
#     # Create response generator (synchronous)
#     response = ollama.chat(
#         model='deepseek-r1',
#         messages=history,
#         stream=True
#     )
    
#     # Create and stream response
#     reply_message = cl.Message(content="")
#     await reply_message.send()
    
#     # Process synchronous generator in async context
#     for chunk in response:
#         await reply_message.stream_token(chunk['message']['content'])
    
#     # Update history and finalize message
#     history.append({"role": "assistant", "content": reply_message.content})
#     await reply_message.update()    


import chainlit as cl
import ollama
import asyncio

# Configuration
MODEL_NAME = "deepseek-r1"
MAX_HISTORY = 10
SYSTEM_PROMPT = """You are Deepseek-R1, a helpful AI assistant. 
Provide concise, accurate responses using proper markdown formatting when appropriate."""

@cl.on_chat_start
async def start_chat():
    cl.user_session.set("history", [
        {"role": "system", "content": SYSTEM_PROMPT}
    ])
    await cl.Message("🚀 Deepseek-R1 Ready! Type /clear to reset history.").send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content.strip()
    history = cl.user_session.get("history")
    
    if user_input.lower() == "/clear":
        cl.user_session.set("history", [
            {"role": "system", "content": SYSTEM_PROMPT}
        ])
        await cl.Message("🔄 History cleared").send()
        return
    
    history.append({"role": "user", "content": user_input})

    # Manage history length
    if len(history) > MAX_HISTORY * 2 + 1:
        history = [history[0]] + history[-(MAX_HISTORY * 2):]

    # Create async generator wrapper
    async def generate_response():
        response = ollama.chat(
            model=MODEL_NAME,
            messages=history,
            stream=True
        )
        
        reply_message = cl.Message(content="")
        await reply_message.send()
        
        try:
            for chunk in response:
                if chunk['message']['content']:
                    await reply_message.stream_token(chunk['message']['content'])
                # Add small delay to prevent packet overflow
                await asyncio.sleep(0.01)
        finally:
            # Finalize message and update history
            await reply_message.update()
            history.append({"role": "assistant", "content": reply_message.content})
            cl.user_session.set("history", history)

    # Run the generator in the event loop
    await generate_response()