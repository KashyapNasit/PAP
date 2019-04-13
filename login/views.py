from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . forms import SignUpForm
from tf.models import TeamFormation
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.cpi = form.cleaned_data.get('cpi')
            user.profile.tier = form.cleaned_data.get('tier')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    # if is_teamformation:
        if  request.user.teamformation.slot_no !=1:
            # print(stri2)
            # g=stri2.len()
            users = User.objects.filter(teamformation__slot_no__exact=1)
            for u in users:
                print(u.teamformation.group_id)
                if request.POST.get(str(u.teamformation.group_id)):
                    std = User.objects.filter(id=u.id)
                    std = std[0]
                    print(std.teamformation.group_id)
                    if is_sloter_present(request.user.teamformation.slot_no, u.teamformation.group):
                        return render(request,'sloter_present.html')
                    else:
                        request.user.teamformation.group_id = u.teamformation.group_id
                        request.user.teamformation.requests = ""
                        request.user.teamformation.save()
                        stri = request.user.teamformation.requests
                        stri2 = stri.split(',')
                        users = User.objects.filter(teamformation__slot_no__exact=-1)
                        context = {
                            "string": stri2,
                            "all": users
                            # "length": g
                        }
                        return render(request, 'normal_login.html', context)
            stri = request.user.teamformation.requests
            stri2 = stri.split(',')
            context = {
                "string": stri2,
                "all": users
                # "length": g
            }
            return render(request,'normal_login.html', context)
        else:
            users = User.objects.filter(teamformation__slot_no__exact=1)
            for u in users:
                print(u.id)
                if request.POST.get(str(u.id)):
                    std = User.objects.filter(id=u.id)
                    std = std[0]
                    print(std.teamformation.requests)
                    std.teamformation.requests = std.teamformation.requests + ',' + str(request.user.teamformation.group_id)
                    std.teamformation.save()
            context = {
                "all":users
            }
            return render(request,'leader_login.html', context)
    # else:
    #     return render(request, 'group.html')
    # return render(request, 'home.html')

def site_home(request):
    return render(request,'site_home.html')

def group(request):
    idd =  request.user.teamformation.group_id
    usrall=User.objects.filter(teamformation__group_id__exact= idd)
    context = {
        "idd": idd,
        "userall" : usrall
    }
    return render(request,'group.html',context)

def is_sloter_present(slot_no, group):
    for s in group.teamformation_set.all():
        if s.slot_no == slot_no:
            return True
    return False


