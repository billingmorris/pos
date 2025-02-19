# pos_cogs_calculation/__manifest__.py
{
    'name': 'POS Cost of Goods Sold Calculation',
    'version': '14.0.1.0.0',
    'summary': 'Calculate the cost of goods sold in POS orders based on standard price.',
    'description': 'This module calculates the cost of goods sold for POS orders using the product standard price.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'data': [
#        'security/pos_cogs_security.xml',  # Add security rules
        'views/pos_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
