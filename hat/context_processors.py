def pjax(request):
    return {
        'base_template': 'base_pjax.html' if request.META.get('HTTP_X_PJAX', False) else 'base.html'
    }