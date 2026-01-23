# [UT06](./index.md)

## PR0601: Campos del modelo
```
PR0601: Campos del modelo

1.- En Docker Desktop en la terminal vamos a la carpeta volumesOdoo y ejecutamos docker exec -ti odoo_prod bash y luego odoo scaffold gestion_productos mnt/extra-addons para crear gestion_productos.

2.- En gestion_productos vamos a __manifest__.py y modificamos su código. En models -> models.py
modificamos su código y en views -> views.py modificamos su código.
```
![Imagen](image.png)

## Codigo 601
```
__manifest__.py

# -*- coding: utf-8 -*-
{
    'name': "Gestion Productos",

    'summary': """
        Modulo de Gestion de Productos""",

    'author': "Leonb",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}



models.py

# -*- coding: utf-8 -*-

from odoo import models, fields


class GestionProductos(models.Model):
    _name = 'gestion_productos.gestion_productos'
    _description = 'Gestión de Productos'

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Char(string="Descripción")

    codProducto = fields.Integer(
        string="Código de Producto",
        required=True
    )

    imaProducto = fields.Image(string="Imagen")

    categoria = fields.Selection([
        ('jardin', 'Jardín'),
        ('hogar', 'Hogar'),
        ('electrodomesticos', 'Electrodomésticos')
    ], string="Categoría")

    tipoProducto = fields.Boolean(string="Tipo de Producto")

    currency_id = fields.Many2one(
        'res.currency',
        string='Moneda',
        required=True,
        default=lambda self: self.env.company.currency_id
    )

    precVenta = fields.Monetary(
        string="Precio de Venta",
        currency_field='currency_id'
    )

    stockDisponible = fields.Integer(string="Stock Disponible")

    fechCreacion = fields.Date(string="Fecha de Creación")
    fechUltAct = fields.Date(string="Fecha Última Actualización")

    activo = fields.Boolean(
        string="Activo",
        default=True
    )

    peso = fields.Float(string="Peso")


views.py

<odoo>
  <data>

    <!-- LIST VIEW -->
    <record model="ir.ui.view" id="gestion_productos.list">
      <field name="name">gestion_productos list</field>
      <field name="model">gestion_productos.gestion_productos</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="descripcion"/>
          <field name="codProducto"/>
          <field name="categoria"/>
          <field name="precVenta"/>
          <field name="stockDisponible"/>
          <field name="activo"/>
        </tree>
      </field>
    </record>

    <!-- ACTION -->
    <record model="ir.actions.act_window" id="gestion_productos.action_window">
      <field name="name">Productos</field>
      <field name="res_model">gestion_productos.gestion_productos</field>
      <field name="view_mode">tree,form</field>
    </record>

    <!-- MENUS -->
    <menuitem name="Gestión Productos" id="gestion_productos.menu_root"/>
    <menuitem name="Productos"
              id="menu_productos"
              parent="gestion_productos.menu_root"
              action="gestion_productos.action_window"/>

  </data>
</odoo>


```

## PR0602: Campos del modelo
```
PR0602: Campos del modelo

1.- En Docker Desktop en la terminal vamos a la carpeta volumesOdoo y ejecutamos docker exec -ti odoo_prod bash y luego odoo scaffold library_lgn mnt/extra-addons para crear library_lgn.

2.- Creamos en views/ library_autor.xml, library_genero.xml, library_libro.xml, library_socio.xml y library_views.xml y en models/ library_author.py, library_book.py, library_genero.py y library_socio.py.

3.- En library_lgn vamos a __manifest__.py y modificamos su código. En models -> __init__.py
modificamos su código, en security -> ir.model.access.csv modificamos su código.

```

![Imagen](<Captura de pantalla (346).png>)

