#-*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_compare, float_is_zero


class HDTickets(models.Model):
    _inherit = 'helpdesk.ticket'
    
    x_causa_incidencia = fields.Selection(string='Causa de Incidencia', [('1','Error de usuario'),('2','Error de configuración'),('3','Bug Standard'),('4','Bug Custom'),('5','Funcionalidad no contemplada'),('0','Desconocida')])
    x_frente = fields.Selection(string='Frente', [('SCM.INV','SCM Inventarios'),('SCM.ICX','SCM Solicitudes'),('SCM.PO','SCM Compras'),('FIN.EXP','FIN Reportes de Gastos'),('FIN.AP','FIN Cuentas por Pagar'),('FIN.AR','FIN Cuentas por Cobrar'),('FIN.FA','FIN Activos Fijos'),('FIN.GL','FIN Contabilidad'),('FIN.CE','FIN Conciliación Bancaria'),('EAM.EAM','EAM Mantenimiento'),('PPM.PJC','PPM Project Costing'),('GEN.ACCESS','GEN Accesos'),('GEN.EMAIL','GEN Correos'),('GEN.AUD','GEN Auditoría'),('DBA.DBA','DBA')])
    x_resumen_solucion = fields.Char(string='Resumen Solución')
    x_resumen_tarea = fields.Char(string='Resumen Tarea')
    #x_sla = fields.Char(string='SLA', readonly = True)
    x_state = fields.Selection(string='Estado', [('En GSG','En GSG'),('En Cliente','En Cliente'),('Stand By','Stand By')])
    x_tipo = fields.Selection(string='Tipo', [('consulta','Consulta'),('incidencia','Incidencia'),('requerimiento','Requerimiento'),('proyecto','Proyecto'),('monitoreo','Monitoreo'),('otro','Otro')])
    x_tipo_monitoreo = fields.Selection(string='Monitoreo', [('Oracle Support','Oracle Support'),('Sistema Cliente','KACE'),('Funcional','Funcional')])
    x_tipo_requerimiento = fields.Selection(string='Tipo Requerimiento', [('variable', 'Variable'), ('fijo', 'Fijo'), ('proyecto', 'Proyecto')])