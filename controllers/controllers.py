# -*- coding: utf-8 -*-
from odoo import http

# class MethodBalanceAperturaPos(http.Controller):
#     @http.route('/method_balance_apertura_pos/method_balance_apertura_pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_balance_apertura_pos/method_balance_apertura_pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_balance_apertura_pos.listing', {
#             'root': '/method_balance_apertura_pos/method_balance_apertura_pos',
#             'objects': http.request.env['method_balance_apertura_pos.method_balance_apertura_pos'].search([]),
#         })

#     @http.route('/method_balance_apertura_pos/method_balance_apertura_pos/objects/<model("method_balance_apertura_pos.method_balance_apertura_pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_balance_apertura_pos.object', {
#             'object': obj
#         })