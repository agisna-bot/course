from odoo import models, fields

class CourseCustomer(models.Model):
    _name = 'course.customer'

    name = fields.Char(string='Nama')
    address_ids = fields.One2many(
        comodel_name='course.customer.address',
        inverse_name='customer_id',
        string='Address',
    )

    category = fields.Char(string='Category')
    phone = fields.Char(string='Phone')

class CourseCustomerAddress(models.Model):
    _name = 'course.customer.address'

    name = fields.Char(string='Short Name')
    address = fields.Text(string='Alamat')
    is_main = fields.Boolean(string='Main')
    customer_id = fields.Many2one(
        comodel_name='course.customer',
        string='Customer'
    )

    _sql_constraints = [
        ('only_one_main', 'unique(is_main, customer_id)', 'Alamat Main harus satu')
    ]