# -*- encoding: utf-8 -*-

#
# Este modulo tiene reportes personalizados para Guatemala.
    
#
# Status 1.0 - tested on Open ERP 5.0.6
#

{
    'name' : 'Sociedad Biblica de Guatemala',
    'version' : '1.0',
    'category': 'Custom',
    'description': """Este modulo tiene Perzonalizaciones para el Proyecto Crece y Aprende""",
    'author': 'Miguel Chuga',
    'website': 'http://openerpgt.wordpress.com',
    'depends' : ['base','sale'],
    'init_xml' : [ ],
    'demo_xml' : [ ],
    'update_xml' : ['catalogos_view.xml','partner_view.xml'],
    'installable': True,
    'certificate': '',
}
#,'catalogos_view.xml'
