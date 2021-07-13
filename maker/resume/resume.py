import pdfplumber
import sys
import json

from pathlib import Path
from pprint import pprint
from prettytable import PrettyTable


def load_config():
    with open("config.json", "r") as f_config:
        config = json.load(f_config)
    return config


filename = load_config()["resume"]["pdf"]


def readpdf(skills):
    resume_count = {"soft": {}, "technical": {}}
    technical = {}
    for skill in skills:
        technical[skill] = 0

    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            value = page.extract_text().split("\n")
            values = [w for v in value for w in v.split(" ")]

        for skill in skills:
            if skill in values:
                technical[skill] += 1
    resume_count["technical"] = technical
    return resume_count


def presentation(word_count):
    skills = [s for s in word_count["technical"]]
    resume_count = readpdf(skills)
    table = PrettyTable(["Skill", "Resume", "Job Posting"])
    for skill in skills:
        skill_in_resume_count = resume_count["technical"][skill]
        skill_in_job_posting_count = word_count["technical"][skill]
        if skill_in_job_posting_count > 0 or skill_in_resume_count > 0:
            table.add_row([skill, skill_in_resume_count, skill_in_job_posting_count])
    print(table)
