# Backend preparado para BilleterAPP Ionic

Ejecuta:

```bash
python run.py
```

API: `http://localhost:5000/api/v1`

CORS preparado para Ionic (`localhost:8100`) y Capacitor.

La mini app movil consume:
- `/auth/login`
- `/clientes/`
- `/categorias/`
- `/productos/`

Categorias quedo sin restriccion de rol unicamente para facilitar el CRUD de la mini app. Para producci0n, volver a aplicar `rol_required("Administrador")`.
