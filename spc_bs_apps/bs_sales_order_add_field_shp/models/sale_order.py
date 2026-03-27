from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    tracking_number = fields.Char(
        string='Tracking Number',
        readonly=True,
    )
    
    tracking_number_returns = fields.Char(
        string='Tracking Number Returns',
        readonly=True,
    )
    
