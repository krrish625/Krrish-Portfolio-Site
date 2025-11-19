import reflex as rx
from app.states.state import State, Project


def project_card(project: Project) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(project["icon"], class_name="h-16 w-16 text-sky-200"),
            class_name="h-48 w-full flex items-center justify-center bg-gradient-to-br from-sky-500 to-blue-600 rounded-t-xl",
        ),
        rx.el.div(
            rx.el.h3(
                project["title"], class_name="text-xl font-bold text-gray-800 mb-2"
            ),
            rx.el.p(project["description"], class_name="text-gray-600 mb-4 text-sm"),
            rx.el.div(
                rx.foreach(
                    project["tech"],
                    lambda tag: rx.el.span(
                        tag,
                        class_name="bg-sky-100 text-sky-700 text-xs font-medium px-2.5 py-1 rounded-full",
                    ),
                ),
                class_name="flex flex-wrap gap-2 mb-6",
            ),
            rx.el.div(
                rx.el.a(
                    rx.el.button(
                        "View Demo",
                        rx.icon("external-link", class_name="ml-2 h-4 w-4"),
                        class_name="flex items-center justify-center w-full bg-sky-500 text-white px-4 py-2 rounded-lg font-semibold hover:bg-sky-600 transition-colors duration-300",
                    ),
                    href=project["demo_url"],
                    is_external=True,
                ),
                rx.el.a(
                    rx.el.button(
                        "GitHub",
                        rx.icon("github", class_name="ml-2 h-4 w-4"),
                        class_name="flex items-center justify-center w-full bg-gray-100 text-gray-700 px-4 py-2 rounded-lg font-semibold hover:bg-gray-200 transition-colors duration-300 border border-gray-200",
                    ),
                    href=project["github_url"],
                    is_external=True,
                ),
                class_name="flex items-center gap-4 mt-auto",
            ),
            class_name="p-6 flex flex-col h-full",
        ),
        class_name="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden transform hover:-translate-y-1 hover:shadow-lg transition-all duration-300 flex flex-col h-full",
    )


def projects_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "My Projects",
                class_name="text-3xl font-bold text-gray-800 mb-12 text-center",
            ),
            rx.el.div(
                rx.foreach(State.projects, project_card),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="projects",
        class_name="py-24 bg-white",
    )