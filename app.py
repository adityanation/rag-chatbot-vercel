from fastapi import FastAPI
import gradio as gr

app = FastAPI()

# Define chatbot function
def chatbot_interface(user_input):
    return "This is a response to: " + user_input  # Replace with generate_response(user_input)

# Gradio UI
gradio_app = gr.Interface(fn=chatbot_interface, inputs="text", outputs="text")

@app.get("/")
def home():
    return {"message": "RAG Chatbot is running on Vercel!"}

@app.get("/gradio")
def gradio_ui():
    return gradio_app.launch()

# Run locally for testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
