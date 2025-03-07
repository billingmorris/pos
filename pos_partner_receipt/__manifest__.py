{
    'name': 'POS Partner Receipt',
    'version': '1.0',
    'summary': 'Display partner name on POS receipt',
    'description': 'This module adds the partner name to the POS receipt.',
    'author': 'BillMorris',
    'website': 'https://billingmorris.com',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'data': [],
    'qweb': ['static/src/xml/pos_receipt_view.xml'],  # Updated file name
    'installable': True,
    'application': False,
}
