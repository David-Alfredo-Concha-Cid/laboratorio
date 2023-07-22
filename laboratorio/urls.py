from django.urls import path
from .views import v_laboratorio_create, v_laboratorio_edit
from .views import v_laboratorio_list, v_laboratorio_delete

urlpatterns = [
    path('laboratorio/create', v_laboratorio_create),
    path('laboratorio/<int:laboratorio_id>/edit', v_laboratorio_edit),
    path('laboratorio/list', v_laboratorio_list),
    path('laboratorio/<int:laboratorio_id>/delete', v_laboratorio_delete)
]