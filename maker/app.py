from jd.webanalyzer import JobDescription
from resume import resume as r

from pprint import pprint

jd = JobDescription()
url = "https://boards.greenhouse.io/turo/jobs/3279487?s=LinkedIn&source=LinkedIn"
word_count = jd.web_processing(url)
pprint(word_count)