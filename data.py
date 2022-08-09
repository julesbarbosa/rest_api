from typing import List, TypedDict, Dict


class Work(TypedDict):
    id: int
    company: str
    Title: str
    start_year: int


class Education(TypedDict):
    id: int
    School: str
    level: str
    start_year: int


class Projects(TypedDict):
    id: int
    title: str
    description: str
    tecnologies: str


class Publications(TypedDict):
    id: int
    title: str


class Skills(TypedDict):
    id: int
    skill: str


WORK: dict[int, Work] = {
    1: {"id": 1, "Company": "Accern", "Title": "Data Scientist", "start_year": "2021"},
    2: {"id": 2, "Company": "Accern", "Title": "Data Scientist intern", "start_year": "2020"},
    3: {"id": 3, "Company": "NYU", "Title": "Graduate Student Assistant", "start_year": "2020"},
}

EDUCATION: dict[int, Education] = {
       1: {"id": 1, "School": "NYU", "level": "Master", "start_year": "2018"},
       2: {"id": 2, "School": "Federal University of Piaui", "level": "Bachelor of Science", "start_year": 2010},
}

PROJECTS: dict[int, Projects] = {
        1: {
            "id": 1,
            "title": "Hurricane population perceptions based on 311 complaints and weather data",
            "description": "spearheaded a comprehensive analysis of weather data to understand patterns in weather changes and human reactions",
            "tecnologies": "Python, Tableau"},
        2: {
            "id": 2,
            "title": "Persona modeling on student profiles for Universities",
            "description": "Performed exploratory and descriptive analysis on large student datasets and performed unsupervised machine learning algorithm (K-means) to identify student personas, so that marketing strategies could be directed only towards eligible student personas thereby optimizing costs and improving results",
            "tecnologies": "R-Studio, Tableau"}
}

PUBLICATIONS: dict[int, Publications] = {
       1: {"id": 1, "title": "BARBOSA, J. S. et al. Analysis of hiring employees by means of time study and queueing theory: a case of study in a gas station. In: Symposium of Production Engineering, XXII SIMPEP, Bauru, 2015. p.14"},
       2: {"id": 2, "title": "BARBOSA, J. S. FILHO, E. G. C. The construction material supplier relationship management. Qualitas electronic journal, v.19, n.1, Jan 2018"},
}

SKILLS: dict[int, Skills] = {
       1: {"id": 1, "skill": "open courses: Learn to Program: The fundamentals​, ​Python for Data Science Essential Training​, ​SQL Essential Training​, and ​Fundamentals of Scalable Data Science​, MIT-6001, MIT-6002"},
       2: {"id": 2, "skill": "Programming Languages and Technologies: Python, Docker, Scikit-learn, HuggingFace, Pandas, Numpy, Pytorch, Spacy, Elasticsearch, Redis, NLP, Machine Learning, Deep Learning, SQL"},
       3: {"id": 3, "skill": "Languages: Portuguese (native), English (fluent), and Spanish (conversational)"},
}


class NotFoundError(Exception):
    pass


def get_all_education() -> List[Education]:
    return list(EDUCATION.values())


def get_all_work_experience() -> List[Work]:
    return list(WORK.values())


def get_all_academic_projects() -> List[Projects]:
    return list(PROJECTS.values())


def get_all_publications() -> List[Publications]:
    return list(PUBLICATIONS.values())


def get_all_skils() -> List[Skills]:
    return list(SKILLS.values())


def get_work(work_id: int) -> Work:
    work = WORK.get(work_id, None)
    if work is not None:
        return work
    raise NotFoundError("work not found")


def create_new_work(work_id: int, new_work: dict) -> list[Work]:
    WORK[work_id] = new_work
    return list(WORK.values())
