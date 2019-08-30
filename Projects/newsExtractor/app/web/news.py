"""
  User: Liujianhan
  Time: 23:07
 """
from flask import render_template, request

from app.forms.content import ContentForm
from app.web import web

__author__ = 'liujianhan'


@web.route('/', methods=['GET', 'POST'])
def extract():
    data = None
    form = ContentForm(request.form)
    from app.libs.extractor import Extractor

    if form.validate_on_submit() and request.method == 'POST':
        sentence = form.q.data.strip()
        result = Extractor().sentence_parse(sentence)
        if len(result) == 3:
            subject, speak_word, content = result
            data = {
                'subject': subject,
                'speak_word': speak_word,
                'content': content
            }
        else:
            data = result
    return render_template('news.html', form=form, data=data)
