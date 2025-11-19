import reflex as rx
from app.states.state import State, Skill


def skill_card(skill: Skill) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(skill["name"], class_name="font-semibold text-gray-700"),
            rx.el.p(
                f"{skill['proficiency']}%", class_name="text-sm text-sky-600 font-bold"
            ),
            class_name="flex justify-between items-center mb-2",
        ),
        rx.el.div(
            rx.el.div(
                style={"width": f"{skill['proficiency']}%"},
                class_name="h-2 rounded-full bg-gradient-to-r from-sky-400 to-blue-500",
            ),
            class_name="w-full bg-gray-200 rounded-full h-2",
        ),
        class_name="bg-white p-4 rounded-lg border border-gray-100 shadow-sm",
    )


def about_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "About Me",
                class_name="text-3xl font-bold text-gray-800 mb-4 text-center",
            ),
            rx.el.div(
                rx.el.p(
                    "I am a Data Scientist and AI/ML Developer with a passion for transforming complex data into intelligent, actionable insights. With a strong foundation in statistical modeling and machine learning, I specialize in building scalable AI applications that drive business value. My journey in tech is fueled by a relentless curiosity and a desire to solve real-world problems through elegant and efficient code.",
                    class_name="text-center text-gray-600 max-w-3xl mx-auto text-lg",
                ),
                class_name="mb-12",
            ),
            rx.el.h3(
                "My Skills",
                class_name="text-2xl font-bold text-gray-800 mb-8 text-center",
            ),
            rx.el.div(
                rx.foreach(State.skills, skill_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-4xl mx-auto",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="about",
        class_name="py-24 bg-gray-50",
    )