import reflex as rx
from app.states.state import State


def nav_link(text: str, section_id: str) -> rx.Component:
    """A navigation link that scrolls to a section."""
    return rx.el.a(
        text,
        on_click=[rx.scroll_to(section_id), State.close_drawer],
        class_name="text-gray-500 hover:text-sky-600 transition-colors duration-300 font-medium cursor-pointer",
    )


def mobile_nav_link(text: str, section_id: str) -> rx.Component:
    """A navigation link for the mobile drawer."""
    return rx.el.a(
        text,
        on_click=[rx.scroll_to(section_id), State.close_drawer],
        class_name="block w-full py-3 px-4 text-lg text-gray-700 hover:bg-sky-50 rounded-md transition-colors duration-200 cursor-pointer",
    )


def navbar() -> rx.Component:
    """The navigation bar component."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("layers", class_name="h-7 w-7 text-sky-600"),
                rx.el.span(
                    "Krrish Jha", class_name="ml-2 text-xl font-bold text-gray-800"
                ),
                class_name="flex items-center",
            ),
            rx.el.nav(
                nav_link("About", "about"),
                nav_link("Skills", "skills"),
                nav_link("Projects", "projects"),
                nav_link("Services", "services"),
                nav_link("Contact", "contact"),
                class_name="hidden md:flex items-center gap-8",
            ),
            rx.el.div(
                rx.el.button(
                    "Hire Me",
                    on_click=rx.scroll_to("contact"),
                    class_name="hidden md:block bg-sky-500 text-white px-5 py-2 rounded-lg font-medium hover:bg-sky-600 transition-all duration-300 shadow-sm hover:shadow-md",
                ),
                rx.el.button(
                    rx.icon(tag="menu", class_name="h-6 w-6"),
                    on_click=State.toggle_drawer,
                    class_name="md:hidden p-2 rounded-md text-gray-600 hover:bg-gray-100",
                ),
                class_name="flex items-center",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-20",
        ),
        rx.el.div(
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
                    rx.el.button(
                        rx.icon("x", class_name="h-6 w-6"),
                        on_click=State.close_drawer,
                        class_name="p-2 rounded-md text-gray-600 hover:bg-gray-100",
                    ),
                    class_name="flex justify-between items-center p-4 border-b",
                ),
                rx.el.nav(
                    mobile_nav_link("About", "about"),
                    mobile_nav_link("Skills", "skills"),
                    mobile_nav_link("Projects", "projects"),
                    mobile_nav_link("Services", "services"),
                    mobile_nav_link("Contact", "contact"),
                    class_name="p-4 flex flex-col gap-2",
                ),
                rx.el.div(
                    rx.el.button(
                        "Hire Me",
                        on_click=[rx.scroll_to("contact"), State.close_drawer],
                        class_name="w-full bg-sky-500 text-white py-3 rounded-lg font-medium hover:bg-sky-600 transition-colors duration-300",
                    ),
                    class_name="p-4 mt-auto border-t",
                ),
                class_name="flex flex-col h-full bg-white",
            ),
            class_name=rx.cond(
                State.is_drawer_open,
                "fixed top-0 right-0 h-full w-4/5 max-w-sm bg-white shadow-2xl z-50 transform translate-x-0 transition-transform duration-300 ease-in-out",
                "fixed top-0 right-0 h-full w-4/5 max-w-sm bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out",
            ),
        ),
        rx.el.div(
            on_click=State.close_drawer,
            class_name=rx.cond(
                State.is_drawer_open,
                "fixed inset-0 bg-black/40 z-40 transition-opacity duration-300",
                "hidden",
            ),
        ),
        class_name="sticky top-0 z-30 bg-white/80 backdrop-blur-md shadow-sm",
    )