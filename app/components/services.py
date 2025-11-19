import reflex as rx
from app.states.state import State, Service


def service_card(service: Service) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(service["icon"], class_name="h-10 w-10 text-sky-500 mb-4"),
            rx.el.h3(
                service["title"], class_name="text-xl font-bold text-gray-800 mb-2"
            ),
            rx.el.p(service["description"], class_name="text-gray-600 text-sm"),
            class_name="p-6",
        ),
        class_name="bg-white rounded-xl shadow-sm border border-gray-100 transform hover:-translate-y-1 hover:shadow-lg transition-all duration-300 h-full",
    )


def services_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "What I Offer",
                class_name="text-3xl font-bold text-gray-800 mb-12 text-center",
            ),
            rx.el.div(
                rx.foreach(State.services, service_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="services",
        class_name="py-24 bg-gray-50",
    )