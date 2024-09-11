from speech_to_text import speech_to_text
from chatbot import chatbot_ans
from joblib import load
from pandas import read_csv
from text_to_speech import text_to_speech

# for chatbot
loaded_model = load('data/chatbot_model.joblib')
sentence_embeddings = load('data/sentence_embeddings')
datafame = read_csv("data/transcript.csv")


def interactive_agent():
    user_question_text = speech_to_text()

    db_ans, similarity_score = chatbot_ans(
        loaded_model, 
        sentence_embeddings, 
        text=user_question_text, 
        datafame=datafame)
    print(similarity_score)

    text_to_speech(text=db_ans)

