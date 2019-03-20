
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/MUL NUMBER VARstart : EXPRESSIONEXPRESSION : NUMBEREXPRESSION : VAREXPRESSION : EXPRESSION '+' EXPRESSION\n                  | EXPRESSION '-' EXPRESSIONEXPRESSION : EXPRESSION '*' EXPRESSION\n                  | EXPRESSION '/' EXPRESSION\n                  | EXPRESSION MUL EXPRESSIONEXPRESSION : '(' EXPRESSION ')'"
    
_lr_action_items = {'NUMBER':([0,5,6,7,8,9,10,],[3,3,3,3,3,3,3,]),'VAR':([0,5,6,7,8,9,10,],[4,4,4,4,4,4,4,]),'(':([0,5,6,7,8,9,10,],[5,5,5,5,5,5,5,]),'$end':([1,2,3,4,12,13,14,15,16,17,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,]),'+':([2,3,4,11,12,13,14,15,16,17,],[6,-2,-3,6,-4,-5,-6,-7,6,-9,]),'-':([2,3,4,11,12,13,14,15,16,17,],[7,-2,-3,7,-4,-5,-6,-7,7,-9,]),'*':([2,3,4,11,12,13,14,15,16,17,],[8,-2,-3,8,8,8,-6,-7,8,-9,]),'/':([2,3,4,11,12,13,14,15,16,17,],[9,-2,-3,9,9,9,-6,-7,9,-9,]),'MUL':([2,3,4,11,12,13,14,15,16,17,],[10,-2,-3,10,-4,-5,-6,-7,10,-9,]),')':([3,4,11,12,13,14,15,16,17,],[-2,-3,17,-4,-5,-6,-7,-8,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'EXPRESSION':([0,5,6,7,8,9,10,],[2,11,12,13,14,15,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> EXPRESSION','start',1,'p_start','test.py',41),
  ('EXPRESSION -> NUMBER','EXPRESSION',1,'p_expression_number','test.py',45),
  ('EXPRESSION -> VAR','EXPRESSION',1,'p_expression_var','test.py',49),
  ('EXPRESSION -> EXPRESSION + EXPRESSION','EXPRESSION',3,'p_expression_sum','test.py',54),
  ('EXPRESSION -> EXPRESSION - EXPRESSION','EXPRESSION',3,'p_expression_sum','test.py',55),
  ('EXPRESSION -> EXPRESSION * EXPRESSION','EXPRESSION',3,'p_expression_mul','test.py',62),
  ('EXPRESSION -> EXPRESSION / EXPRESSION','EXPRESSION',3,'p_expression_mul','test.py',63),
  ('EXPRESSION -> EXPRESSION MUL EXPRESSION','EXPRESSION',3,'p_expression_mul','test.py',64),
  ('EXPRESSION -> ( EXPRESSION )','EXPRESSION',3,'p_expression_group','test.py',71),
]
