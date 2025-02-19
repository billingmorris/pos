# pos_cogs_calculation/__manifest__.py
{
    'name': 'POS Cost of Goods Sold Calculation',
    'version': '14.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Calculate and display the total cost of goods sold in POS orders.',
    'description': """
        This module adds a field to calculate and display the total cost of goods sold
        in POS orders, with restricted access to authorized users.
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['point_of_sale'],
    'data': [
        'security/pos_cogs_calculation_security.xml',
        'security/ir.model.access.csv',
        'views/pos_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
