import spacy
import pandas as pd

nlp = spacy.load('en_core_web_md')

# Sentence from which the recommendation will be worked out.
sentence_to_compare = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# Importing the movies from which a recommandation will be made.
sentences = pd.read_csv('movies.txt', delimiter='\t', header=None)
model_sentence = nlp(sentence_to_compare)

# Below block has an array and a loop to store and iterate throught the sentences in preparation for the next movie recommandation all stored inside a function. 
def next_recommended_movie():
    similarities = {}
    for sentence in sentences.iloc[:, 0]:
        similarity = nlp(sentence).similarity(model_sentence)
        similarities[sentence] = similarity
    similarity_max_score = max(similarities.values())
    recommended_movie = max(similarities, key=similarities.get)

    # Below block will only allow to print the movie title, discarding the movie description.
    if ':' in recommended_movie:
        recommended_movie = recommended_movie[:recommended_movie.index(':')]
    
    return recommended_movie, similarity_max_score

# To use the below variables we need to call the function first
recommended_movie, similarity_max_score = next_recommended_movie()

print(f"The recommended movie title will be ' {recommended_movie}' with a similarity score of: {similarity_max_score:.2f} (to 2 s.f.).")

# References:
# 1 - Files provided by HyperionDev on this task and previous tasks
# 2 - https://www.programiz.com/python-programming/methods/dictionary/keys
# 3 - https://tutorial.eyehunts.com/python/key-lambda-python-keylambda-function-example/
# 4 - https://stackoverflow.com/questions/41587578/read-file-headers-and-delimiters-using-python
