# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 14:14:03 2025

@author: suresh.burra
"""

from typing import List, Optional
from dataclasses import dataclass
from datetime import date

@dataclass
class Education:
    institution: str
    degree: str
    field: str
    start_date: date
    end_date: Optional[date]
    gpa: Optional[float] = None

@dataclass
class Experience:
    company: str
    position: str
    start_date: date
    end_date: Optional[date]
    responsibilities: List[str]
    location: Optional[str] = None

@dataclass
class Skill:
    name: str
    level: str  # e.g., Beginner, Intermediate, Advanced, Expert

class Resume:
    def __init__(self):
        self.personal_info: dict = {}
        self.summary: Optional[str] = None
        self.education: List[Education] = []
        self.experience: List[Experience] = []
        self.skills: List[Skill] = []
        self.languages: List[str] = []
        self.certifications: List[str] = []
        self.projects: List[dict] = []

    def __str__(self):
        output = f"\n=== RESUME ===\n"
        output += f"Name: {self.personal_info.get('name', 'N/A')}\n"
        output += f"Email: {self.personal_info.get('email', 'N/A')}\n"
        output += f"\nSummary: {self.summary}\n"
        output += f"\nEducation: {len(self.education)} entries\n"
        output += f"Experience: {len(self.experience)} entries\n"
        output += f"Skills: {len(self.skills)} skills\n"
        return output

class ResumeBuilder:
    def __init__(self):
        self.resume = Resume()

    def add_personal_info(self, name: str, email: str, phone: str, location: Optional[str] = None, linkedin: Optional[str] = None):
        self.resume.personal_info = {
            'name': name,
            'email': email,
            'phone': phone,
            'location': location,
            'linkedin': linkedin
        }
        return self

    def add_summary(self, summary: str):
        self.resume.summary = summary
        return self

    def add_education(self, institution: str, degree: str, field: str, start_date: date, end_date: Optional[date] = None, gpa: Optional[float] = None):
        education = Education(institution, degree, field, start_date, end_date, gpa)
        self.resume.education.append(education)
        return self

    def add_experience(self, company: str, position: str, start_date: date, end_date: Optional[date], responsibilities: List[str], location: Optional[str] = None):
        experience = Experience(company, position, start_date, end_date, responsibilities, location)
        self.resume.experience.append(experience)
        return self

    def add_skill(self, name: str, level: str):
        skill = Skill(name, level)
        self.resume.skills.append(skill)
        return self

    def add_skills(self, *skills: tuple):
        for name, level in skills:
            self.add_skill(name, level)
        return self

    def add_language(self, language: str):
        self.resume.languages.append(language)
        return self

    def add_certification(self, certification: str):
        self.resume.certifications.append(certification)
        return self

    def add_project(self, name: str, description: str, technologies: List[str]):
        project = {
            'name': name,
            'description': description,
            'technologies': technologies
        }
        self.resume.projects.append(project)
        return self

    def build(self) -> Resume:
        if not self.resume.personal_info:
            raise ValueError("Personal information is required to build a resume.")
        return self.resume


# Usage
resume = (ResumeBuilder()
          .add_personal_info(
    name="Jane Smith",
    email="jane.smith@example.com",
    phone="+1234567890",
    location = "San Francisco, CA"
)
            .add_summary("Experienced software engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success.")
            .add_education(
    institution="University of California, Berkeley",
    degree="Bachelor of Science",
    field="Computer Science",
    start_date=date(2012, 8, 1),
    end_date=date(2016, 5, 15),
    gpa=3.9)
    .add_experience(
    company="Tech Solutions Inc.",
    position="Senior Software Engineer",
    start_date=date(2018, 6, 1),
    end_date=None,
    responsibilities=[
        "Led a team of 5 engineers to develop scalable web applications.",
        "Implemented CI/CD pipelines to streamline deployment processes.",
        "Collaborated with cross-functional teams to define project requirements."
    ],
    location="San Francisco, CA"
)
    .add_skill("Python", "Expert")
    .add_skill("JavaScript", "Advanced")
    .add_skill("Docker", "Intermediate")
    .add_language("English")
    .add_language("Spanish")
    .add_certification("AWS Certified Solutions Architect")
    .add_project(
    name="E-commerce Platform",
    description="Developed a full-featured e-commerce platform with user authentication, product management, and payment integration.",
    technologies=["Django", "React", "PostgreSQL", "AWS"]
)
          .build())

print(resume)




