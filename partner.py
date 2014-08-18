# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields

class Partner(osv.Model):
    """Inherited res.partner"""
    # The line above is the Pythons way to document
    # your objects (like classes)
    _inherit = 'res.partner'
    
    _columns = {
    # We just add a new column in res.partner model
    'dias_horas': fields.char('Dias y horarios de servicios', size=200),    
    'horarios': fields.char('Horarios', size=200),
    'denominaciones_id': fields.many2one('sbg.denominaciones', 'Denominaciones'),
    'maestros': fields.integer('Cantidad de maestros'),
    'ninos': fields.integer('Cantidad de ninios en la Iglesia'),
    'edades': fields.char('Division de edades', size=200),
    'especificos': fields.char('Atienden a ninios y ninias de que lugares aledanios especificos', size=200),

    'departamento': fields.char('Departamento', size=200),
    'ninos_ma': fields.integer('Cantidad de ninios del maestro'),
    'edad_ma': fields.integer('Edad del maestro'),
    'tiempo_ma': fields.integer('Tiempo de ser miembro en la Iglesia'),
    'funcion_ma': fields.integer('Funcion del maestro de la Escuela Domincal'),
    
    'departamento_ni': fields.char('Departamento o clase niño', size=200),
    'fecha_nacimiento': fields.date('Fecha de Nacimiento', size=10),
    'edad_ni': fields.integer('Edad del Niño'),
    'padre_ni': fields.char('Padre del niño', size=200),
    'madre_ni': fields.char('Madre del niño', size=200),
    'hermanos_ni': fields.integer('Cantidad de hermanos del Niño'),
    'grado_ni': fields.integer('Grado del Niño'),
    'estudia_ni': fields.selection([('SI','SI'),('NO','NO')], 'Estudia ?'),
                   
    }
