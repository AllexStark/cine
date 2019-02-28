# -*- coding: utf-8 -*-
{
    'name': "Cine",

    'summary': """
        Gestión de datos para un cine""",

    'description': """
        Con este módulo resultará más fácil gestionar los datos de nuestro cine, permitiéndonos añadir empleados, fidelizar clientes, añadir distribuidoras, registrar películas y sesiones, crear tarifas para los distintos días de la semana y aplicarlas en la venta de entradas.
    """,

    'author': "Lorena",
    'website': "http://www.iescomercio.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestion',
    'version': '0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],

    'application': True
}
