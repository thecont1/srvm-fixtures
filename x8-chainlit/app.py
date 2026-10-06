import chainlit as cl


@cl.on_chat_start
async def greet():
    await cl.Message(content="srvm fixture x8 - chainlit echo bot. Send me anything.").send()


@cl.on_message
async def reply(message: cl.Message):
    await cl.Message(content=f"echo: {message.content}").send()
