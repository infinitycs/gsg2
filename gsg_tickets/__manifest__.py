# -*- coding: utf-8 -*-
{
    'name': "GSG Gestion de Tickets",

    'summary': """
        Gestión de Tickets de soporte para control de incidencias y requerimientos""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Infinity Solutions",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','helpdesk.ticket',
                ],

    # always loaded
    'data': [
        'views/tickets_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}