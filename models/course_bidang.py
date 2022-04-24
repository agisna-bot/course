from . import fields, models, api

class Coursebidang(models.Model):
    _name = 'course.bidang'

    bidang = fields.One2many('course.list', 'nama', 'Bidang')
