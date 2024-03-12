# This code reads tweets from a JSON file, creates text documents for each tweet, and translates them using the OCI Language service.

from language import text_translation, create_text_document, create_language_client, sentiment_analysis, key_phrase_extraction, named_entity_extraction, text_classification
from language import print_all_responses, print_divider
import ujson as json
import statistics

# Path to OCI config file
config_path = "~/.oci/config"

# Create a language client using the config path
language_client = create_language_client(config_path)

final_tweets = list()
sentiments = list()

stock_subject = 'NVIDIA'

# Open the tweets JSON file
with open('../data/nvidia_tweets.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    # Iterate through each tweet in the data
    for element in data:
        tweet = element['tweet']
        # Create a text document for the tweet
        text_document = create_text_document(key_="Example", language_code_="auto", data=tweet)
        
        # Translate the text document using the language client
        result = text_translation(language_client, text_document)
        print(result)
        # Print the original tweet

        # Print the translation result
        for i in range(len(result.documents)):
            print("Translation: {}".format(result.documents[i].translated_text))
            final_tweets.append({'tweet': result.documents[i].translated_text})

file.close()

# Write final_tweets to a JSON file
with open('../data/translated_tweets.json', 'w', encoding='utf-8') as output_file:
    json.dump(final_tweets, output_file, ensure_ascii=False, indent=4)

# Now that we have translated tweets, open this file again with utf-8 encoding,
# read tweets, and process the sentiment for each one of the tweets:

output_file.close()

with open('../data/translated_tweets.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    for element in data:
        tweet = element['tweet']
        print(tweet)
        # Create a text document for the tweet
        text_document = create_text_document(key_="Example", language_code_="en", data=tweet) # autodetect language
        # Grab all responses by the AI client  
        sentiment_response = sentiment_analysis(language_client, text_document)
        # you could search for specific phrases, like $NVDA using key phrase extraction
        key_phrase_response = key_phrase_extraction(language_client, text_document)
        # you could filter only tweets that mention specific orgs, e.g. "Text: Nvidia Type: ORGANIZATION"
        named_entity_response = named_entity_extraction(language_client, text_document)
        # you could filter only tweets that have Label: Finance/Investing from text_classification
        text_classification_response = text_classification(language_client, text_document)

        #print_all_responses(sentiment_response, key_phrase_response, named_entity_response, text_classification_response)
        all_scores = {
            'mixed': list(),
            'positive': list(),
            'neutral': list(),
            'negative': list()
        }
        for i in range(0, len(sentiment_response.documents)):
            all_scores['mixed'].append(sentiment_response.documents[i].document_scores['Mixed'])
            all_scores['positive'].append(sentiment_response.documents[i].document_scores['Positive'])
            all_scores['neutral'].append(sentiment_response.documents[i].document_scores['Neutral'])
            all_scores['negative'].append(sentiment_response.documents[i].document_scores['Negative'])
            #print(sentiment_response.documents[i].document_sentiment)
            print(sentiment_response.documents[i].document_scores)
        
print_divider()
print('** [SUMMARY] ** [{}]'.format(stock_subject))
print_divider()
for key,value in all_scores.items():
    print("--- Average {} sentiment: {:.3f}%".format(key, statistics.mean(value)*100))

