
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
import fr_core_news_sm

def resume(text):

    nlp = fr_core_news_sm.load()
    if text is not None:
        doc = nlp(text)
    else:
        print("Le texte est vide ou None")
    corpus = [ sent.text.lower() for sent in doc.sents ]

    cv = CountVectorizer(stop_words=list(STOP_WORDS))
    cv_fit = cv.fit_transform(corpus)

    words = cv.get_feature_names_out()
    occurs_words = cv_fit.toarray().sum(axis=0)

    freq_mot = dict(zip(words, occurs_words))
    valeurs = sorted(freq_mot.values())

    freq_mot_plus_freq = valeurs[-1]
    for mot in freq_mot:
        print(f"{mot} : {freq_mot[mot]/freq_mot_plus_freq}")

    score_phrase = {}
    for phrase in doc.sents:
        for mot in phrase:
            if mot.text.lower() in freq_mot.keys():
                if phrase.text.lower() in score_phrase.keys():
                    score_phrase[phrase.text.lower()] += freq_mot[mot.text.lower()]
                else:
                    score_phrase[phrase.text.lower()] = freq_mot[mot.text.lower()]

    top_impo = sorted(score_phrase.values())[::-1]
    top_syn = top_impo[:3]

    brouillon = []
    resumer = ""
    for phrase, score in score_phrase.items():
        if score in top_syn:
            brouillon.append(phrase)
        else:
            continue
    for phrase in brouillon:
        resumer += phrase + " "

        return resumer.capitalize()
    