## Codigo 602
```
manifest.py

# -*- coding: utf-8 -*-
{
    'name': "Library Lgn",

    'author': "leonb",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_autor.xml',
        'views/library_libro.xml',
        'views/library_socio.xml',
        'views/library_genero.xml',
        'views/library_views.xml',
    ],
    # only loaded in demonstration mode
    'application': True,
}


library_autor.xml

<odoo>
    <data>
        <record id="view_library_lgn_autor_form" model="ir.ui.view">
            <field name="name">library_lgn.autor.form</field>
            <field name="model">library_lgn.autor</field>
            <field name="arch" type="xml">
                <form>
                    <sheet>
                        <group>
                            <field name="nombre"/>
                            <field name="paisorigen"/>
                        </group>

                        <notebook>
                            <page string="Libros como autor">
                                <field name="libro_autor_ids"/>
                            </page>

                            <page string="Libros como revisor">
                                <field name="libro_revisor_ids"/>
                            </page>
                        </notebook>
                    </sheet>
                </form>
            </field>
        </record>

        <record id="view_library_lgn_autor_tree" model="ir.ui.view">
            <field name="name">library_lgn.autor.tree</field>
            <field name="model">library_lgn.autor</field>
            <field name="arch" type="xml">
                <tree>
                    <field name="nombre"/>
                    <field name="paisorigen"/>
                </tree>
            </field>
        </record>

        <record id="action_library_lgn_authors" model="ir.actions.act_window">
            <field name="name">Autores</field>
            <field name="res_model">library_lgn.autor</field>
            <field name="view_mode">tree,form</field>
        </record>
    </data>
</odoo>


library_genero.xml

<odoo>
    <data>
        <record id="view_library_lgn_genero_form" model="ir.ui.view">
            <field name="name">library_lgn.genero.form</field>
            <field name="model">library_lgn.genero</field>
            <field name="arch" type="xml">
                <form>
                    <sheet>
                        <field name="name"/>
                    </sheet>
                </form>
            </field>
        </record>

        <record id="view_library_lgn_genero_tree" model="ir.ui.view">
            <field name="name">library_lgn.genero.tree</field>
            <field name="model">library_lgn.genero</field>
            <field name="arch" type="xml">
                <tree>
                    <field name="name"/>
                </tree>
            </field>
        </record>

        <record id="action_library_lgn_genero" model="ir.actions.act_window">
            <field name="name">Géneros</field>
            <field name="res_model">library_lgn.genero</field>
            <field name="view_mode">tree,form</field>
            <field name="view_id" ref="view_library_lgn_genero_tree"/>
        </record>
    </data>
</odoo>


library_libro.xml

<odoo>
    <data>
        <record id="view_library_lgn_libro_form" model="ir.ui.view">
            <field name="name">library_lgn.libro.form</field>
            <field name="model">library_lgn.libro</field>
            <field name="arch" type="xml">
                <form>
                    <sheet>
                        <group>
                            <field name="titulo"/>
                            <field name="genero_id"/>
                        </group>

                        <group string="Participantes">
                            <field name="autor_ids" widget="many2many_tags"/>
                            <field name="revisor_ids" widget="many2many_tags"/>
                        </group>

                        <group>
                            <field name="socios"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>


        <record id="view_library_lgn_libro_tree" model="ir.ui.view">
            <field name="name">library_lgn.libro.tree</field>
            <field name="model">library_lgn.libro</field>
            <field name="arch" type="xml">
                <tree>
                    <field name="titulo"/>
                    <field name="autor_ids"/>
                    <field name="revisor_ids"/>
                    <field name="genero_id"/>
                </tree>
            </field>
        </record>


        <record id="action_library_lgn_libro" model="ir.actions.act_window">
            <field name="name">Libros</field>
            <field name="res_model">library_lgn.libro</field>
            <field name="view_mode">tree,form</field>
        </record>

    </data>
</odoo>


library_socio.xml

<odoo>
    <data>
        <record id="view_library_lgn_socio_form" model="ir.ui.view">
            <field name="name">library_lgn.socio.form</field>
            <field name="model">library_lgn.socio</field>
            <field name="arch" type="xml">
                <form>
                    <sheet>
                        <field name="nombre"/>
                        <field name="tele"/>
                        <field name="libros"/>
                    </sheet>
                </form>
            </field>
        </record>

        <record id="view_library_lgn_socio_tree" model="ir.ui.view">
            <field name="name">library_lgn.socio.tree</field>
            <field name="model">library_lgn.socio</field>
            <field name="arch" type="xml">
                <tree>
                    <field name="nombre"/>
                    <field name="tele"/>
                </tree>
            </field>
        </record>

        <record id="action_library_lgn_socio" model="ir.actions.act_window">
            <field name="name">Socios</field>
            <field name="res_model">library_lgn.socio</field>
            <field name="view_mode">tree,form</field>
            <field name="view_id" ref="view_library_lgn_socio_tree"/>
        </record>
    </data>
</odoo>


library_views.xml

<odoo>
    <data>
        <menuitem id="menu_library_lgn_root" name="Libreria LGN" sequence="10"/>

        <menuitem id="menu_library_lgn_authors"
                  name="Autores"
                  parent="menu_library_lgn_root"
                  action="action_library_lgn_authors"/>

        <menuitem id="menu_library_lgn_libros"
                  name="Libros"
                  parent="menu_library_lgn_root"
                  action="action_library_lgn_libro"/>

        <menuitem id="menu_library_lgn_socios"
                  name="Socios"
                  parent="menu_library_lgn_root"
                  action="action_library_lgn_socio"/>

        <menuitem id="menu_library_lgn_genero"
                  name="Generos"
                  parent="menu_library_lgn_root"
                  action="action_library_lgn_genero"/>
    </data>
</odoo>


ir.model.access.csv

id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_library_libro,access_library_libro,model_library_lgn_libro,base.group_user,1,1,1,1
access_library_autor,access_library_autor,model_library_lgn_autor,base.group_user,1,1,1,1
access_library_socio,access_library_socio,model_library_lgn_socio,base.group_user,1,1,1,1
access_library_genero,access_library_genero,model_library_lgn_genero,base.group_user,1,1,1,1


library_author.py

from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library_lgn.autor'
    _description = 'Autor / Revisor'

    nombre = fields.Char(string='Nombre', required=True)
    paisorigen = fields.Many2one('res.country', string='País de origen')

    libro_autor_ids = fields.Many2many(
        'library_lgn.libro',
        'library_libro_autor_rel',
        'autor_id',
        'libro_id',
        string='Libros como autor'
    )

    libro_revisor_ids = fields.Many2many(
        'library_lgn.libro',
        'library_libro_revisor_rel',
        'autor_id',
        'libro_id',
        string='Libros como revisor'
    )


library_book.py

from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library_lgn.libro'
    _description = 'Libro'

    titulo = fields.Char(string='Nombre', required=True)

    autor_ids = fields.Many2many(
        'library_lgn.autor',
        'library_libro_autor_rel',
        'libro_id',
        'autor_id',
        string='Autores'
    )

    revisor_ids = fields.Many2many(
        'library_lgn.autor',
        'library_libro_revisor_rel',
        'libro_id',
        'autor_id',
        string='Revisores'
    )

    genero_id = fields.Many2one('library_lgn.genero', string='Género')

    socios = fields.Many2many(
        'library_lgn.socio',
        string='Prestado a'
    )


library_genero.py

from odoo import models, fields

class LibraryGenero(models.Model):
    _name = 'library_lgn.genero'
    _description = 'Genero'

    name = fields.Char(string='Género', required=True)
    libro_ids = fields.One2many('library_lgn.libro', 'genero_id', string='Libros')


library_socio.py

from odoo import models, fields

class LibrarySocio(models.Model):
    _name = 'library_lgn.socio'
    _description = 'Socio libreria'

    nombre = fields.Char(string='Nombre', required=True)
    tele = fields.Char(string='Teléfono')
    libros = fields.Many2many('library_lgn.libro', string='Libros prestados')

```


