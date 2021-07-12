import requests as rq
from bs4 import BeautifulSoup
from jd.skills import TECHNICAL_SKILLS as ts, SOFT_SKILLS as ss


class JobDescription:
    def __init__(self):
        self.technical_skills = ts
        self.soft_skills = ss
        self.word_count = {"soft": {}, "technical": {}}

    def populate_word_count(self, technical_skills, data):
        soft = {}
        technical = {}
        for skill in technical_skills:
            technical[skill] = 0
        count = 0
        for d in data:
            for skill in technical_skills:
                if skill in d:
                    technical[skill] += 1
        self.word_count["technical"] = technical
        return self.word_count

    def process(self, content):
        data = []
        soup = BeautifulSoup(content, "lxml")
        data = [d for d in soup.findAll(text=True) if d != "\\n"]
        return data

    def web_processing(self, url):
        r = rq.get(url)
        data = self.process(r.content)
        return self.populate_word_count(self.technical_skills, data)
