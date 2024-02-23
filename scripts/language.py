# coding: utf-8
# Copyright (c) 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

################################################################################################################
# This script assumes you have created an OCI config on your local machine to interact with the SDK.
# For more information: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#
# Information on OCI AI Language service: https://www.oracle.com/artificial-intelligence/language/
#
################################################################################################################


import oci

# Please fill out all paramaters
config_path = "~/.oci/config"
# From https://www.oracle.com/cloud/
test_string = "Oracle Cloud Infrastructure is built for enterprises seeking higher performance, lower costs, and easier cloud migration for their applications. Customers choose Oracle Cloud Infrastructure over AWS for several reasons: First, they can consume cloud services in the public cloud or within their own data center with Oracle Dedicated Region Cloud@Customer. Second, they can migrate and run any workload as is on Oracle Cloud, including Oracle databases and applications, VMware, or bare metal servers. Third, customers can easily implement security controls and automation to prevent misconfiguration errors and implement security best practices. Fourth, they have lower risks with Oracle’s end-to-end SLAs covering performance, availability, and manageability of services. Finally, their workloads achieve better performance at a significantly lower cost with Oracle Cloud Infrastructure than AWS. Take a look at what makes Oracle Cloud Infrastructure a better cloud platform than AWS."


def create_language_client(config_path):

    config = oci.config.from_file(
        config_path, "DEFAULT")
    return oci.ai_language.AIServiceLanguageClient(config)


def create_text_document(key_, data, language_code_="auto"):

    return oci.ai_language.models.TextDocument(
        key=key_,
        text=data,
        language_code=language_code_
    )


def sentiment_analysis(AI_client, text_document):

    try:
        # Run sentiment analysis on text_document
        detect_language_sentiments_response = AI_client.batch_detect_language_sentiments(
            batch_detect_language_sentiments_details=oci.ai_language.models.BatchDetectLanguageSentimentsDetails(documents=[text_document])
        )
        return detect_language_sentiments_response.data

    # Print service error for debugging
    except Exception as e:
        print(e)
    return


def key_phrase_extraction(AI_client, text_document):
    try:
        keyphrase_extraction = AI_client.batch_detect_language_key_phrases(
            batch_detect_language_key_phrases_details=oci.ai_language.models.BatchDetectLanguageKeyPhrasesDetails(documents=[text_document])
        )
        return keyphrase_extraction.data
    except Exception as e:
        print(e)


def named_entity_extraction(AI_client, text_document):
    try:
        language_entities = AI_client.batch_detect_language_entities(
            batch_detect_language_entities_details=oci.ai_language.models.BatchDetectLanguageEntitiesDetails(documents=[text_document])
        )

        return language_entities.data

    # Print service error for debugging
    except Exception as e:
        print(e)
    return


def text_classification(AI_client, text_document):
    try:
        # Run text classification on text_document
        text_classification = AI_client.batch_detect_language_text_classification(
            batch_detect_language_text_classification_details=oci.ai_language.models.BatchDetectLanguageTextClassificationDetails(
                documents=[text_document]
            )
        )
        # return the data
        return text_classification.data

    # Print any API errors
    except Exception as e:
        print(e)
    return

# https://docs.oracle.com/en-us/iaas/tools/python/2.122.0/api/ai_language/models/oci.ai_language.models.BatchLanguageTranslationDetails.html#oci.ai_language.models.BatchLanguageTranslationDetails
def text_translation(AI_client, text_document):
    try:
        # Run text classification on text_document
        text_translation = AI_client.batch_language_translation(
            batch_language_translation_details=oci.ai_language.models.BatchLanguageTranslationDetails(
                documents=[text_document],
                target_language_code="en"
            )
        )
        # return the data
        return text_translation.data

    # Print any API errors
    except Exception as e:
        print(e)
    return


def print_divider():
    # Helper function to print a divider between analysis'
    for i in range(50):
        print("-", end=""),
    print("\n")


def print_all_responses(sentiment_response, key_phrase_response, named_entity_response, text_classification_response):
    """
    Prints all OCI AI Language responses.

    Parameters:
    sentiment_response(BatchDetectLanguageSentimentsResult): JSON object that holds the result of API call to OCI Language endpoint for sentiment response.
    key_phrase_response(): JSON object that holds the result of API call to OCI Language endpoint for key phrase response.
    named_entity_response(): JSON object that holds the result of API call to OCI Language endpoint for named entity response.
    text_classification_response(): JSON object that holds the result of API call to OCI Language endpoint for text classification response.

    """
    print("Sentiment Analysis on text:")
    for i in range(0, len(sentiment_response.documents)):
        for j in range(0, len(sentiment_response.documents[i].aspects)):
            print("Text: {}".format(sentiment_response.documents[i].aspects[j].text))
            print("Overall sentiment: {}".format(sentiment_response.documents[i].aspects[j].sentiment))
            print("Length: {}".format(sentiment_response.documents[i].aspects[j].length))
            print("Offset: {}".format(sentiment_response.documents[i].aspects[j].offset))

    print_divider()
    print("Key phrase extraction on text:")

    for i in range(len(key_phrase_response.documents)):
        for j in range(len(key_phrase_response.documents[i].key_phrases)):
            print("phrase: {}".format(key_phrase_response.documents[i].key_phrases[j].text))
            print("score: {}".format(key_phrase_response.documents[i].key_phrases[j].score))

    print_divider()
    print("Named entity extraction on text:")

    for i in range(len(named_entity_response.documents)):
        for j in range(len(named_entity_response.documents[i].entities)):
            print("Text: {}".format(named_entity_response.documents[i].entities[j].text))
            print("Type: {}".format(named_entity_response.documents[i].entities[j].type))
            print("Sub_Type: {}".format(named_entity_response.documents[i].entities[j].sub_type))
            print("Length: {}".format(named_entity_response.documents[i].entities[j].length))
            print("Offset: {}".format(named_entity_response.documents[i].entities[j].offset))

    print_divider()
    print("Text classification analysis on text:")
    for i in range(len(text_classification_response.documents)):
        for j in range(len(text_classification_response.documents[i].text_classification)):
            print("Label: {}".format(text_classification_response.documents[i].text_classification[j].label))
            print("Score: {}".format(text_classification_response.documents[i].text_classification[j].score))


def run_model(data, config_path="~/.oci/config", text_model_key="Example", language_code="en"):
    """
    Runs all functions needed for this example.

    Creates language client, 4 text analysis reponses and prints all the necessary output.

    Parameters:
    data(str): The text that will be analyzed.
    config_path(str): Path to OCI config file. Default value: ~/.oci/config
    text_model_key(str): Added to the metadata of the text document, required. Default value: Example
    language_code(str): Language code for a text document, required. Default value: en
    Returns:
    TextDocument: The document details for language service call.

    """

    # Create language client and text document to be analyzed, up to 100 can be analyzed at the same time.
    language_client = create_language_client(config_path)
    text_document = create_text_document(key_=text_model_key, language_code_="en", data=data)

    # Grab all responses by the AI client
    sentiment_response = sentiment_analysis(language_client, text_document)
    key_phrase_response = key_phrase_extraction(language_client, text_document)
    named_entity_response = named_entity_extraction(language_client, text_document)
    text_classification_response = text_classification(language_client, text_document)

    print_all_responses(sentiment_response, key_phrase_response, named_entity_response, text_classification_response)

def main() -> None:
    # Run example model
    run_model(test_string, config_path, text_model_key="example", language_code="en")


if __name__ == '__main__':
    main()