## PR0603: Campos calculados y restricciones
```
PR0603: Campos calculados y restricciones

1.- En Docker Desktop en la terminal vamos a la carpeta volumesOdoo y ejecutamos docker exec -ti odoo_prod bash y luego odoo scaffold stock_management mnt/extra-addons para crear stock_management.

2.- Creamos en views/ menu.xml y en models/ stock_product.py.

3.- En stock_management vamos a __manifest__.py y modificamos su código, en views vamos a views.xml y modificamos su código, en models -> __init__.py y modificamos su código, en security -> ir.model.access.csv modificamos su código.

```

![Imagen](<Captura de pantalla (347).png>)

## Codigo 603
```
__manifest__.py

{
    'name': "Stock Management",
    'summary': "Gestión de inventario",
    'description': "Módulo para manejar productos y stock",
    'author': "leonb",
    'website': "https://www.yourcompany.com",
    'category': 'Inventory',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/views.xml',
    ],

    'application': True,
}


menu.xml

<odoo>
    <data>
        <record id="action_stock_product" model="ir.actions.act_window">
            <field name="name">Stock Management</field>
            <field name="res_model">stock.product</field>
            <field name="view_mode">tree,form</field>
        </record>

        <menuitem id="menu_stock_root" name="Stock Management"/>

        <menuitem id="menu_stock_management"
                  name="Stock Management"
                  parent="menu_stock_root"
                  action="action_stock_product"/>
    </data>
</odoo>


views.xml

<odoo>
    <data>
        <record id="view_stock_product_tree" model="ir.ui.view">
            <field name="name">stock.product.tree</field>
            <field name="model">stock.product</field>
            <field name="arch" type="xml">
                <tree string="Productos">
                    <field name="name"/>
                    <field name="category"/>
                    <field name="price"/>
                    <field name="quantity"/>
                    <field name="total_value"/>
                    <field name="stock_status"/>
                    <field name="full_name"/>
                </tree>
            </field>
        </record>

        <record id="view_stock_product_form" model="ir.ui.view">
            <field name="name">stock.product.form</field>
            <field name="model">stock.product</field>
            <field name="arch" type="xml">
                <form string="Producto">
                    <sheet>
                        <group>
                            <field name="name"/>
                            <field name="category"/>
                            <field name="price"/>
                            <field name="quantity"/>
                            <field name="total_value"/>
                            <field name="minimum_quantity"/>
                            <field name="stock_status"/>
                            <field name="full_name"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>
    </data>
</odoo>


ir.model.access.csv

id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_stock_product_user,stock.product user,model_stock_product,base.group_user,1,1,1,1


__init__.py

# -*- coding: utf-8 -*-

from . import stock_product


stock_product.py

# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class stock_product(models.Model):
    _name = 'stock.product'
    _description = 'stock.product'
    _sql_constraints=[
        ('unique_name','unique(name)','El nombre debe ser unico'),
        ('check_price','CHECK(price > 0)','El precio debe ser positivo')]

    name = fields.Char()
    category = fields.Selection([
        ('televisor','Televisor'),
        ('movil','Movil'),
        ('ordenador','Ordenador'),
        ('microprocesadores','Microprocesadores')
    ])
    price = fields.Integer()
    quantity = fields.Integer()
    total_value = fields.Char(compute="_total", string='Total')
    minimum_quantity = fields.Integer()
    stock_status = fields.Selection([
        ('normal','Normal'),
        ('low_stock','Low Stock')
    ], compute='_compute_stock_status', store=True)
    full_name = fields.Text(compute="_full_name", string='Nombre completo')


    @api.constrains('price')
    def _price(self):
        for record in self:
            if record.price < 0:
                raise ValidationError('El precio debe ser > 0')
    @api.constrains('quantity')
    def _quantity(self):
        for record in self:
            if record.quantity <= 0:
                raise ValidationError('El cantidad debe ser >= 0')
            if record.quantity > 100000:
                raise ValidationError('El cantidad debe ser < 100000')
    @api.depends('quantity', 'minimum_quantity')
    def _compute_stock_status(self):
        for record in self:
            if record.quantity < record.minimum_quantity:
                record.stock_status = 'low_stock'
            else:
                record.stock_status = 'normal'
    @api.constrains('category')
    def _category(self):
        for record in self:
            if not record.category:
                raise ValidationError('Debe seleccionar una categoría')


    @api.depends('price','quantity')
    def _total(self):
        for record in self:
            record.total_value = record.price * record.quantity
    @api.depends('name', 'category')
    def _full_name(self):
        for record in self:
            record.full_name = (record.name or "") + " (" + (record.category or "") + ")"
```



