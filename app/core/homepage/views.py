from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'homepage.html'



#class LogoutRedirectView(RedirectView):
#    pattern_name = 'login'

#    def dispatch(self, request, *args, **kwargs):
#        logout(request)
#        return super().dispatch(request, *args, **kwargs)