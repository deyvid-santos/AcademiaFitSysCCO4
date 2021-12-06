from django.urls import path

from academiafitApp.consumers import NotificationsConsumer

ws_patterns=[
    path('ws/notifications/',NotificationsConsumer.as_asgi())
]