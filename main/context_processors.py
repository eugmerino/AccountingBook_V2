def user_details(request):
    if request.user.is_authenticated:
        return {
            'user_full_name': request.user.get_full_name(),
            'user_email': request.user.email,
            'user_groups': request.user.groups.all(),  # Si quieres mostrar los grupos
        }
    return {}