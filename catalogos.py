# -*- encoding: utf-8 -*-

from osv import osv, fields
from tools import config
import datetime
import time
import sys
import netsvc


class sbg_denominaciones(osv.osv):
    _name = 'sbg.denominaciones'
    _description = 'Denominaciones'
    _rec_name = 'nombre'
    _columns = {
        'nombre': fields.char('Denominacion', size=40, required=True),
    }
    _order = 'nombre'
sbg_denominaciones()

 
