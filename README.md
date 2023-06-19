# finalCapstone
# Movie Recommendation System

This code provides a movie recommendation based on a given sentence. It uses the `spacy` library for NLP processing and the `pandas` library for data manipulation.

## Table of contents
- [Installation](# Installation)
- [Usage](# Usage)
- [Credits](# Credits)

## Installation
1. Install Python 3.x

2. Install required libraries:
   ```
   pip install spacy pandas
   ```

3. Download the language model:
   ```
   python -m spacy download en_core_web_md
   ```

## Usage
1. Ensure that the `movies.txt` file is present in the same directory as the script. 

2. Import the necessary libraries at the beginning of your script:
   ```python
   import spacy
   import pandas as pd
   ```

3. Load the language model:
   ```python
   nlp = spacy.load('en_core_web_md')
   ```

4. Define the sentence from which the recommendation will be worked out:
   ```python
   sentence_to_compare = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
   the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
   Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''
   ```

5. Implement the recommendation system:
   ```python
   sentences = pd.read_csv('movies.txt', delimiter='\t', header=None)

   def next_recommended_movie():
       similarities = {}
       for sentence in sentences.iloc[:, 0]:
           similarity = nlp(sentence).similarity(nlp(sentence_to_compare))
           similarities[sentence] = similarity
       similarity_max_score = max(similarities.values())
       recommended_movie = max(similarities, key=similarities.get)
       if ':' in recommended_movie:
           recommended_movie = recommended_movie[:recommended_movie.index(':')]
       return recommended_movie, similarity_max_score

   recommended_movie, similarity_max_score = next_recommended_movie()

   print(f"The recommended movie title will be '{recommended_movie}' with a similarity score of: {similarity_max_score:.2f} (to 2 s.f.).")
   ```

   The code will calculate the similarity score between the given sentence and each movie title from the `movies.txt` file. 
   It then recommends the movie title with the highest similarity score.

6. Run the script and view the recommended movie title and its similarity score.
Note: Make sure to update the `movies.txt` file with a relevant list of movies for accurate recommendations.

## Credits
- Files provided by HyperionDev on this task and previous tasks
- https://www.programiz.com/python-programming/methods/dictionary/keys
- https://tutorial.eyehunts.com/python/key-lambda-python-keylambda-function-example/
- https://stackoverflow.com/questions/41587578/read-file-headers-and-delimiters-using-python



Feel free to modify and customize the code to suit your specific requirements.
