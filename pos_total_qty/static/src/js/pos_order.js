odoo.define('pos_total_qty.pos_order', function(require) {
    "use strict";

    const models = require('point_of_sale.models');
    const OrderSuper = models.Order.prototype;

    models.Order = models.Order.extend({

        export_for_printing: function() {
            let json = OrderSuper.export_for_printing.apply(this, arguments);

            let total_qty = this.get_orderlines().reduce(
                (sum, line) => sum + line.get_quantity(), 0
            );

            json.total_qty = total_qty;
            return json;
        },

    });

});
