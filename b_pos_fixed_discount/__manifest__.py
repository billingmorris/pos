# -*- coding: utf-8 -*-
{
    'name': "POS Global Fixed Discount",
    'summary': """
        POS fixed discount""",
    'description': """
        Changes the percent discount to fixed discount in the POS module.
    """,
    'author': "Baramej® Business and Digital Technology Center LLC",
    'website': "https://baramej.io",
    'support': "info@baramej.io",
    'category': 'Customizations',
    'version': '1.0',
    'license': 'LGPL-3',
    'application': True,
    'price': 10,
    'currency': "USD",
    'depends': ['pos_discount'],
    'assets': {
        'point_of_sale.assets': [
            'b_pos_fixed_discount/static/src/js/**/*',
            'b_pos_fixed_discount/static/src/xml/**/*',
        ],
    },
    'images': ["static/description/banner.png"],
}
