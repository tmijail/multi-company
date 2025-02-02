##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Account Multicompany Usability',
    'version': '13.0.1.1.0',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'views/res_company_property_views.xml',
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
        'views/product_category_views.xml',
        'views/product_template_views.xml',
        'views/product_product_views.xml',
        'views/account_journal_dashboard_views.xml',
        'security/account_multicompany_ux_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': False,
    'auto_install': False,
}
