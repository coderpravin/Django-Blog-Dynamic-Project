from django.apps import AppConfig


class MainblogConfig(AppConfig):
    name = 'mainBlog'

    def ready(self):
        import mainBlog.signals