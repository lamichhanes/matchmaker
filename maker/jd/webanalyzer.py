import requests as rq
from lxml import html
from bs4 import BeautifulSoup


def run():
    # r = rq.get("https://jobs.lever.co/blendlabs/ea55639b-3ab0-45d6-98fc-13d731ed766e?lever-origin=applied&lever-source%255B%255D=LinkedInPremium&lever-source=LinkedInJobs")
    r = rq.get(
        "https://boards.greenhouse.io/turo/jobs/3279487?s=LinkedIn&source=LinkedIn")
    # with open('./response.txt') as f:
    #     content = f.readlines()
    technical_skills = ['frontend', 'rest', 'api', 'backend', 'development',
                        'react', 'angular', 'java', 'python', 'node',
                        'javascript', 'C#', 'mysql', 'mongo', 'database',
                        'software', 'engineering', 'sql']

    soft_skills = ['team', 'collaborative', 'strong communicaiton', 'problem',
                   'solving', 'team player']

    word_count = {
        "soft": {},
        "technical": {}

    }
    soft = {}
    technical = {}
    soup = BeautifulSoup(r.content, "lxml")
    data = [d.lower() for d in soup.findAll(text=True)]

    for skill in technical_skills:
        technical[skill] = 0
    count = 0
    for d in data:
        for skill in technical_skills:
            if skill in d:
                technical[skill] += 1
    word_count['technical'] = technical
    return word_count

    # for line in content:
    #     word_count = {
    #         "soft": {},
    #         "technical": {}

    #     }
    #     soft = {}
    #     technical = {}
    #     soup = BeautifulSoup(line, "lxml")
    #     data = [d.lower() for d in soup.findAll(text=True)]

    #     for skill in technical_skills:
    #         technical[skill] = 0
    #     count = 0
    #     for d in data:
    #         for skill in technical_skills:
    #             if skill in d:
    #                 technical[skill] += 1
    #     word_count['technical'] = technical
    #     return word_count
