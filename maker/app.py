from jd.posting import JobDescription
from resume import resume as r
from pprint import pprint


def run(url):
    jd = JobDescription()
    word_count = jd.web_processing(url)
    r.presentation(word_count)


if __name__ == "__main__":
    url = input("Enter posting url: ")
    run(url)
