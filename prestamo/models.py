from django.db import models
class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    herramienta = models.ForeignKey(Herramienta, on_delete=models.PROTECT, db_column='id_herramienta')  # Relación a tabla herramienta (no mostrada en diagrama)
    numero_documento = models.ForeignKey(
        'Usuario',
        to_field='numero_documento',
        on_delete=models.PROTECT,
        db_column='numero_documento'
    )
    id_estado = models.ForeignKey(
        'Estado',
        on_delete=models.PROTECT,
        db_column='id_estado'
    )
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'prestamo'
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'

    def __str__(self):
        return f'Préstamo #{self.id_prestamo}'


class DetallePrestamo(models.Model):
    id_detalle_prestamo = models.AutoField(primary_key=True)
    id_prestamo = models.ForeignKey(
        Prestamo,
        on_delete=models.CASCADE,
        db_column='id_prestamo',
        related_name='detalles'
    )
    herramienta = models.ForeignKey(Herramienta, on_delete=models.PROTECT, db_column='id_herramienta')  # Relación a tabla herramienta (no mostrada en diagrama)
    cantidad = models.PositiveIntegerField()

    class Meta:
        db_table = 'detalle_prestamo'
        verbose_name = 'Detalle de Préstamo'
        verbose_name_plural = 'Detalles de Préstamo'

    def __str__(self):
        return f'Detalle #{self.id_detalle_prestamo} - Préstamo #{self.id_prestamo_id}'


class DevolucionHerramienta(models.Model):
    id_devolucion_herramienta = models.AutoField(primary_key=True)
    id_detalle_prestamo = models.ForeignKey(
        DetallePrestamo,
        on_delete=models.PROTECT,
        db_column='id_detalle_prestamo',
        related_name='devoluciones'
    )
    id_herramienta = models.ForeignKey(Herramienta, on_delete=models.PROTECT, db_column='id_herramienta')  # Relación a tabla herramienta (no mostrada en diagrama)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'devolucion_herramienta'
        verbose_name = 'Devolución de Herramienta'
        verbose_name_plural = 'Devoluciones de Herramienta'

    def __str__(self):
        return f'Devolución #{self.id_devolucion_herramienta}'


# ──────────────────────────────────────────────
# Modelos de referencia (inferidos del diagrama)
# ──────────────────────────────────────────────

class Usuario(models.Model):
    numero_documento = models.CharField(max_length=20, primary_key=True)
    id_rol = models.ForeignKey(
        'Rol',
        on_delete=models.PROTECT,
        db_column='id_rol'
    )
    nombre_completo = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=50)

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre_completo


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'rol'

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'estado'

    def __str__(self):
        return self.nombre