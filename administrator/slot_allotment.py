from allotment.models import Group


def slot_allotment(batch):
    students = (batch.profile_set.all()).order_by("-cpi")
    number_of_groups = batch.number_of_groups
    i = number_of_groups
    j = 1
    for s in students:
        n = int(i/number_of_groups)
        s.user.teamformation.slot_no = n
        i = i+1
        if n == 1:
            group = Group(batch=batch)
            # group.group_id = j
            group.save()
            j = j+1
            s.user.teamformation.group = group
        s.user.teamformation.save()
    batch.number_of_slots = n
    batch.save()

