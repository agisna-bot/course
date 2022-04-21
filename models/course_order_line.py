from odoo import models, fields, api

class CourseOrderLine(models.Model):
    _name = 'course.order.line'
    
    course_id = fields.Many2one('course.list', string='Course')
    quantity = fields.Integer(string='Quantity', default=1)
    price = fields.Float(string='Price')
    price_total = fields.Float(string='Price Total', compute='get_price_total', store=True,)

    order_id = fields.Many2one('course.order', string='Order')

    @api.onchange('course_id')
    def get_price(self):
        self.price = self.course_id.price
    
    @api.onchange('quantity')
    def validate_qty(self):
        if self.quantity <= 0:
            return {
                'warning': {
                    'title': 'Cek Kembali Kolom Quantity',
                    'message': 'Jumlah pembelian harus lebih besar daripada 0',
                }
            }
    
    @api.depends('quantity', 'price')
    def get_price_total(self):
        for doc in self:
            doc.price_total = doc.quantity * doc.price