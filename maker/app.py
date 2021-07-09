from jd import webanalyzer as wa
from resume import resume as r

from pprint import pprint

word_count = wa.run()
r.resume(word_count)
