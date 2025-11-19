import reflex as rx
from app.states.state import State


def social_link(icon: str, href: str, is_external: bool = True) -> rx.Component:
    return rx.el.a(
        rx.icon(
            icon,
            class_name="h-7 w-7 text-gray-500 hover:text-sky-600 transition-colors",
        ),
        href=href,
        is_external=is_external,
    )


def contact_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Get In Touch",
                class_name="text-3xl font-bold text-gray-800 mb-4 text-center",
            ),
            rx.el.p(
                "Have a project in mind or just want to say hello? I'd love to hear from you.",
                class_name="text-center text-gray-600 max-w-2xl mx-auto text-lg mb-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Contact Information",
                        class_name="text-2xl font-semibold text-gray-800 mb-4",
                    ),
                    rx.el.p(
                        "Feel free to reach out via email or connect with me on social media. I'm always open to discussing new projects, creative ideas, or opportunities to be part of an amazing team.",
                        class_name="text-gray-600 mb-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon("mail", class_name="h-5 w-5 text-sky-500 mr-3"),
                            rx.el.span(
                                "krrish.jha@email.com", class_name="text-gray-700"
                            ),
                            class_name="flex items-center mb-4",
                        ),
                        rx.el.div(
                            rx.icon("map-pin", class_name="h-5 w-5 text-sky-500 mr-3"),
                            rx.el.span("San Francisco, CA", class_name="text-gray-700"),
                            class_name="flex items-center mb-8",
                        ),
                    ),
                    rx.el.div(
                        social_link("github", "#"),
                        social_link("linkedin", "#"),
                        social_link("twitter", "#"),
                        social_link(
                            "mail", "mailto:krrish.jha@email.com", is_external=False
                        ),
                        class_name="flex items-center space-x-6",
                    ),
                    class_name="p-8 bg-gray-50 rounded-xl border border-gray-100",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Full Name",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            name="name",
                            placeholder="Your Name",
                            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-shadow",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Email Address",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.input(
                            name="email",
                            type="email",
                            placeholder="your.email@example.com",
                            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-shadow",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Message",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.textarea(
                            name="message",
                            placeholder="Your message...",
                            rows=5,
                            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-shadow",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.button(
                        "Send Message",
                        rx.icon("send", class_name="ml-2 h-4 w-4"),
                        type="submit",
                        class_name="w-full bg-sky-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-sky-600 transition-all duration-300 shadow-lg hover:shadow-sky-300/50 flex items-center justify-center",
                    ),
                    on_submit=State.submit_contact_form,
                    reset_on_submit=True,
                    class_name="p-8 bg-white rounded-xl shadow-sm border border-gray-100",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-6xl mx-auto",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="contact",
        class_name="py-24 bg-white",
    )