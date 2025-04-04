#from .alumno_views import (alumnosupdate, alumnosdelete,
 #                          alumnoslist, alumnoscreate)
from .cliente_views import (
    cliente_create, cliente_list, cliente_delete, cliente_edit
)

from .plato_views import (
    plato_create, plato_list, plato_delete, plato_edit
)

from .mesero_views import (
    mesero_create, mesero_list, mesero_delete, mesero_edit
)

from .mesa_views import (
    mesa_create, mesa_list, mesa_delete, mesa_edit
)

from .orden_views import (
    orden_create, orden_list, orden_delete, orden_close, orden_edit
)
