THE APPLICATION/SCRIPT IS ONLY MEANT TO USE FOR PERSONAL USE!

# matchmaker
Keyword search tool. Will check for technical keywords in the job listing and search those keywords in the resume.

1. Create new virtual environment and install requirements
2. Update path to your resume in .pdf format in matchmaker.resume.resume.py
3. To run -  `python app.py`

This is only bootstrap. Need performance improvement and multiple other fixes.
Sample Output of a linkedin job posting againts the my resume. 
+----------+--------+-------------+
|  Skill   | Resume | Job Posting |
+----------+--------+-------------+
|   HTML   |   0    |      6      |
|   CSS    |   0    |      1      |
|  Java,   |   1    |      0      |
|    C#    |   0    |      1      |
|  Spring  |   1    |      0      |
|   Boot   |   1    |      0      |
|  Agile   |   1    |      0      |
|  Scrum   |   1    |      0      |
|   API    |   1    |      1      |
| Software |   1    |      2      |
+----------+--------+-------------+
