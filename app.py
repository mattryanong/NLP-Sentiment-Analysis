import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from flask import abort, Flask, jsonify, request

app = Flask(__name__)


@app.route('/analyseSentiment', methods=['POST'])
def analyseSentiment():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']
    lower_case = message.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    sentiment = ""
    if neg > pos:
        sentiment = "Negative Sentiment"
    elif pos > neg:
        sentiment = "Positive Sentiment"
    else:
        sentiment = "Neutral Sentiment"

    tokenized_words = word_tokenize(cleaned_text, "english")
    final_words = []
    for word in tokenized_words:
        if word not in stopwords.words('english'):
            final_words.append(word)
    emotion_list = []
    # 'r' is read only mode
    with open('emotions.txt', 'r') as file:
        for line in file:
            # clean up all the unnecessary characters in each line
            # strip is like .trim()
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            # splits line into whatever is before and after ":"
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)

    w = Counter(emotion_list)

    response = {'score': score, 'sentiment': sentiment, "breakdown": w}
    return jsonify(response), 200


if __name__ == "__main__":
    app.run()

# # reading text file
# # encoding is to read stuff written in html
# # text = open("read.txt", encoding="utf-8").read()
# #
# # # converting to lowercase
# # lower_case = text.lower()
#
# # Removing punctuations
# # 1st param specifies list of chars that need to be replaced
# # 2nd param is the list of chars with which the chars need to be replaced
# # 3rd param specifies list of chars that need to be removed
# cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
#
# # splitting text into words
# # tokenized_words = cleaned_text.split()
# tokenized_words = word_tokenize(cleaned_text, "english")
#
# # stop words don't add any meaning to the sentence (NLTK has a more exhaustive list)
# # stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
# #               "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
# #               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
# #               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
# #               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
# #               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
# #               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
# #               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
# #               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
# #               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#
#
# # Removing stop words from the tokenized words list
# final_words = []
# for word in tokenized_words:
#     if word not in stopwords.words('english'):
#         final_words.append(word)
#
# # NLP Emotion Algorithm
# # 1) Check if the word in the final word list is also present in emotion.txt
# #  - open the emotion file
# #  - Loop through each line and clear it
# #  - Extract the word and emotion using split
#
# # 2) If word is present -> Add the emotion to emotion_list
# # 3) Finally count each emotion in the emotion list
#
# emotion_list = []
# # 'r' is read only mode
# with open('emotions.txt', 'r') as file:
#     for line in file:
#         # clean up all the unnecessary characters in each line
#         # strip is like .trim()
#         clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
#         # splits line into whatever is before and after ":"
#         word, emotion = clear_line.split(':')
#
#         if word in final_words:
#             emotion_list.append(emotion)
#
# # print(emotion_list)
# w = Counter(emotion_list)
# print(w)
#
#
# def sentiment_analyse(sentiment_text):
#     score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
#     print(score)
#     neg = score['neg']
#     pos = score['pos']
#     if neg > pos:
#         print("Negative Sentiment")
#     elif pos > neg:
#         print("Positive Sentiment")
#     else:
#         print("Neutral Sentiment")
#
#
# sentiment_analyse(cleaned_text)
#
# # Plotting the emotions on the graph
#
# fig, ax1 = plt.subplots()
# ax1.bar(w.keys(), w.values())
# # auto formats x and y axis so that all values are presented properly
# fig.autofmt_xdate()
# plt.savefig('graph.png')
# plt.show()
