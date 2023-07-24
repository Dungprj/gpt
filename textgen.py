import streamlit as st
import openai

st.title("hello world")
#cai dat model davanci 
model = "text-davinci-003"
with open("api.txt","r") as f:
	openai.api_key = f.readline()


def get_response_from_chatgpt(user_question):
	response = openai.Completion.create(

		engine = model,
		prompt = user_question,
		max_tokens = 1024,
		n = 1,
		temperature = 0.5
		)

	response_text = response.choices[0].text
	return response_text

def main():
	user_question = st.text_input("Nhập câu hỏi vào đây ")
	if st.button("Bắt đầu tìm câu trả lời"):
		response_text = get_response_from_chatgpt(user_question)
		return st.write(f"{user_question} {response_text}" )


main()