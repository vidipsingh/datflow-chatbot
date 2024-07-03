from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import keras
import pickle
import json
import nltk
from nltk.stem import WordNetLemmatizer
import random
import sqlite3

app = Flask(__name__)

lemmatizer = WordNetLemmatizer()

# Load the model, words, and classes
model = keras.models.load_model('chatbot_model.h5')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Load intents
with open('intents.json') as file:
    intents = json.load(file)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_product_details(product_name):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT description, price FROM products WHERE name=?', (product_name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        description, price = result
        return f"The {product_name} is {description} and costs ${price:.2f}."
    else:
        return f"Sorry, I couldn't find any details for {product_name}."

def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            if tag == 'order_status':
                result = "Your order is being prepared and will be delivered in approximately 30 minutes."
            elif tag == 'product_details':
                # Extract the product name from the user's message
                for pattern in i['patterns']:
                    if pattern.lower() in message.lower():
                        product_name = pattern.split()[-1]
                        result = get_product_details(product_name)
                        break
                else:
                    result = random.choice(i['responses'])
            else:
                result = random.choice(i['responses'])
            break
    return result

@app.route('/chat', methods=['POST'])
def chat():
    global message
    message = request.json['message']
    ints = predict_class(message, model)
    res = get_response(ints, intents)
    return jsonify({"response": res})

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)

