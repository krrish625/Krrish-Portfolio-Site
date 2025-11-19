import reflex as rx
from app.states.state import State
from app.components.navbar import navbar
from app.components.hero import hero_section
from app.components.about import about_section
from app.components.projects import projects_section
from app.components.services import services_section
from app.components.contact import contact_section


def scroll_to_top_button() -> rx.Component:
    return rx.el.button(
        rx.icon("arrow-up", class_name="h-5 w-5"),
        on_click=rx.scroll_to("top"),
        class_name=rx.cond(
            State.show_scroll_to_top,
            "fixed bottom-8 right-8 bg-sky-500 text-white p-3 rounded-full shadow-lg hover:bg-sky-600 transition-all duration-300 z-50 opacity-100 transform scale-100",
            "fixed bottom-8 right-8 bg-sky-500 text-white p-3 rounded-full shadow-lg hover:bg-sky-600 transition-all duration-300 z-50 opacity-0 transform scale-95 pointer-events-none",
        ),
    )


def index() -> rx.Component:
    """The main page of the portfolio."""
    return rx.el.div(
        navbar(),
        rx.el.main(
            hero_section(),
            about_section(),
            projects_section(),
            services_section(),
            contact_section(),
            id="top",
        ),
        rx.el.footer(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("layers", class_name="h-7 w-7 text-sky-600"),
                        rx.el.span(
                            "Krrish Jha",
                            class_name="ml-2 text-xl font-bold text-gray-800",
                        ),
                        class_name="flex items-center",
                    ),
                    rx.el.p(
                        "Data Scientist & AI/ML Developer passionate about creating intelligent solutions.",
                        class_name="mt-2 text-gray-500 max-w-sm",
                    ),
                    class_name="flex flex-col items-start",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Quick Links", class_name="font-semibold text-gray-800 mb-4"
                    ),
                    rx.el.div(
                        rx.el.a(
                            "About",
                            href="#about",
                            class_name="text-gray-500 hover:text-sky-600",
                        ),
                        rx.el.a(
                            "Projects",
                            href="#projects",
                            class_name="text-gray-500 hover:text-sky-600",
                        ),
                        rx.el.a(
                            "Services",
                            href="#services",
                            class_name="text-gray-500 hover:text-sky-600",
                        ),
                        rx.el.a(
                            "Contact",
                            href="#contact",
                            class_name="text-gray-500 hover:text-sky-600",
                        ),
                        class_name="flex flex-col space-y-2",
                    ),
                    class_name="hidden md:block",
                ),
                rx.el.div(
                    rx.el.h3("Connect", class_name="font-semibold text-gray-800 mb-4"),
                    rx.el.div(
                        rx.el.a(
                            rx.icon(
                                "github",
                                class_name="h-6 w-6 text-gray-500 hover:text-sky-600",
                            ),
                            href="#",
                            is_external=True,
                        ),
                        rx.el.a(
                            rx.icon(
                                "linkedin",
                                class_name="h-6 w-6 text-gray-500 hover:text-sky-600",
                            ),
                            href="#",
                            is_external=True,
                        ),
                        rx.el.a(
                            rx.icon(
                                "twitter",
                                class_name="h-6 w-6 text-gray-500 hover:text-sky-600",
                            ),
                            href="#",
                            is_external=True,
                        ),
                        rx.el.a(
                            rx.icon(
                                "mail",
                                class_name="h-6 w-6 text-gray-500 hover:text-sky-600",
                            ),
                            href="mailto:krrish.jha@email.com",
                        ),
                        class_name="flex items-center space-x-4",
                    ),
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-3 gap-8 text-left",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 Krrish Jha. All Rights Reserved.",
                    class_name="text-sm text-gray-500",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 mt-12 pt-8 border-t border-gray-200 text-center",
            ),
            class_name="py-12 bg-gray-50",
        ),
        scroll_to_top_button(),
        class_name="font-['Roboto'] bg-white",
        on_scroll=State.on_scroll,
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")