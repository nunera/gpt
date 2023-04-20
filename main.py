import streamlit as st
import openai, os

keys = os.environ['MY_SECRET'].split()


# keys = [""]
def chatbot(text, token, temperature):
  prompt = text
  return openai.Completion.create(
    max_tokens=token,
    model='text-davinci-003',
    prompt=prompt,
    temperature=temperature,
  ).choices[0]["text"]


def send(prompt, Tokens, Temperature, Api_Key):
  openai.api_key = Api_Key
  output = chatbot(prompt, Tokens, Temperature)
  st.markdown(output, True)


inp = st.text_area("Input", "Write me an essay about penguins.")
temp = st.slider("Temperature (Creativity)", 0.0, 2.0, 1.0, 0.01)
tokens = st.slider("Tokens (Length)",
                   0,
                   4000,
                   3800,
                   1,
                   help="If nothing happens, gradually decrease this number.")
api_key = st.selectbox("Api Key", keys)
if st.button("Start"):
  send(inp, tokens, temp, api_key)
else:
  pass
