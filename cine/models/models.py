# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import *
from openerp.exceptions import ValidationError

class empleado(models.Model):
        _name = 'cine.empleado'
        name = fields.Char(string  = "DNI", required = True)
        nombre = fields.Char(string = "Nombre", required = True)
        apellidos = fields.Char(string="Apellidos", required = True)
        telefono = fields.Integer(string = "Número de teléfono")
        puesto = fields.Char(string = "Puesto de trabajo")
        horas = fields.Integer(string = "Horas de trabajo semanales")
        sueldo = fields.Float(string = "Sueldo base")
        _sql_constraints = [('PK_NM', 'unique (name)','Ese empleado ya existe.')]

        @api.depends('value')
        def _value_pc(self):
            self.value2 = float(self.value) / 100

class cliente(models.Model):
        _name = 'cine.cliente'
        name = fields.Integer(string  = "Número del cliente", required = True)
        nombre = fields.Char(string = "Nombre", required = True)
        apellidos = fields.Char(string="Apellidos", required = True)
        telefono = fields.Integer(string = "Número de teléfono")
        cod_postal = fields.Integer(string = "Código postal")
        _sql_constraints = [('PK_NM', 'unique (name)','Ese cliente ya existe.')]

        @api.constrains('name')
        def _check_name(self):
            for record in self:
                if record.name < 1:
                    raise ValidationError("El ID debe ser mayor que 0")

class pelicula(models.Model):
        _name = 'cine.pelicula'
        name = fields.Char(string  = "ID", required = True)
        imagen = fields.Binary()
        nombre = fields.Char(string = "Nombre", required = True)
        sinopsis = fields.Text(string = "Sinopsis")
        duracion = fields.Integer(string = "Duración en minutos")
        fecha_estreno = fields.Date(string = "Fecha de estreno")
        distribuidora = fields.Many2one("cine.distribuidora", string ="Distribuidora")
        _sql_constraints = [('PK_NM', 'unique (name)','Esa película ya existe.')]

class distribuidora(models.Model):
        _name = 'cine.distribuidora'
        name = fields.Char(string  = "Identificador", required = True)
        nombre = fields.Char(string = "Nombre", required = True)
        pelicula = fields.One2many("cine.pelicula", "distribuidora", string = "Películas")
        _sql_constraints = [('PK_NM', 'unique (name)','Esa distribuidora ya existe.')]

class sesion(models.Model):
        _name = 'cine.sesion'
        name = fields.Integer(string  = "Número de sesión", required = True)
        peli = fields.Many2one('cine.pelicula', string='Película')
        sala = fields.Integer(string = "Sala de proyección")
        fecha = fields.Datetime(string = "Fecha y hora de la sesión")
        _sql_constraints = [('PK_NM', 'unique (name)','Esa sesión ya existe.')]

class tarifa(models.Model):
        _name = 'cine.tarifa'
        name = fields.Char(string  = "Tipo de tarifa", required = True)
        importe = fields.Float(string = "Importe")

class venta(models.Model):
        _name = 'cine.venta'
        name = fields.Integer(string  = "Número de venta", required = True)
        ses = fields.Many2one('cine.sesion', string='Sesión', required = True)
        entrada = fields.Many2one('cine.tarifa', string='Tarifa aplicada', required = True)
        cantidad = fields.Integer(string = "Cantidad de entradas", required = True)
        emp = fields.Many2one('cine.empleado', string='Empleado que realiza la venta')
        cli = fields.Many2one('cine.cliente', string='Cliente')
        importe = fields.Float(compute = "_value_importe", store = True)
        _sql_constraints = [('PK_NM', 'unique (name)','Esa venta ya existe.')]

        @api.depends('importe', 'cantidad')
        def _value_importe(self):
            self.importe = self.entrada.importe * self.cantidad

        @api.constrains('name')
        def _check_name(self):
            for record in self:
                if record.name < 1:
                    raise ValidationError("El numero de venta debe ser mayor que 0")

        @api.constrains('cantidad')
        def _check_cantidad(self):
            for record in self:
                if record.cantidad < 1:
                    raise ValidationError("La cantidad debe ser mayor que 0")
