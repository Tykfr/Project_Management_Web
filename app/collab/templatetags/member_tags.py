from django import template
register = template.Library()

@register.filter
def is_project_member(project,user):
    if(project.boss == user):
        return True
    for objective in project.objective_set.all():
        if(user in objective.members):
            return True

    return False

@register.filter
def can_see_post(post,user):
    return (user in post.member)

@register.filter
def is_team_leader(objective,user):
    member = [member for member in objective.members.all() if (user == member)]
    return (member and member[0].team_leader or user == objective.project.boss)

@register.filter
def not_completed(objectives):
    return [objective for objective in objectives if (not objective.completed)]

@register.filter
def completed(objectives):
    return [objective for objective in objectives if (objective.completed)]
