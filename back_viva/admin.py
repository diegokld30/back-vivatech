from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# ---- Branding básico ----
admin.site.site_header = "Panel de administración · Vivatech"
admin.site.site_title  = "Vivatech Admin"          # <title> del navegador
admin.site.index_title = _("Bienvenido al panel Vivatech")

# (opcional) cambia el icono del navegador añadiendo un favicon en
# templates/admin/base_site.html → ver paso 2.
