# pos_cogs_calculation/models/pos_order.py
from odoo import models, fields, api

class PosOrder(models.Model):
    _inherit = 'pos.order'
    total_cost_of_goods_sold = fields.Float(
        string='Total Cost of Goods Sold',
        groups='pos_cogs_calculation.group_view_total_cost_of_goods_sold',  # Restrict access
    )
    #total_cost_of_goods_sold = fields.Float(string='Total Cost of Goods Sold', readonly=True)

    def _calculate_cost_of_goods_sold(self):
        total_cost = 0
        for line in self.lines:
            product = line.product_id
            standard_price = product.standard_price
            line_cost = standard_price * line.qty
            total_cost += line_cost
        return total_cost

    def action_pos_order_paid(self):
        res = super(PosOrder, self).action_pos_order_paid()
        total_cost = self._calculate_cost_of_goods_sold()
        self.write({'total_cost_of_goods_sold': total_cost})
        return res

