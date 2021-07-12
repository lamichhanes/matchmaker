RESUME_ATTRIBUTES = {
    "first_name": str(),
    "last_name": str(),
    "email": str(),
    "phone": str(),
    "location": str(),
    "work_experience": [
        {
            "company_name": str(),
            "start_date": str(),
            "end_date": str(),
            "title": str(),
            "location": {"city": str(), "state": str()},
            "responsibilities": [],
            "projects": [],
            "tech_stact": [],
        }
    ],
    "techinical_skills": [],
    "soft_skills": [],
}
