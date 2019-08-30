"""
  User: Liujianhan
  Time: 23:05
 """

from flask import Blueprint
from pyltp import Segmentor, Postagger, Parser, SementicRoleLabeller

__author__ = 'liujianhan'

web = Blueprint('web', __name__)
segmentor = Segmentor()
segmentor.load(r"D:\\Github\\NLP\\Projects\\data\\ltp_data_v3.4.0\\cws.model")

postagger = Postagger()
postagger.load(r"D:\\Github\\NLP\\Projects\\data\\ltp_data_v3.4.0\\pos.model")

parser = Parser()
parser.load(r"D:\\Github\\NLP\\Projects\\data\\ltp_data_v3.4.0\\parser.model")

labeller = SementicRoleLabeller()
labeller.load(r"D:\\Github\\NLP\\Projects\\data\\ltp_data_v3.4.0\\pisrl_win.model")
from app.web import news
