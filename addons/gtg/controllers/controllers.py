# -*- coding: utf-8 -*-
# from odoo import http


# class Gtg(http.Controller):
#     @http.route('/gtg/gtg', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gtg/gtg/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gtg.listing', {
#             'root': '/gtg/gtg',
#             'objects': http.request.env['gtg.gtg'].search([]),
#         })

#     @http.route('/gtg/gtg/objects/<model("gtg.gtg"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gtg.object', {
#             'object': obj
#         })
