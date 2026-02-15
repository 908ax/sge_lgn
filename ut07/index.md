# [UT07](./index.md)

## PR0701: Página estática y dinámica básica
```
PR0701: Página estática y dinámica básica

1.- En nuestro proyecto taller mecanico creamos dos xml en views/ web_bienvenida y web_vehiculos, con su codigo, en controllers/ creamos main con el codigo de las dos web.

2.- En controllers/__init__.py importamos main y en el __manifest__.py importamos los dos xml de views/.
```
![Imagen](<Captura de pantalla (359).png>)

![Imagen](<Captura de pantalla (360).png>)

## Codigo 701
```
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
        'views/web_bienvenida.xml',
        'views/web_vehiculos.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}


web_bienvenida.xml

<odoo>
    <data>

        <template id="taller_web_bienvenida" name="Web Bienvenida Taller">
            <t t-call="web.layout">
                <div class="container mt-5">
                    <h1>Bienvenido al módulo Taller</h1>
                    <p>Aplicación desarrollada para la práctica PR0606.</p>
                </div>
            </t>
        </template>

    </data>
</odoo>


web_vehiculos.xml

<odoo>
    <data>

        <template id="taller_web_vehiculos" name="Web Listado Vehículos">
            <t t-call="web.layout">
                <div class="container mt-5">

                    <h1>Listado de vehículos</h1>

                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th>Matrícula</th>
                                <th>Marca</th>
                                <th>Modelo</th>
                                <th>Año</th>
                            </tr>
                        </thead>
                        <tbody>
                            <t t-foreach="vehiculos" t-as="v">
                                <tr>
                                    <td><t t-esc="v.matricula"/></td>
                                    <td><t t-esc="v.marca"/></td>
                                    <td><t t-esc="v.modelo"/></td>
                                    <td><t t-esc="v.anio"/></td>
                                </tr>
                            </t>
                        </tbody>
                    </table>

                </div>
            </t>
        </template>

    </data>
</odoo>


main.py

from odoo import http
from odoo.http import request

class TallerController(http.Controller):

    @http.route('/taller/bienvenida', auth='public', website=True)
    def web_bienvenida(self, **kw):
        return request.render('taller_mecanico.taller_web_bienvenida')
    @http.route('/taller/vehiculos', auth='public', website=True)
    def web_listado_vehiculos(self, **kw):
        vehiculos = request.env['taller.vehiculo'].sudo().search([])
        return request.render('taller_mecanico.taller_web_vehiculos', {
            'vehiculos': vehiculos
        })


__init__.py

# -*- coding: utf-8 -*-

from . import controllers
from . import main



```

## PR0702: API REST
```
PR0702: API REST

1.- En subscriptions en controllers/ creamos api.py junto con su codigo y en __init__.py de controllers/ le importamos api.


```

![Imagen](<Captura de pantalla (361).png>)

## Codigo 702
```
api.py

from odoo import http
from odoo.http import request

class SubscriptionAPI(http.Controller):

    @http.route('/api/suscription', auth='public', type='http', methods=['GET'], website=False)
    def list_subscriptions(self, **kwargs):
        status = kwargs.get('status')
        page = int(kwargs.get('page', 1))
        per_page = 10
        allowed_status = ['active', 'expired', 'pending', 'cancelled']

        if status and status not in allowed_status:
            response = {'error': "Estado inválido, debe ser uno de: active, expired, pending, cancelled"}
            return request.make_response(
                str(response),
                headers=[('Content-Type', 'application/json')],
                status=400
            )

        domain = []
        if status:
            domain.append(('status', '=', status))

        all_subs = request.env['subscription.subscription'].sudo().search(domain, order='id asc')

        start = (page - 1) * per_page
        end = start + per_page
        paginated = all_subs[start:end]

        result = []
        for s in paginated:
            result.append({
                'name': s.name,
                'customer_id': s.customer_id.id if s.customer_id else None,
                'customer_name': s.customer_id.name if s.customer_id else None,
                'subscription_code': s.subscription_code,
                'start_date': str(s.start_date) if s.start_date else None,
                'end_date': str(s.end_date) if s.end_date else None,
                'duration_months': s.duration_months,
                'renewal_date': str(s.renewal_date) if s.renewal_date else None,
                'status': s.status,
                'is_renewable': s.is_renewable,
                'auto_renewal': s.auto_renewal,
                'price': s.price,
                'usage_limit': s.usage_limit,
                'current_usage': s.current_usage,
                'use_percent': s.use_percent
            })

        response = {
            'page': page,
            'per_page': per_page,
            'total': len(all_subs),
            'subscriptions': result
        }

        return request.make_response(
            str(response),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/api/suscription/<string:name>', auth='public', type='http', methods=['GET'], website=False)
    def get_subscription_by_name(self, name):
        subscription = request.env['subscription.subscription'].sudo().search([('name', '=', name)], limit=1)

        if not subscription:
            response = {'error': f"No se encontró suscripción con nombre '{name}'"}
            return request.make_response(
                str(response),
                headers=[('Content-Type', 'application/json')],
                status=400
            )

        result = {
            'name': subscription.name,
            'customer_id': subscription.customer_id.id if subscription.customer_id else None,
            'customer_name': subscription.customer_id.name if subscription.customer_id else None,
            'subscription_code': subscription.subscription_code,
            'start_date': str(subscription.start_date) if subscription.start_date else None,
            'end_date': str(subscription.end_date) if subscription.end_date else None,
            'duration_months': subscription.duration_months,
            'renewal_date': str(subscription.renewal_date) if subscription.renewal_date else None,
            'status': subscription.status,
            'is_renewable': subscription.is_renewable,
            'auto_renewal': subscription.auto_renewal,
            'price': subscription.price,
            'usage_limit': subscription.usage_limit,
            'current_usage': subscription.current_usage,
            'use_percent': subscription.use_percent
        }

        return request.make_response(
            str(result),
            headers=[('Content-Type', 'application/json')]
        )



__init__.py

# -*- coding: utf-8 -*-

from . import controllers
from . import api


```

