from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ProfessorForm
from .models import Professor


# Create your views here.

@login_required
def professors_list_view(request):
    queryset = request.user.profile.batch.professor.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "professor/display_all.html", context)


@login_required
def professor_create_view(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfessorForm()
    context = {
        'form': form
    }
    return render(request, "professor/create.html", context)


@login_required
def professor_priority(request):
    if request.user.teamformation.slot_no == 1:
        proffs = request.user.profile.batch.professor.all()
        gid = request.user.teamformation.group
        print(gid)
        for u in proffs:
            print(request.GET.get(u.ID))
            if request.GET.get(str(u.ID) + "_add"):
                if gid.preference_of_professor.find(str(u.ID)):
                    print(u.ID)
                    print("Hello")
                else:
                    print(u.ID)
                    print(gid.preference_of_professor)
                    gid.preference_of_professor = gid.preference_of_professor + str(u.ID) + ","
                    print(gid.preference_of_professor)
                    gid.save()

            if request.GET.get(str(u.ID) + "_remove"):
                print("clicked remove")
                if gid.preference_of_professor.find(str(u.ID)):
                    print("***")
                    gid.preference_of_professor = gid.preference_of_professor.replace("," + str(u.ID) + ",", ",")
                    print(gid.preference_of_professor)
                    gid.save()

        context = {
            'proffs': proffs,
            'preference': gid.preference_of_professor
        }
        return render(request, "proff_priority.html", context)
    else:
        return redirect("/")