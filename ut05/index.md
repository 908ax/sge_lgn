# [UT05](./index.md)

## Ejercicio paso a paso
```
PR0501: Creación de un módulo básico 

1.- En Docker Desktop en la terminal vamos a la carpeta volumesOdoo y ejecutamos docker exec -ti odoo_prod bash y luego odoo scaffold reservas_salas mnt/extra-addons para crear reservas_salas.

2.- En reservas_salas vamos a __manifest__.py y modificamos su código. En models -> models.py
modificamos su código y en views -> views.py modificamos su código.
```

## Codigo 501
```
__manifest__.py

# -*- coding: utf-8 -*-
{
    'name': "Gestión de reservas de salas",

    'summary': """
        Modulo para la gestión de reserva de salas""",

    'description': """
        Modulo que permite reservar salas con una prioridad asociada. Permite marcar tareas
        como realizadas o no realizadas y tiene un campo calculado llamado 'Urgente' que se 
        marca si la propiedad es superior a 10
    """,

    'author': "Leonb",
    'website': "https://www.yourcompany.com",

    'application': True,
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
}


models.py

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class reservas_salas(models.Model):
    _name = 'reservas_salas.reservas_salas'
    _description = 'reservas_salas.reservas_salas'

    nombre = fields.Char()
    capacidad = fields.Integer()
    fecha_reserva = fields.Date()
    reservada = fields.Boolean()
    comentarios = fields.Char()


views.py

<odoo>
  <data>
    <!-- explicit list view definition -->

    <record model="ir.ui.view" id="reservas_salas.list">
      <field name="name">reservas_salas list</field>
      <field name="model">reservas_salas.reservas_salas</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="capacidad"/>
          <field name="fecha_reserva"/>
          <field name="reservada"/>
          <field name="comentarios"/>
        </tree>
      </field>
    </record>


    <!-- actions opening views on models -->
    
    <record id="reservas_salas.action_window" model="ir.actions.act_window">
      <field name="name">Salas</field>
      <field name="res_model">reservas_salas.reservas_salas</field>
      <field name="view_mode">tree,form</field>
    </record>


    <!-- server action to the one above -->
<!--
    <record model="ir.actions.server" id="reservas_salas.action_server">
      <field name="name">reservas_salas server</field>
      <field name="model_id" ref="model_reservas_salas_reservas_salas"/>
      <field name="state">code</field>
      <field name="code">
        action = {
          "type": "ir.actions.act_window",
          "view_mode": "tree,form",
          "res_model": model._name,
        }
      </field>
    </record>
-->

    <!-- Top menu item -->

    <menuitem name="Gestión de salas" id="reservas_salas.menu_root"/>

    <!-- menu categories -->

    <menuitem name="Salas" id="reservas_salas.menu_1" parent="reservas_salas.menu_root"/>
    <menuitem name="Reservas" id="reservas_salas.menu_2" parent="reservas_salas.menu_root"/>

    <!-- actions -->

    <menuitem name="Salas Disponibles" id="reservas_salas.menu_1_list" parent="reservas_salas.menu_1"
              action="reservas_salas.action_window"/>
    <menuitem name="Reservas realizadas" 
          id="reservas_salas.menu_reservas_realizadas" 
          parent="reservas_salas.menu_2" action="reservas_salas.action_window"/>



  </data>
</odoo>
```