## PR0604: Vista de tipo lista
```
PR0604: Vista de tipo lista

1.- En Docker Desktop en la terminal vamos a la carpeta volumesOdoo y ejecutamos docker exec -ti odoo_prod bash y luego odoo scaffold subscription mnt/extra-addons para crear subscription.

2.- En subscription vamos a __manifest__.py y modificamos su código, en views vamos a views.xml y modificamos su código, en models -> models.py.

```

![Imagen](<Captura de pantalla (348).png>)

## Codigo 604
```
models.py

# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api

class Subscription(models.Model):
    _name = 'subscription.subscription'
    _description = 'Gestión de Suscripciones'
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'El nombre de la suscripción debe ser único')
    ]

    name = fields.Char(string='Nombre', required=True)
    customer_id = fields.Many2one('res.partner', required=True)
    subscription_code = fields.Char(string='Código de Suscripción', required=True)
    start_date = fields.Date(string='Fecha Inicio', required=True)
    end_date = fields.Date(string='Fecha Fin')
    duration_months = fields.Integer(string='Duración (meses)', compute='_compute_duration')
    renewal_date = fields.Date(string='Fecha de Renovación')
    status = fields.Selection([
        ('active', 'Activa'),
        ('expired', 'Vencida'),
        ('pending', 'Pendiente'),
        ('cancelled', 'Cancelada')
    ], string='Estado', default='pending')
    is_renewable = fields.Boolean(string='Renovable automáticamente')
    auto_renewal = fields.Boolean(string='Renovación automática')
    price = fields.Float(string='Precio')
    usage_limit = fields.Integer(string='Límite de Uso')
    current_usage = fields.Integer(string='Servicios Utilizados')
    use_percent = fields.Float(string='Porcentaje de Uso', compute='_compute_use_percent')


    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration_months = (record.end_date.year - record.start_date.year) * 12 + \
                                         (record.end_date.month - record.start_date.month)
            else:
                record.duration_months = 0

    @api.depends('current_usage', 'usage_limit')
    def _compute_use_percent(self):
        for record in self:
            if record.usage_limit:
                record.use_percent = (record.current_usage / record.usage_limit) * 100
            else:
                record.use_percent = 0

    def aumento(self):
        """Añade 15 días a la fecha de fin de la suscripción"""
        for record in self:
            if record.end_date:
                record.end_date += timedelta(days=15)


views.xml

<odoo>
  <data>
    <record id="view_subscription_tree_basic" model="ir.ui.view">
      <field name="name">subscription.tree.basic</field>
      <field name="model">subscription.subscription</field>
      <field name="arch" type="xml">
        <tree string="Suscripciones" decoration-danger="status=='expired'" decoration-warning="status=='cancelled'">
          <field name="name"/>
          <field name="customer_id"/>
          <field name="subscription_code"/>
          <field name="start_date"/>
          <field name="end_date" widget="remaining_days"/>
          <field name="duration_months"/>
          <field name="renewal_date"/>
          <field name="status" widget="radio"/>
          <field name="is_renewable"/>
          <field name="auto_renewal"/>
          <field name="price" attrs="{'invisible':[('status','=','cancelled')]}"/>
          <button name="aumento" type="object" string="+15 días" class="btn-primary" icon="fa-gift"/>
        </tree>
      </field>
    </record>

    <record id="view_subscription_tree_usage" model="ir.ui.view">
      <field name="name">subscription.tree.usage</field>
      <field name="model">subscription.subscription</field>
      <field name="arch" type="xml">
        <tree string="Suscripciones Uso" decoration-danger="use_percent&gt;=80">
          <field name="name"/>
          <field name="usage_limit" widget="progressbar"/>
          <field name="current_usage"/>
          <field name="use_percent" avg="1"/>
        </tree>
      </field>
    </record>

    <record id="action_subscription_basic" model="ir.actions.act_window">
      <field name="name">Suscripciones (Básico)</field>
      <field name="res_model">subscription.subscription</field>
      <field name="view_mode">tree,form</field>
      <field name="view_id" ref="view_subscription_tree_basic"/>
    </record>

    <record id="action_subscription_usage" model="ir.actions.act_window">
      <field name="name">Suscripciones (Uso)</field>
      <field name="res_model">subscription.subscription</field>
      <field name="view_mode">tree,form</field>
      <field name="view_id" ref="view_subscription_tree_usage"/>
    </record>

    <menuitem id="menu_subscription_root" name="Suscripciones"/>
    <menuitem id="menu_subscription_basic" name="Básico" parent="menu_subscription_root" action="action_subscription_basic"/>
    <menuitem id="menu_subscription_usage" name="Uso" parent="menu_subscription_root" action="action_subscription_usage"/>
  </data>
</odoo>


__manifest__.py

{
    'name': 'Gestión de Suscripciones',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Módulo para gestionar suscripciones',
    'depends': ['base'],
    'data': [
        
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}
```


