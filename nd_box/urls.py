from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    ## DEV Path
    # path('', include('core.urls')),
    # path('manager/', admin.site.urls),
    # path('carreiras/', include('carreiras.urls')),
    # path('reports/', include('reports.urls')),
    # path('privacidade/', include('privacidade.urls')),
    # path('autorizacoes/', include('autorizacoes.urls')),
    # path('jund/', include('jund.urls')),
    ## IIS Path
    path('nd_box_hml/', include('core.urls')),
    path('nd_box_hml/manager/', admin.site.urls),
    path('nd_box_hml/carreiras/', include('carreiras.urls')),
    path('nd_box_hml/reports/', include('reports.urls')),
    path('nd_box_hml/privacidade/', include('privacidade.urls')),
    path('nd_box_hml/autorizacoes/', include('autorizacoes.urls')),
    path('nd_box_hml/jund/', include('jund.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Gestão ND Box'
admin.site.site_title = 'Gestão ND Box'
admin.site.index_title = 'Área Administrativa'
