from odoo import models, fields, api

class CourseOrder(models.Model):
    _name = 'course.order'

    name = fields.Char(string='Nomor Struk', required="True", index="True", default="New", readonly="1")

    customer = fields.Char(string='Customer')

    customer_id = fields.Many2one(
        comodel_name='course.customer',
        string='Customer'
        )
    address_id = fields.Many2one(
        comodel_name='course.customer.address',
        string='Address'
        )

    category = fields.Char(related='customer_id.category', string='Kategori')
    phone = fields.Char(related='customer_id.phone', string='Phone')

    trainer_id = fields.Many2one('course.trainer', string='Trainer')

    date_order = fields.Date(string='Date Order', default=fields.Date.today())

    state = fields.Selection([
            ('draft', 'Draft'),
            ('open', 'Open'),
        ], string='Status', default='draft')


    line_ids = fields.One2many(
        comodel_name='course.order.line',
        inverse_name='order_id',
        string='Line',
        )

    amount_total = fields.Float(compute='_compute_total', string='Total', store=True)

    @api.depends('line_ids')
    def _compute_total(self):
        for order_doc in self:
            amount_total = sum(order_doc.line_ids.mapped('price_total'))
            order_doc.amount_total = amount_total

    @api.onchange('customer_id')
    def get_address(self):
        if self.customer_id:
            if self.customer_id.address_ids:
                self.address_id = self.customer_id.address_ids[0].id
        else:
            self.address_id = False
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('course.order')
        return super(CourseOrder, self).create(vals)