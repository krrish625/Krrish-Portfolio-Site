import reflex as rx


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Krrish Jha",
                    class_name="text-5xl md:text-7xl font-extrabold text-gray-800 tracking-tighter",
                ),
                rx.el.p(
                    "Data Scientist & AI/ML Developer",
                    class_name="mt-4 text-lg md:text-2xl font-medium text-transparent bg-clip-text bg-gradient-to-r from-sky-500 to-blue-600",
                ),
                rx.el.p(
                    "Transforming complex data into intelligent solutions. Passionate about building scalable AI applications that drive business value.",
                    class_name="mt-6 max-w-2xl text-gray-500 text-base md:text-lg",
                ),
                rx.el.div(
                    rx.el.button(
                        "View My Work",
                        rx.icon("arrow-down", class_name="ml-2 h-4 w-4"),
                        on_click=rx.scroll_to("projects"),
                        class_name="bg-sky-500 text-white px-8 py-3 rounded-lg font-semibold hover:bg-sky-600 transition-all duration-300 shadow-lg hover:shadow-sky-300/50 transform hover:-translate-y-0.5 flex items-center",
                    ),
                    rx.el.a(
                        rx.el.button(
                            "Get In Touch",
                            on_click=rx.scroll_to("contact"),
                            class_name="bg-gray-100 text-gray-700 px-8 py-3 rounded-lg font-semibold hover:bg-gray-200 transition-colors duration-300 border border-gray-200",
                        ),
                        href="#contact",
                    ),
                    class_name="mt-10 flex flex-col sm:flex-row items-center gap-4",
                ),
                class_name="text-center flex flex-col items-center",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 z-10 relative",
        ),
        rx.el.div(
            class_name="absolute inset-0 bg-gradient-to-br from-sky-50 via-white to-blue-100 opacity-50"
        ),
        rx.el.div(
            class_name="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_400px_at_50%_300px,_#bae6fd,_transparent)]"
        ),
        class_name="relative flex items-center justify-center min-h-[calc(100vh-80px)] py-20 overflow-hidden",
    )