# https://github.com/ROCm/ROCm/issues/2536

from transformers import *
import random

def generate_random_sentence():
   # Define a list of sentence structures
   structures = [
       "NOUN VERB ADJECTIVE NOUN.",
       "NOUN VERB ADJECTIVE NOUN ADVERB.",
       "NOUN ADVERB VERB NONU."
   ]

   # Choose a random sentence structure from the list
   structure = random.choice(structures)

   # Define a list of nouns
   nouns = [
       "cat", "dog", "bird", "car", "plane", "ship"
   ]

   # Define a list of verbs
   verbs = [
       "sat", "barked", "flew", "drove", "flew", "crewed"
   ]

   # Define a list of adjectives
   adjectives = [
       "blue", "red", "green", "white", "black", "orange"
   ]

   # Define a list of adverbs
   adverbs = [
       "quickly", "slowly", "loudly", "quietly", "angrily", "calmly"
   ]

   # Replace placeholders in the sentence structure with random words from the lists
   sentence = structure.replace("NOUN", random.choice(nouns))
   sentence = sentence.replace("VERB", random.choice(verbs))
   sentence = sentence.replace("ADJECTIVE", random.choice(adjectives))
   sentence = sentence.replace("ADVERB", random.choice(adverbs))

   return sentence

# Generate an array of 10 random sentences
random_sentences = [generate_random_sentence() for _ in range(100)]

pipe = pipeline("translation", "Helsinki-NLP/opus-mt-en-zh", device=0)

ret = pipe(random_sentences)
print(ret)
