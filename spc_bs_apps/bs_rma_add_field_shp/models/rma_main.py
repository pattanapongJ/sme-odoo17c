from odoo import fields, models

class RmaMain(models.Model):
    _inherit = 'rma.main'

    tracking_number = fields.Char(
        string='Tracking Number',
        readonly=True,
        related='sale_order.tracking_number',
    )
    
    tracking_number_returns = fields.Char(
        string='Tracking Number Returns',
        readonly=True,
        related='sale_order.tracking_number_returns',
    )
