from joblib import dump
from sentence_transformers import SentenceTransformer
import pandas as pd

def chatbot_train(data, model_path="data/", embeding_path="data/"):

    dataset_lenght,columns = data.shape

    sentences=[]
    for i in range(0,dataset_lenght):
        corpus=data.iloc[i,columns-2]
        sentences.append(corpus)
    
    model= SentenceTransformer('paraphrase-mpnet-base-v2')
    sentence_embeddings = model.encode(sentences)

    # save the trained model ('paraphrase-mpnet-base-v2') for further use
    # model_directory = "database/model/"
    # data_path = "database/data/"
    
    dump(model, model_path+'chatbot_model.joblib')
    dump(sentence_embeddings, embeding_path+"sentence_embeddings")
    
    return None

# if __name__ == "__main__":
#     # Train model
#     data_path = "data/transcript.csv"    
    
#     data = pd.read_csv(data_path)
#     chatbot_train(data)
