from odoo import models, fields, api

class Ingrediente(models.Model):
    _name = 'gtg.ingrediente'
    _description = 'Modelo de Ingrediente'

    name = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio", required=True)
    tipo = fields.Selection([("proteina", "Proteína"), ("carbohidratos", "Carbohidratos"), ("grasas", "Grasas"), ("complemento", "Complemento")], 
                            string="Tipo de Ingrediente", required=True)
    
    bowls_ids = fields.Many2many("gtg.bowl", string="Bowls")
    menus_ids = fields.Many2many("gtg.menu", string="Menús")

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

class Menu(models.Model):
    _name = 'gtg.menu'
    _description = 'Modelo de Menú'
    
    name = fields.Char(string="Nombre", required=True)
    entrante = fields.Char(string="Entrante", required=True)
    principal = fields.Char(string="Plato Principal", required=True)
    postre = fields.Char(string="Postre", required=True)
    
    ingredientes_ids = fields.Many2many("gtg.ingrediente", string="Ingredientes")
    precio_total = fields.Float(string="Precio Total", compute='_compute_precio_total', store=True)

    @api.depends('ingredientes_ids.precio')
    def _compute_precio_total(self):
        for menu in self:
            menu.precio_total = sum(menu.ingredientes_ids.mapped('precio'))

class Client(models.Model):
    _name = 'gtg.client'
    _description = 'Modelo de Cliente'

    dni = fields.Char(string="Número de identificación", required=True)
    name = fields.Char(string="Nombre", required=True)
    surnames = fields.Char(string="Apellidos")
    email = fields.Char(string="Correo eléctronico")
    address = fields.Char(string="Dirección del cliente", required=True)
    phone = fields.Char(string="Número de teléfono", required=True)
    city = fields.Char(string="Ciudad", required=True)
    country = fields.Char(string="País", required=True)
    information = fields.Text(string="Información extra acerca del usuario")