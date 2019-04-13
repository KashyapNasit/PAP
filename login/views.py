from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . forms import SignUpForm
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
        if request.user.is_staff:
            return redirect('/administrator/')
        elif request.user.teamformation.slot_no != 1:
            if (request.user.teamformation.group is None) and request.user.profile.batch.is_team_formation_allowed:
                print(request.user.profile.batch.is_team_formation_allowed)
                users = User.objects.filter(teamformation__slot_no__exact=1)  # Come bake here and fix this.....non leader ke page pe sare log dikh rahe hai naki jisne request bheji ho
                for u in users:
                    print(u.teamformation.group_id)
                    if request.POST.get(str(u.teamformation.group_id)+'_accept'):
                        std = User.objects.filter(id=u.id)
                        std = std[0]
                        print(std.teamformation.group_id)
                        if is_sloter_present(request.user.teamformation.slot_no, u.teamformation.group):
                            request.user.teamformation.requests.replace(','+str(u.teamformation.group)+',', ',')
                            request.user.teamformation.save()
                            return render(request,'sloter_present.html')
                        else:
                            request.user.teamformation.group_id = u.teamformation.group_id
                            request.user.teamformation.requests = ""
                            request.user.teamformation.save()
                            stri = request.user.teamformation.requests
                            stri2 = stri.split(',')
                            # users = User.objects.filter(teamformation__slot_no__exact=1)
                            user = []
                            return render(request, 'normal_login.html')

                    elif request.POST.get(str(u.teamformation.group_id)+'_reject'):
                        request.user.teamformation.requests.replace(',' + str(u.teamformation.group.group_id) + ',', ',')
                        request.user.teamformation.save()
                        print("reject : ", u.teamformation.group_id,request.user.teamformation.requests )


                stri = request.user.teamformation.requests
                stri2 = stri.split(',')
                context = {
                    "string": stri2,
                    "all": users
                    # "length": g
                }
                return render(request, 'normal_login.html', context)
            else:
                return render(request, 'normal_login.html')
        else:
            if request.user.profile.batch.is_team_formation_allowed:
                users = User.objects.filter(teamformation__slot_no__gt=1)
                number_of_slots = request.user.profile.batch.number_of_slots
                available_users = []

                for u in users:
                    print(u.id)
                    if request.POST.get(str(u.id)):
                        std = User.objects.filter(id=u.id)
                        std = std[0]
                        print(std.teamformation.requests)
                        std.teamformation.requests = std.teamformation.requests + str(request.user.teamformation.group_id) +','
                        request.user.teamformation.requests = request.user.teamformation.requests + str(std.id) + ','
                        request.user.teamformation.save()
                        std.teamformation.save()
                    if u.teamformation.group is None:
                        available_users.append(u)

                sent_requests = request.user.teamformation.requests.split(',')
                print("Hello", sent_requests)

                aaa = []

                for u in available_users:
                    if not str(u.id) in sent_requests:
                        aaa.append(u)
                print(aaa,available_users)
                context = {
                    "all": aaa,
                    "range": range(number_of_slots+1),
                    "sent_requests": sent_requests,
                }
                return render(request, 'leader_login.html', context)
            else:
                return render(request, 'leader_login.html')
    # else:
    #     return render(request, 'group.html')
    # return render(request, 'home.html')


def site_home(request):
    return render(request, 'site_home.html')


@login_required()
def group(request):
    idd = request.user.teamformation.group
    if idd is None:
        return render(request, 'group.html', { 'idd' : -1})

    usrall = User.objects.filter(teamformation__group_id__exact=idd.group_id)
    context = {
        "idd": idd.group_id,
        "userall" : usrall
    }
    return render(request, 'group.html', context)


def is_sloter_present(slot_no, group):
    for s in group.teamformation_set.all():
        if s.slot_no == slot_no:
            return True
    return False


