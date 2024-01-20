from odoo import models, fields, api

class Ingrediente(models.Model):
    _name = 'gtg.ingrediente'
    _description = 'Modelo de Ingrediente'

    name = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio", required=True)
    tipo = fields.Selection([("proteina", "Proteína"), ("carbohidratos", "Carbohidratos"), ("grasas", "Grasas"), ("complemento", "Complemento")], 
                            string="Tipo de Ingrediente", required=True)
    
    bowls_ids = fields.Many2many("gtg.bowl", string="Bowls")

class Bowl(models.Model):
    _name = 'gtg.bowl'
    _description = 'Modelo de Bowl'
    
    name = fields.Char(string="Nombre", required=True)
    
    ingredientes_ids = fields.Many2many("gtg.ingrediente", string="Ingredientes")
    precio_total = fields.Float(string="Precio Total", compute='_compute_precio_total', store=True)

    @api.depends('ingredientes_ids.precio')
    def _compute_precio_total(self):
        for bowl in self:
            bowl.precio_total = sum(bowl.ingredientes_ids.mapped('precio'))
