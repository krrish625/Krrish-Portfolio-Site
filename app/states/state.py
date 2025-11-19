import reflex as rx
from typing import TypedDict


class Skill(TypedDict):
    name: str
    proficiency: int


class Project(TypedDict):
    icon: str
    title: str
    description: str
    tech: list[str]
    demo_url: str
    github_url: str


class Service(TypedDict):
    icon: str
    title: str
    description: str


class State(rx.State):
    """The base state for the app."""

    is_drawer_open: bool = False
    show_scroll_to_top: bool = False
    skills: list[Skill] = [
        {"name": "Python", "proficiency": 95},
        {"name": "TensorFlow", "proficiency": 90},
        {"name": "PyTorch", "proficiency": 85},
        {"name": "Scikit-learn", "proficiency": 95},
        {"name": "Pandas", "proficiency": 98},
        {"name": "NumPy", "proficiency": 98},
        {"name": "SQL", "proficiency": 80},
        {"name": "Docker", "proficiency": 75},
        {"name": "AWS", "proficiency": 70},
        {"name": "React", "proficiency": 85},
        {"name": "FastAPI", "proficiency": 90},
    ]
    services: list[Service] = [
        {
            "icon": "figma",
            "title": "Graphic Design",
            "description": "Creating visually stunning graphics that capture attention and communicate your brand's message effectively.",
        },
        {
            "icon": "code",
            "title": "Web Development",
            "description": "Building responsive, high-performance websites with a focus on user experience and modern technologies.",
        },
        {
            "icon": "smartphone",
            "title": "App Development",
            "description": "Developing intuitive and feature-rich mobile applications for both iOS and Android platforms.",
        },
        {
            "icon": "pen-tool",
            "title": "UI/UX Design",
            "description": "Designing user-centric interfaces that are not only beautiful but also easy to navigate and a pleasure to use.",
        },
    ]
    projects: list[Project] = [
        {
            "icon": "file-text",
            "title": "AI Resume Analyzer",
            "description": "An intelligent system to parse resumes, extract key information using NLP, and match candidates to job requirements efficiently.",
            "tech": ["Python", "OpenAI", "LangChain", "FastAPI", "React"],
            "demo_url": "#",
            "github_url": "#",
        },
        {
            "icon": "heart-pulse",
            "title": "Heart Disease Prediction Model",
            "description": "A machine learning model to predict the risk of heart disease based on patient data, aiding in early diagnosis.",
            "tech": ["Python", "Scikit-learn", "Pandas", "Streamlit", "XGBoost"],
            "demo_url": "#",
            "github_url": "#",
        },
    ]

    @rx.event
    def toggle_drawer(self):
        """Toggles the mobile navigation drawer."""
        self.is_drawer_open = not self.is_drawer_open

    @rx.event
    def close_drawer(self):
        """Closes the mobile navigation drawer."""
        self.is_drawer_open = False

    @rx.event
    def on_scroll(self):
        """Handles the on_scroll event to show/hide the scroll-to-top button."""
        pass

    @rx.event
    async def submit_contact_form(self, form_data: dict):
        """Handles contact form submission."""
        name = form_data.get("name", "").strip()
        email = form_data.get("email", "").strip()
        message = form_data.get("message", "").strip()
        if not name or not email or (not message):
            yield rx.toast.error("Please fill out all fields.")
            return
        import asyncio

        yield rx.toast.info("Submitting your message...")
        await asyncio.sleep(2)
        print(f"Form submitted: Name='{name}', Email='{email}', Message='{message}'")
        yield rx.toast.success("Message sent successfully! I'll be in touch soon.")