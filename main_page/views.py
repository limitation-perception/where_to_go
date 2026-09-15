import random
from datetime import date

from django.http import Http404
from django.shortcuts import redirect, render

from .forms import ParticipantForm

places = [
    {
        "id": 1,
        "name": "Tbiliso",
        "type": "cafe",
        "location": "next to Mohyla",
        "rating": 5,
        "created_at": "06.08.2025",
        "description": (
            "it's a nice cafe where you can buy hinkali and eat some other "
            "Georgian food. There are also great beverages"
        ),
    },
    {
        "id": 2,
        "name": "Fido",
        "type": "learning_place",
        "location": "next to 4 campus",
        "rating": 3,
        "created_at": "14.09.2026",
        "description": (
            "it's a horrible place where you can`t do anything because of "
            "the terrible aura there. we bought a fridge recently"
        ),
    },
    {
        "id": 3,
        "name": "puzatka",
        "type": "restaurant",
        "location": "",
        "rating": 5,
        "created_at": "03.09.2026",
        "description": (
            "it's a cozy, appealing place where you can buy some great food "
            "but usually people go there just to talk."
        ),
    },
]


def where_to_go(request):
    place = None
    if request.method == "POST":
        ratings = [p["rating"] for p in get_places(request)]
        place = random.choices(get_places(request), weights=ratings)[0]
    return render(request, "main_page/main_page.html", {"place": place})


def get_places(request):
    if "places" not in request.session:
        request.session["places"] = places.copy()
    return request.session["places"]


def show_places(request):
    return render(
        request, "places_list/places.html", {"places": get_places(request)}
    )


def place_detail(request, id):
    for place in get_places(request):
        if place["id"] == id:
            return render(
                request, "place_detail/place_detail.html", {"place": place}
            )
    raise Http404("Didn`t find the page")


def add_places(request):
    form = ParticipantForm()
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            place = form.cleaned_data
            name = place["name"].casefold()
            if any(name == p["name"].casefold() for p in get_places(request)):
                form.add_error("name", "That place is already listed")
            else:
                place["created_at"] = date.today().strftime("%d.%m.%Y")
                place["id"] = max(p["id"] for p in get_places(request)) + 1
                get_places(request).append(place)
                request.session.modified = True
                return redirect("main_page:show_places")

    context = {"form": form, "places": get_places(request)}
    return render(request, "add_places/add_places.html", context)
