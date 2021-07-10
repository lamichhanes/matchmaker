import requests as rq
from lxml import html
from bs4 import BeautifulSoup


class JobDescription:
    def __init__(self):
        self.technical_skills = [
            "frontend",
            "rest",
            "api",
            "backend",
            "development",
            "react",
            "angular",
            "java",
            "python",
            "node",
            "javascript",
            "C#",
            "mysql",
            "mongo",
            "database",
            "software",
            "engineering",
            "sql",
        ]
        self.soft_skills = [
            "team",
            "collaborative",
            "strong communication",
            "problem",
            "solving",
            "team player",
        ]
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
        data = [d.lower() for d in soup.findAll(text=True)]
        return data


    def web_processing(self, url):
        r = rq.get(url)
        data = self.process(r.content)
        return self.populate_word_count(self.technical_skills, data)


    
