from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def cube_surface_area_calculator(request):
    cube_len = ""
    cube_surface_area = ""

    if request.method == "POST":
        cube_len = request.POST.get("cube_len")
        button = request.POST.get("button")

        if button == "Очистить":
            cube_len = ""

        elif button == "Вычислить" and len(cube_len) > 0:
            cube_surface_area = round(6 * pow(int(cube_len), 2), 2)

    context = {"cube_len": cube_len, "cube_surface_area": cube_surface_area}
    return render(request, "cube_surface_area_calculator.html", context)
