from odoo import models, fields

class CourseList(models.Model):
    _name = 'course.list'

    kode = fields.Char(string='Kode Course')
    name = fields.Char(string='Nama Course')
    price = fields.Float(string='Harga')
    bidang = fields.Selection([
        ('halal', 'Halal'),
        ('pangan', 'Pangan'),
    ], string='Tipe')
    is_aktif = fields.Boolean(string='Aktif')

    _sql_constraints = [
        ('kode_uniq', 'unique(kode)', 'kode harus unik!')
    ]

