from django.shortcuts import redirect


def is_sloter_present(slot_no, group):
    for s in group.teamformation_set.all():
        if s.slot_no == slot_no:
            return True
    return False


def allot_random_group(student_profile, batch):
    group = batch.group_set.all()
    for g in group:
        print(g.group_id)
        if not is_sloter_present(student_profile.user.teamformation.slot_no, g):
            student_profile.user.teamformation.group = g
            student_profile.user.teamformation.requests = ""
            student_profile.user.teamformation.save()
            return


def find_professor(id, batch):
    if id != '':
        id = int(id, 10)
        professors = batch.professor.all()

        for p in professors:
            if p.ID == id:
                return p
    return None


def is_available(professor):
    max_limit = professor.max_group
    groups = professor.group_set.all()
    if max_limit > groups.count():
        return True
    else:
        return False


def allot_mentor(batch):
    if batch.professor_data_uploaded:
        student_profile = batch.profile_set.all()
        for s in student_profile:
            if s.user.teamformation.group is None:
                allot_random_group(s, batch)

        groups = batch.group_set.all().order_by("group_id")
        preference_not_filled = []

        for g in groups:
            preference = g.preference_of_professor
            if preference is ',':
                preference_not_filled.append(g)
                continue

            preference = preference.split(',')

            for p in preference:
                prof = find_professor(p, batch)
                if prof is not None:
                    if is_available(prof):
                        print("To group ", g.group_id, " Mentor ", prof.ID)
                        g.mentor = prof  # TODO admin will make sure that there are enough professors available for that batch for that amount of groups
                        g.save()
                        break

        if 0 < preference_not_filled.__len__():

            professors = batch.professor.all()
            i = 0
            for p in professors:
                while is_available(p) and i < preference_not_filled.__len__():
                    preference_not_filled[i].mentor = p
                    preference_not_filled[i].save()
                    i = i + 1

    return redirect("/administrator")