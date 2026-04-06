from odoo import models, fields, api

class PosOrder(models.Model):
    _inherit = "pos.order"

    total_qty = fields.Float(
        string="Total Qty",
        compute="_compute_total_qty",
        store=True
    )

    @api.depends('lines.qty')
    def _compute_total_qty(self):
        for order in self:
            order.total_qty = sum(order.lines.mapped('qty'))