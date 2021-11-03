from odoo import models, fields,api,_

class UniversityStudent(models.Model):
    _name = 'university.student'
    _inherit = ['mail.thread','mail.activity.mixin',]
    _description = 'student inscription'
    _rec_name = 'f_name'
    reference = fields.Char(string='student reference', required=True, copy=False, readonly=True,
                        default=lambda self: _('New'))
    f_name = fields.Char(string='First Name', tracking = True)
    l_name = fields.Char(string='Last Name',tracking = True)
    identity_card = fields.Char(string='Identity card',required = True,tracking = True)
    gender = fields.Selection([('male','Male'),('female','Female')])
    date_of_birth = fields.Date(string='Date of birth')
    date_inscription = fields.Datetime(string='Date of inscription')
    e_mail = fields.Text(string='E-mail')
    phone = fields.Char(string='Phone number')
    teacher_id = fields.Many2one(comodel_name='university.teacher', string='teachers')
    teacher_ids = fields.Many2many(comodel_name='university.teacher', string='teachers')
    student_id = fields.Many2one('university.teacher',string="student")

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('university.student.seq') or _('New')
        result = super(UniversityStudent, self).create(vals)
        return result

    @api.depends('f_name','gender')
    def whoIs(self):
        if self.gender=='male':
            print('he is a man')
        else:
            print('she is a woman')