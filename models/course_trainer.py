from odoo import models, fields

class CourseTrainer(models.Model):
    _name = 'course.trainer'

    name = fields.Char(string='Nama Trainer', required=True)
    rating = fields.Float(string='Rating')

    bidang = fields.Selection([
        ('halal', 'Halal'),
        ('pangan', 'Pangan'),
    ], string='Bidang')

    is_part_time = fields.Boolean(string='Part Time')

    image = fields.Binary('Image')
