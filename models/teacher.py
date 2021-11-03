from odoo import models, fields, api, _


class UniversityTeacher(models.Model):
    _name = 'university.teacher'
    _description = 'Teacher management'
    _rec_name = 'f_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    date_start = fields.Datetime('Date of start', tracking=True)
    f_name = fields.Char('First Name', tracking=True)
    l_name = fields.Char('Last Name', tracking=True)
    identity_card = fields.Char('Identity card', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    date_of_birth = fields.Date('Date of birth', tracking=True)
    date_start = fields.Datetime('Date of start', tracking=True)
    e_mail = fields.Char('E-mail', tracking=True)
    phone = fields.Char('Phone number', tracking=True)
    rue = fields.Char('Rue')
    ville = fields.Char('Ville')
    code_postale = fields.Char('Code postale')
    suggestions = fields.Text('Suggestions')
    student_ids = fields.One2many('university.student', 'student_id', string="Students")
    departments_ids = fields.One2many('university.department', 'department_id', string='Departments')
    reference = fields.Char(string='teacher reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))


@api.model
def create(self, vals):
    if vals.get('reference', _('New')) == _('New'):
        vals['reference'] = self.env['ir.sequence'].next_by_code('university.teacher.seq') or _('New')
    result = super(UniversityTeacher, self).create(vals)
    return result
