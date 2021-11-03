from odoo import models, fields, api, _


class UniversityAziz(models.Model):
    _name = 'university.aziz'
    _description = 'callse of university management'

    name = fields.Char('Name', tracking=True)
    code = fields.Char('Code', tracking=True)
    director = fields.Char('Director', tracking=True)
    discipline = fields.Char('Discipline', tracking=True)
    date = fields.Date('Date of creation')
