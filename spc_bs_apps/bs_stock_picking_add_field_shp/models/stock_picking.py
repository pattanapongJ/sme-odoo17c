from odoo import fields, models

class stock_picking(models.Model):
    _inherit = 'stock.picking'

    tracking_number = fields.Char(
        string='Tracking Number',
        readonly=True,
        related='sale_id.tracking_number',
    )
    
    tracking_number_returns = fields.Char(
        string='Tracking Number Returns',
        readonly=True,
        related='sale_id.tracking_number_returns',
    )
