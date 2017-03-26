from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
def require_role(role="user"):
    def _dec(fn):
        def wrapper(request,*args,**kwargs):
            request.session['pre_url']=request.path
            if not request.user.is_authenticated():
                return HttpResponseRedirect(reverse('login'))
            else:
                return HttpResponseRedirect(reverse('index'))
            return fn(request,*args,**kwargs)
        return wrapper
    return _dec
