from jd import webanalyzer as wa
from pathlib import Path
from pprint import pprint
import pdfplumber
import sys

sys.path.append(Path.home()/"Desktop/Interview Materials/matchmaker/maker")


filename = Path.home()/"path/to/resume"

def readpdf(skills, resume_count):
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            value = page.extract_text().split("\n")
        values = [w.lower() for v in value for w in v.split(" ") ]
        technical = {}
        for skill in skills:
            technical[skill] = 0
        for skill in skills:
            if skill in values:
                technical[skill] += 1
    resume_count['technical'] = technical
    return resume_count


def resume(word_count):
    skills = [s for s in word_count["technical"]]
    resume_count = {
        "soft" : {},
        "technical" : {}
    }
    data = readpdf(skills, resume_count)
    for skill in skills:
        print(f'Skill {skill} count in resume is {data["technical"][skill]} in JD the cound is {word_count["technical"][skill]}')
