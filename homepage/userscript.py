from homepage.models import MySystem, User


def add_location(location):
    lo = MySystem.objects.get_or_create(location=location)[0]
    lo.save()
