{
    "name": "POS Total Quantity",
    "summary": "Imprime el total de productos en cada ticket del POS",
    "version": "14.0.1.0.0",
    "author": "elmonitor.net",
    "license": "LGPL-3",
    "depends": ["point_of_sale"],
    "data": [
        "static/src/xml/pos_receipt_template.xml",
    ],
    "qweb": [
        "static/src/xml/pos_receipt_template.xml",
    ],
    "installable": True,
}