## PR0606: Gestión de un taller mecánico
```
PR0606: Gestión de un taller mecánico

1.- En Docker Desktop en la terminal vamos a la carpeta volumesOdoo y ejecutamos docker exec -ti odoo_prod bash y luego odoo scaffold taller_mecanico mnt/extra-addons para crear taller_mecanico.

2.- En taller_mecanico vamos a models/ y creamos cliente.py, pieza.py, reparacion.py y vehiculo.py y modificamos __init__.py, en views/ creamos menu.xml, cliente.xml, pieza.xml, reparacion.xml y vehiculo.xml y entramos en security/ ir.model.access.csv modificamos su código, entramos en __manifest__.py y modificamos su código.

```

![Imagen](<Captura de pantalla (358).png>)

## Codigo 606
```
__init__.py

# -*- coding: utf-8 -*-

from . import cliente
from . import vehiculo
from . import reparacion
from . import pieza


cliente.py

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class cliente(models.Model):
    _name = 'taller.cliente'
    _description = 'taller.cliente'
    _sql_constraints=[]

    name = fields.Char()
    telefono = fields.Integer()
    email = fields.Char()
    direccion = fields.Char()

    vehiculo_id = fields.One2many(comodel_name='taller.vehiculo', inverse_name='cliente_id')


pieza.py

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class pieza(models.Model):
    _name = 'taller.pieza'
    _description = 'taller.pieza'
    _sql_constraints=[]

    nombre = fields.Char()
    codigo = fields.Integer()
    precio_unitario = fields.Integer(string='Precio')

    reparacion_id = fields.Many2many('taller.reparacion')

    @api.constrains('precio_unitario')
    def _price(self):
        for record in self:
            if record.precio_unitario < 0:
                raise ValidationError('El precio debe ser > 0')


reparacion.py

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class reparacion(models.Model):
    _name = 'taller.reparacion'
    _description = 'taller.reparacion'
    _sql_constraints=[]

    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()
    descripcion = fields.Char()
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_curso', 'En curso'),
        ('finalizada', 'Finalizada')
    ])
    coste_total = fields.Integer()

    vehiculo_id = fields.Many2one(comodel_name='taller.vehiculo')
    pieza_id = fields.Many2many('taller.pieza')
    tecnico_id = fields.Many2one('res.users')

    def action_abrir(self):
        self.estado = 'en_curso'

    def action_cerrar(self):
        self.estado = 'finalizada'

    def action_reabrir(self):
        self.estado = 'borrador'


vehiculo.py

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'taller.vehiculo'
    _sql_constraints=[]

    matricula = fields.Char()
    marca = fields.Char()
    modelo = fields.Char()
    anio = fields.Integer()

    cliente_id = fields.Many2one(comodel_name='taller.cliente')
    reparacion_id = fields.One2many(comodel_name='taller.reparacion', inverse_name='vehiculo_id')


ir.model.access.csv

id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_taller_cliente,taller.cliente,model_taller_cliente,base.group_user,1,1,1,1
access_taller_vehiculo,taller.vehiculo,model_taller_vehiculo,base.group_user,1,1,1,1
access_taller_reparacion,taller.reparacion,model_taller_reparacion,base.group_user,1,1,1,1
access_taller_pieza,taller.pieza,model_taller_pieza,base.group_user,1,1,1,1


cliente.xml

<odoo>
  <data>
    <record id="view_cliente_tree" model="ir.ui.view">
      <field name="name">taller.cliente.tree</field>
      <field name="model">taller.cliente</field>
      <field name="arch" type="xml">
        <tree string="Clientes">
          <field name="name"/>
          <field name="telefono"/>
          <field name="email"/>
          <field name="direccion"/>
          <field name="vehiculo_id"/>
        </tree>
      </field>
    </record>

    <record id="action_cliente" model="ir.actions.act_window">
      <field name="name">Clientes</field>
      <field name="res_model">taller.cliente</field>
      <field name="view_mode">tree,form</field>
      <field name="view_id" ref="view_cliente_tree"/>
    </record>
  </data>
</odoo>


menu.xml

<odoo>
  <data>
    <menuitem id="menu_taller_root" name="Taller Mecánico"/>

    <menuitem id="menu_clientes" name="Clientes" parent="menu_taller_root" action="action_cliente"/>
    <menuitem id="menu_vehiculos" name="Vehículos" parent="menu_taller_root" action="action_vehiculo"/>
    <menuitem id="menu_reparaciones" name="Reparaciones" parent="menu_taller_root" action="action_reparacion"/>
    <menuitem id="menu_piezas" name="Piezas" parent="menu_taller_root" action="action_pieza"/>
  </data>
</odoo>


piezas.xml

<odoo>
  <data>
    <record id="view_pieza_tree" model="ir.ui.view">
      <field name="name">taller.pieza.tree</field>
      <field name="model">taller.pieza</field>
      <field name="arch" type="xml">
        <tree string="Piezas" decoration-success="precio_unitario&lt;10" decoration-danger="precio_unitario&gt;100">
          <field name="nombre"/>
          <field name="codigo"/>
          <field name="precio_unitario"/>
          <field name="reparacion_id"/>
        </tree>
      </field>
    </record>

    <record id="action_pieza" model="ir.actions.act_window">
      <field name="name">Piezas</field>
      <field name="res_model">taller.pieza</field>
      <field name="view_mode">tree,form</field>
      <field name="view_id" ref="view_pieza_tree"/>
    </record>
  </data>
</odoo>


reparacion.xml

<odoo>
  <data>
    <record id="view_reparacion_tree" model="ir.ui.view">
      <field name="name">taller.reparacion.tree</field>
      <field name="model">taller.reparacion</field>
      <field name="arch" type="xml">
        <tree string="Reparaciones"
              editable="bottom"
              decoration-muted="estado=='borrador'"
              decoration-info="estado=='en_curso'"
              decoration-success="estado=='finalizada'">

          <field name="fecha_inicio" attrs="{'readonly':[('estado','=','finalizada')]}"/>
          <field name="fecha_fin" attrs="{'readonly':[('estado','=','finalizada')]}"/>
          <field name="descripcion" attrs="{'readonly':[('estado','=','finalizada')]}"/>
          <field name="estado" attrs="{'readonly':[('estado','=','finalizada')]}"/>
          <field name="coste_total" attrs="{'readonly':[('estado','=','finalizada')]}"/>
          <field name="vehiculo_id" attrs="{'readonly':[('estado','=','finalizada')]}"/>
          <field name="pieza_id" attrs="{'readonly':[('estado','=','finalizada')]}"/>
          <field name="tecnico_id" attrs="{'readonly':[('estado','=','finalizada')]}"/>

          <button name="action_abrir" type="object" string="Abrir reparación" class="btn-primary"
                  attrs="{'invisible':[('estado','!=','borrador')]}"/>
          <button name="action_cerrar" type="object" string="Cerrar reparación" class="btn-success"
                  attrs="{'invisible':[('estado','!=','en_curso')]}"/>
          <button name="action_reabrir" type="object" string="Reabrir" class="btn-warning"
                  attrs="{'invisible':[('estado','!=','finalizada')]}"/>
        </tree>
      </field>
    </record>

    <record id="action_reparacion" model="ir.actions.act_window">
      <field name="name">Reparaciones</field>
      <field name="res_model">taller.reparacion</field>
      <field name="view_mode">tree</field>
      <field name="view_id" ref="view_reparacion_tree"/>
    </record>
  </data>
</odoo>


vehiculo.xml

<odoo>
  <data>
    <record id="view_vehiculo_tree" model="ir.ui.view">
      <field name="name">taller.vehiculo.tree</field>
      <field name="model">taller.vehiculo</field>
      <field name="arch" type="xml">
        <tree string="Vehículos">
          <field name="matricula"/>
          <field name="marca"/>
          <field name="modelo"/>
          <field name="anio"/>
          <field name="cliente_id"/>
          <field name="reparacion_id"/>
        </tree>
      </field>
    </record>

    <record id="action_vehiculo" model="ir.actions.act_window">
      <field name="name">Vehículos</field>
      <field name="res_model">taller.vehiculo</field>
      <field name="view_mode">tree,form</field>
      <field name="view_id" ref="view_vehiculo_tree"/>
    </record>
  </data>
</odoo>


__manifest__.py

# -*- coding: utf-8 -*-
{
    'name': "Taller Mecánico",
    'summary': "Gestión de clientes, vehículos, reparaciones y piezas",
    'description': """
        Módulo para gestionar clientes, vehículos, reparaciones y piezas en un taller mecánico.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Services',
    'version': '0.1',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'views/cliente.xml',
        'security/ir.model.access.csv',
        'views/vehiculo.xml',
        'views/reparacion.xml',
        'views/piezas.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

```