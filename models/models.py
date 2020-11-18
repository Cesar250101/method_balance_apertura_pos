# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, AccessError, ValidationError

class Session(models.Model):
    _inherit = 'pos.session'

    @api.one
    def action_pos_session_open(self):
        if self.control_register_balance_start==0:
            raise UserError(u'Debe establecer un saldo de apartura de la caja!')
        else:
            return super(Session, self).action_pos_session_open()