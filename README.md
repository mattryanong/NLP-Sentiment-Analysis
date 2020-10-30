# NLP-Sentiment-Analysis
NLP using NLTK for textual sentiment/ emotion analysis.

Original boiler plate code from buildwithpython- Attreya Bhatt. Modified algorithm components and deployed as a microservice.

Use command: 

python app.py 

from the root directory to deploy the application. 
Default endpoint is localhost:5000/analyseSentiment.

Dependencies required:

flask
collections
nltk
matplotlib

Algorithm for scoring: 
https://stackoverflow.com/questions/40325980/how-is-the-vader-compound-polarity-score-calculated-in-python-nltk

Algorithm for feeling categorisation/ breakdown:
- dataset found in emotions.txt (expandable)
- scans through emotions.txt for related emotions
- categorises results into a bar chart
