def baseurl(request):
    """
    Return a BASE_URL template context for the current request.
    """
    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'

    return {'BASE_URL': scheme + request.get_host(),}


#from ecommerce.models import Category
from qipt import settings

def telephony(request):

    if 'username' in request.session:
        return {
            #        'active_categories': Category.objects.filter(is_active=True),
            #        'site_name': settings.SITE_NAME,
            #        'meta_keywords': settings.META_KEYWORDS,
            #        'meta_description': settings.META_DESCRIPTION,
                    'username': request.session['username'],
        }

    return {'test': 'test'}
