# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ProductPackLine(models.Model):
    _inherit = 'product.pack.line'
    
    
    def get_sale_order_line_vals(self, line, order):
        vals = super().get_sale_order_line_vals(line, order)
        if 'name' in vals and vals['name'].startswith('> '):
            vals['name'] = vals['name'][2:]
        return vals



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'



    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for line in records:
            if line.multi_discount and line.gross_unit_price == line.price_unit:
                line._compute_multi_discount()
        return records

