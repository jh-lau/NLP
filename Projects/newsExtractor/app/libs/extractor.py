"""
  User: Liujianhan
  Time: 11:55
 """

from flask import current_app
from app.web import segmentor, postagger, labeller, parser

__author__ = 'liujianhan'


class Extractor:
    target_verbs = current_app.config['TARGET_VERBS']

    @staticmethod
    def ltp_integrated(sentence):
        words = list(segmentor.segment(sentence))
        postags = postagger.postag(words)
        arcs = parser.parse(words, postags)
        roles = labeller.label(words, postags, arcs)
        return words, postags, arcs, roles

    def sentence_parse(self, sentence):
        words, postags, arcs, roles = self.ltp_integrated(sentence)
        # content = ''
        tags = list(zip(words, postags))
        subject_index = [(arg.range.start, arg.range.end) for role in roles
                         for arg in role.arguments if arg.name == 'A0']
        if subject_index:
            subject = [words[index[0]:index[1] + 1] for index in subject_index][0][0]
        else:
            return "No subject is found in sentence."

        verbs = [x[0] for x in tags if x[1] == 'v']
        try:
            speak_word = (set(verbs) & self.target_verbs).pop()
        except KeyError:
            return "No speech is found in sentence."

        speak_word_index = sentence.index(speak_word)
        size = len(speak_word)
        if sentence[speak_word_index + 1] in {'。', '，', '：', ',', '.', ':'}:
            content = sentence[speak_word_index + size + 1:-1]
        else:
            content = sentence[speak_word_index + size:-1]

        return subject, speak_word, content
