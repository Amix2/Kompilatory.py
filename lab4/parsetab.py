
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIFleftELSEnonassocGTLTLEGENEEQnonassocADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNleft*/DOTMULDOTDIVleft+-DOTADDDOTSUBleftexprrightuminusleft\'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOATNUM FOR GE GT ID IF INTNUM LE LT MULASSIGN NE ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSSTART : START INSTRUCTION\n             | INSTRUCTION INSTRUCTION : \'{\' START \'}\'\n                   | ASSIGN_EXP\n                   | IF_INSTRUCTION\n                   | WHILE_INSTRUCTION\n                   | FOR_INSTRUCTION\n                   | PRINT_FUN\n                   | RETURN_FUN\n                   | BREAK \';\'\n                   | CONTINUE \';\' VECTOR : \'[\' LIST_VALUE \']\'VALUE : INTNUM\n             | FLOATNUM\n             | ID\n             | STRING\n             | EYE \'(\' ARITHMETIC_EXP \')\'\n             | ZEROS \'(\' ARITHMETIC_EXP \')\'\n             | ONES \'(\' ARITHMETIC_EXP \')\'\n             | VECTOR\n             | ID VECTOR\n             | VALUE "\'" LIST_VALUE : VALUE\n                  | VALUE \',\' LIST_VALUEARITHMETIC_OP : \'+\'\n                     | \'-\'\n                     | \'*\'\n                     | \'/\'\n                     | DOTADD\n                     | DOTSUB\n                     | DOTMUL\n                     | DOTDIV ASSIGN_OP : ADDASSIGN\n                 | SUBASSIGN\n                 | MULASSIGN\n                 | DIVASSIGN\n                 | \'=\' RELATION_OP : GT\n                   | LT\n                   | LE\n                   | GE\n                   | NE\n                   | EQ ARITHMETIC_OP_UNARY : \'+\'\n                           | \'-\' ARITHMETIC_EXP : ARITHMETIC_EXP ARITHMETIC_OP ARITHMETIC_EXP %prec expr\n                     | \'(\' ARITHMETIC_EXP \')\'\n                     | ARITHMETIC_OP_UNARY ARITHMETIC_EXP %prec uminus\n                     | VALUERELATION_EXP : ARITHMETIC_EXP RELATION_OP ARITHMETIC_EXP\n                    | \'(\' RELATION_EXP \')\'ASSIGN_EXP : ID ASSIGN_OP ARITHMETIC_EXP \';\'\n                    | ID \'[\' LIST_VALUE \']\' ASSIGN_OP ARITHMETIC_EXP \';\' IF_INSTRUCTION : IF \'(\' RELATION_EXP  \')\' INSTRUCTION %prec IF\n                      | IF \'(\' RELATION_EXP  \')\' INSTRUCTION  ELSE INSTRUCTION WHILE_INSTRUCTION : WHILE \'(\' RELATION_EXP  \')\' INSTRUCTION FOR_INSTRUCTION : FOR ID \'=\' ARITHMETIC_EXP \':\' ARITHMETIC_EXP INSTRUCTION PRINT_FUN : PRINT LIST_VALUE \';\'RETURN_FUN : RETURN LIST_VALUE \';\''
    
_lr_action_items = {'{':([0,1,2,3,4,5,6,7,8,9,18,19,20,21,34,35,36,37,41,44,48,57,59,60,65,66,77,81,89,95,96,97,100,102,104,105,106,108,109,110,111,112,],[3,3,-2,3,-4,-5,-6,-7,-8,-9,-1,3,-10,-11,-13,-14,-15,-16,-20,-3,-49,-58,-22,-21,-59,-52,-48,3,3,-12,-46,-47,-54,-56,-17,-18,-19,3,3,-53,-55,-57,]),'BREAK':([0,1,2,3,4,5,6,7,8,9,18,19,20,21,34,35,36,37,41,44,48,57,59,60,65,66,77,81,89,95,96,97,100,102,104,105,106,108,109,110,111,112,],[10,10,-2,10,-4,-5,-6,-7,-8,-9,-1,10,-10,-11,-13,-14,-15,-16,-20,-3,-49,-58,-22,-21,-59,-52,-48,10,10,-12,-46,-47,-54,-56,-17,-18,-19,10,10,-53,-55,-57,]),'CONTINUE':([0,1,2,3,4,5,6,7,8,9,18,19,20,21,34,35,36,37,41,44,48,57,59,60,65,66,77,81,89,95,96,97,100,102,104,105,106,108,109,110,111,112,],[11,11,-2,11,-4,-5,-6,-7,-8,-9,-1,11,-10,-11,-13,-14,-15,-16,-20,-3,-49,-58,-22,-21,-59,-52,-48,11,11,-12,-46,-47,-54,-56,-17,-18,-19,11,11,-53,-55,-57,]),'ID':([0,1,2,3,4,5,6,7,8,9,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,35,36,37,41,42,44,46,47,48,49,50,52,56,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,77,81,82,83,84,85,86,87,88,89,95,96,97,98,100,102,103,104,105,106,108,109,110,111,112,],[12,12,-2,12,-4,-5,-6,-7,-8,-9,31,36,36,-1,12,-10,-11,36,36,-33,-34,-35,-36,-37,36,36,-13,-14,-15,-16,-20,36,-3,36,36,-49,-44,-45,36,36,-58,36,-22,-21,36,36,36,-59,-52,36,-25,-26,-27,-28,-29,-30,-31,-32,-48,12,36,-38,-39,-40,-41,-42,-43,12,-12,-46,-47,36,-54,-56,36,-17,-18,-19,12,12,-53,-55,-57,]),'IF':([0,1,2,3,4,5,6,7,8,9,18,19,20,21,34,35,36,37,41,44,48,57,59,60,65,66,77,81,89,95,96,97,100,102,104,105,106,108,109,110,111,112,],[13,13,-2,13,-4,-5,-6,-7,-8,-9,-1,13,-10,-11,-13,-14,-15,-16,-20,-3,-49,-58,-22,-21,-59,-52,-48,13,13,-12,-46,-47,-54,-56,-17,-18,-19,13,13,-53,-55,-57,]),'WHILE':([0,1,2,3,4,5,6,7,8,9,18,19,20,21,34,35,36,37,41,44,48,57,59,60,65,66,77,81,89,95,96,97,100,102,104,105,106,108,109,110,111,112,],[14,14,-2,14,-4,-5,-6,-7,-8,-9,-1,14,-10,-11,-13,-14,-15,-16,-20,-3,-49,-58,-22,-21,-59,-52,-48,14,14,-12,-46,-47,-54,-56,-17,-18,-19,14,14,-53,-55,-57,]),'FOR':([0,1,2,3,4,5,6,7,8,9,18,19,20,21,34,35,36,37,41,44,48,57,59,60,65,66,77,81,89,95,96,97,100,102,104,105,106,108,109,110,111,112,],[15,15,-2,15,-4,-5,-6,-7,-8,-9,-1,15,-10,-11,-13,-14,-15,-16,-20,-3,-49,-58,-22,-21,-59,-52,-48,15,15,-12,-46,-47,-54,-56,-17,-18,-19,15,15,-53,-55,-57,]),'PRINT':([0,1,2,3,4,5,6,7,8,9,18,19,20,21,34,35,36,37,41,44,48,57,59,60,65,66,77,81,89,95,96,97,100,102,104,105,106,108,109,110,111,112,],[16,16,-2,16,-4,-5,-6,-7,-8,-9,-1,16,-10,-11,-13,-14,-15,-16,-20,-3,-49,-58,-22,-21,-59,-52,-48,16,16,-12,-46,-47,-54,-56,-17,-18,-19,16,16,-53,-55,-57,]),'RETURN':([0,1,2,3,4,5,6,7,8,9,18,19,20,21,34,35,36,37,41,44,48,57,59,60,65,66,77,81,89,95,96,97,100,102,104,105,106,108,109,110,111,112,],[17,17,-2,17,-4,-5,-6,-7,-8,-9,-1,17,-10,-11,-13,-14,-15,-16,-20,-3,-49,-58,-22,-21,-59,-52,-48,17,17,-12,-46,-47,-54,-56,-17,-18,-19,17,17,-53,-55,-57,]),'$end':([1,2,4,5,6,7,8,9,18,20,21,44,57,65,66,100,102,110,111,112,],[0,-2,-4,-5,-6,-7,-8,-9,-1,-10,-11,-3,-58,-59,-52,-54,-56,-53,-55,-57,]),'}':([2,4,5,6,7,8,9,18,19,20,21,44,57,65,66,100,102,110,111,112,],[-2,-4,-5,-6,-7,-8,-9,-1,44,-10,-11,-3,-58,-59,-52,-54,-56,-53,-55,-57,]),'ELSE':([4,5,6,7,8,9,20,21,44,57,65,66,100,102,110,111,112,],[-4,-5,-6,-7,-8,-9,-10,-11,-3,-58,-59,-52,108,-56,-53,-55,-57,]),';':([10,11,32,33,34,35,36,37,41,43,45,48,59,60,77,91,95,96,97,104,105,106,107,],[20,21,57,-23,-13,-14,-15,-16,-20,65,66,-49,-22,-21,-48,-24,-12,-46,-47,-17,-18,-19,110,]),'[':([12,16,17,22,23,24,25,26,27,28,29,30,36,42,46,47,49,50,52,56,58,61,62,63,67,68,69,70,71,72,73,74,75,82,83,84,85,86,87,88,98,103,],[23,42,42,42,42,-33,-34,-35,-36,-37,42,42,42,42,42,42,-44,-45,42,42,42,42,42,42,42,-25,-26,-27,-28,-29,-30,-31,-32,42,-38,-39,-40,-41,-42,-43,42,42,]),'ADDASSIGN':([12,78,],[24,24,]),'SUBASSIGN':([12,78,],[25,25,]),'MULASSIGN':([12,78,],[26,26,]),'DIVASSIGN':([12,78,],[27,27,]),'=':([12,31,78,],[28,56,28,]),'(':([13,14,22,24,25,26,27,28,29,30,38,39,40,46,47,49,50,52,56,61,62,63,67,68,69,70,71,72,73,74,75,82,83,84,85,86,87,88,98,103,],[29,30,46,-33,-34,-35,-36,-37,52,52,61,62,63,46,46,-44,-45,52,46,46,46,46,46,-25,-26,-27,-28,-29,-30,-31,-32,46,-38,-39,-40,-41,-42,-43,46,46,]),'INTNUM':([16,17,22,23,24,25,26,27,28,29,30,42,46,47,49,50,52,56,58,61,62,63,67,68,69,70,71,72,73,74,75,82,83,84,85,86,87,88,98,103,],[34,34,34,34,-33,-34,-35,-36,-37,34,34,34,34,34,-44,-45,34,34,34,34,34,34,34,-25,-26,-27,-28,-29,-30,-31,-32,34,-38,-39,-40,-41,-42,-43,34,34,]),'FLOATNUM':([16,17,22,23,24,25,26,27,28,29,30,42,46,47,49,50,52,56,58,61,62,63,67,68,69,70,71,72,73,74,75,82,83,84,85,86,87,88,98,103,],[35,35,35,35,-33,-34,-35,-36,-37,35,35,35,35,35,-44,-45,35,35,35,35,35,35,35,-25,-26,-27,-28,-29,-30,-31,-32,35,-38,-39,-40,-41,-42,-43,35,35,]),'STRING':([16,17,22,23,24,25,26,27,28,29,30,42,46,47,49,50,52,56,58,61,62,63,67,68,69,70,71,72,73,74,75,82,83,84,85,86,87,88,98,103,],[37,37,37,37,-33,-34,-35,-36,-37,37,37,37,37,37,-44,-45,37,37,37,37,37,37,37,-25,-26,-27,-28,-29,-30,-31,-32,37,-38,-39,-40,-41,-42,-43,37,37,]),'EYE':([16,17,22,23,24,25,26,27,28,29,30,42,46,47,49,50,52,56,58,61,62,63,67,68,69,70,71,72,73,74,75,82,83,84,85,86,87,88,98,103,],[38,38,38,38,-33,-34,-35,-36,-37,38,38,38,38,38,-44,-45,38,38,38,38,38,38,38,-25,-26,-27,-28,-29,-30,-31,-32,38,-38,-39,-40,-41,-42,-43,38,38,]),'ZEROS':([16,17,22,23,24,25,26,27,28,29,30,42,46,47,49,50,52,56,58,61,62,63,67,68,69,70,71,72,73,74,75,82,83,84,85,86,87,88,98,103,],[39,39,39,39,-33,-34,-35,-36,-37,39,39,39,39,39,-44,-45,39,39,39,39,39,39,39,-25,-26,-27,-28,-29,-30,-31,-32,39,-38,-39,-40,-41,-42,-43,39,39,]),'ONES':([16,17,22,23,24,25,26,27,28,29,30,42,46,47,49,50,52,56,58,61,62,63,67,68,69,70,71,72,73,74,75,82,83,84,85,86,87,88,98,103,],[40,40,40,40,-33,-34,-35,-36,-37,40,40,40,40,40,-44,-45,40,40,40,40,40,40,40,-25,-26,-27,-28,-29,-30,-31,-32,40,-38,-39,-40,-41,-42,-43,40,40,]),'+':([22,24,25,26,27,28,29,30,34,35,36,37,41,45,46,47,48,49,50,52,54,56,59,60,61,62,63,67,68,69,70,71,72,73,74,75,76,77,80,82,83,84,85,86,87,88,90,92,93,94,95,96,97,98,101,103,104,105,106,107,109,],[49,-33,-34,-35,-36,-37,49,49,-13,-14,-15,-16,-20,68,49,49,-49,-44,-45,49,68,49,-22,-21,49,49,49,49,-25,-26,-27,-28,-29,-30,-31,-32,68,-48,68,49,-38,-39,-40,-41,-42,-43,68,68,68,68,-12,-46,-47,49,68,49,-17,-18,-19,68,68,]),'-':([22,24,25,26,27,28,29,30,34,35,36,37,41,45,46,47,48,49,50,52,54,56,59,60,61,62,63,67,68,69,70,71,72,73,74,75,76,77,80,82,83,84,85,86,87,88,90,92,93,94,95,96,97,98,101,103,104,105,106,107,109,],[50,-33,-34,-35,-36,-37,50,50,-13,-14,-15,-16,-20,69,50,50,-49,-44,-45,50,69,50,-22,-21,50,50,50,50,-25,-26,-27,-28,-29,-30,-31,-32,69,-48,69,50,-38,-39,-40,-41,-42,-43,69,69,69,69,-12,-46,-47,50,69,50,-17,-18,-19,69,69,]),']':([33,34,35,36,37,41,51,59,60,64,91,95,104,105,106,],[-23,-13,-14,-15,-16,-20,78,-22,-21,95,-24,-12,-17,-18,-19,]),',':([33,34,35,36,37,41,59,60,95,104,105,106,],[58,-13,-14,-15,-16,-20,-22,-21,-12,-17,-18,-19,]),"'":([33,34,35,36,37,41,48,59,60,95,104,105,106,],[59,-13,-14,-15,-16,-20,59,-22,-21,-12,-17,-18,-19,]),'*':([34,35,36,37,41,45,48,54,59,60,76,77,80,90,92,93,94,95,96,97,101,104,105,106,107,109,],[-13,-14,-15,-16,-20,70,-49,70,-22,-21,70,-48,70,70,70,70,70,-12,-46,-47,70,-17,-18,-19,70,70,]),'/':([34,35,36,37,41,45,48,54,59,60,76,77,80,90,92,93,94,95,96,97,101,104,105,106,107,109,],[-13,-14,-15,-16,-20,71,-49,71,-22,-21,71,-48,71,71,71,71,71,-12,-46,-47,71,-17,-18,-19,71,71,]),'DOTADD':([34,35,36,37,41,45,48,54,59,60,76,77,80,90,92,93,94,95,96,97,101,104,105,106,107,109,],[-13,-14,-15,-16,-20,72,-49,72,-22,-21,72,-48,72,72,72,72,72,-12,-46,-47,72,-17,-18,-19,72,72,]),'DOTSUB':([34,35,36,37,41,45,48,54,59,60,76,77,80,90,92,93,94,95,96,97,101,104,105,106,107,109,],[-13,-14,-15,-16,-20,73,-49,73,-22,-21,73,-48,73,73,73,73,73,-12,-46,-47,73,-17,-18,-19,73,73,]),'DOTMUL':([34,35,36,37,41,45,48,54,59,60,76,77,80,90,92,93,94,95,96,97,101,104,105,106,107,109,],[-13,-14,-15,-16,-20,74,-49,74,-22,-21,74,-48,74,74,74,74,74,-12,-46,-47,74,-17,-18,-19,74,74,]),'DOTDIV':([34,35,36,37,41,45,48,54,59,60,76,77,80,90,92,93,94,95,96,97,101,104,105,106,107,109,],[-13,-14,-15,-16,-20,75,-49,75,-22,-21,75,-48,75,75,75,75,75,-12,-46,-47,75,-17,-18,-19,75,75,]),'GT':([34,35,36,37,41,48,54,59,60,77,80,95,96,97,104,105,106,],[-13,-14,-15,-16,-20,-49,83,-22,-21,-48,83,-12,-46,-47,-17,-18,-19,]),'LT':([34,35,36,37,41,48,54,59,60,77,80,95,96,97,104,105,106,],[-13,-14,-15,-16,-20,-49,84,-22,-21,-48,84,-12,-46,-47,-17,-18,-19,]),'LE':([34,35,36,37,41,48,54,59,60,77,80,95,96,97,104,105,106,],[-13,-14,-15,-16,-20,-49,85,-22,-21,-48,85,-12,-46,-47,-17,-18,-19,]),'GE':([34,35,36,37,41,48,54,59,60,77,80,95,96,97,104,105,106,],[-13,-14,-15,-16,-20,-49,86,-22,-21,-48,86,-12,-46,-47,-17,-18,-19,]),'NE':([34,35,36,37,41,48,54,59,60,77,80,95,96,97,104,105,106,],[-13,-14,-15,-16,-20,-49,87,-22,-21,-48,87,-12,-46,-47,-17,-18,-19,]),'EQ':([34,35,36,37,41,48,54,59,60,77,80,95,96,97,104,105,106,],[-13,-14,-15,-16,-20,-49,88,-22,-21,-48,88,-12,-46,-47,-17,-18,-19,]),')':([34,35,36,37,41,48,53,55,59,60,76,77,79,80,92,93,94,95,96,97,99,101,104,105,106,],[-13,-14,-15,-16,-20,-49,81,89,-22,-21,97,-48,99,97,104,105,106,-12,-46,-47,-51,-50,-17,-18,-19,]),':':([34,35,36,37,41,48,59,60,77,90,95,96,97,104,105,106,],[-13,-14,-15,-16,-20,-49,-22,-21,-48,103,-12,-46,-47,-17,-18,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'START':([0,3,],[1,19,]),'INSTRUCTION':([0,1,3,19,81,89,108,109,],[2,18,2,18,100,102,111,112,]),'ASSIGN_EXP':([0,1,3,19,81,89,108,109,],[4,4,4,4,4,4,4,4,]),'IF_INSTRUCTION':([0,1,3,19,81,89,108,109,],[5,5,5,5,5,5,5,5,]),'WHILE_INSTRUCTION':([0,1,3,19,81,89,108,109,],[6,6,6,6,6,6,6,6,]),'FOR_INSTRUCTION':([0,1,3,19,81,89,108,109,],[7,7,7,7,7,7,7,7,]),'PRINT_FUN':([0,1,3,19,81,89,108,109,],[8,8,8,8,8,8,8,8,]),'RETURN_FUN':([0,1,3,19,81,89,108,109,],[9,9,9,9,9,9,9,9,]),'ASSIGN_OP':([12,78,],[22,98,]),'LIST_VALUE':([16,17,23,42,58,],[32,43,51,64,91,]),'VALUE':([16,17,22,23,29,30,42,46,47,52,56,58,61,62,63,67,82,98,103,],[33,33,48,33,48,48,33,48,48,48,48,33,48,48,48,48,48,48,48,]),'VECTOR':([16,17,22,23,29,30,36,42,46,47,52,56,58,61,62,63,67,82,98,103,],[41,41,41,41,41,41,60,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'ARITHMETIC_EXP':([22,29,30,46,47,52,56,61,62,63,67,82,98,103,],[45,54,54,76,77,80,90,92,93,94,96,101,107,109,]),'ARITHMETIC_OP_UNARY':([22,29,30,46,47,52,56,61,62,63,67,82,98,103,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'RELATION_EXP':([29,30,52,],[53,55,79,]),'ARITHMETIC_OP':([45,54,76,77,80,90,92,93,94,96,101,107,109,],[67,67,67,67,67,67,67,67,67,67,67,67,67,]),'RELATION_OP':([54,80,],[82,82,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> START","S'",1,None,None,None),
  ('START -> START INSTRUCTION','START',2,'p_start','Mparser.py',34),
  ('START -> INSTRUCTION','START',1,'p_start','Mparser.py',35),
  ('INSTRUCTION -> { START }','INSTRUCTION',3,'p_instruction','Mparser.py',44),
  ('INSTRUCTION -> ASSIGN_EXP','INSTRUCTION',1,'p_instruction','Mparser.py',45),
  ('INSTRUCTION -> IF_INSTRUCTION','INSTRUCTION',1,'p_instruction','Mparser.py',46),
  ('INSTRUCTION -> WHILE_INSTRUCTION','INSTRUCTION',1,'p_instruction','Mparser.py',47),
  ('INSTRUCTION -> FOR_INSTRUCTION','INSTRUCTION',1,'p_instruction','Mparser.py',48),
  ('INSTRUCTION -> PRINT_FUN','INSTRUCTION',1,'p_instruction','Mparser.py',49),
  ('INSTRUCTION -> RETURN_FUN','INSTRUCTION',1,'p_instruction','Mparser.py',50),
  ('INSTRUCTION -> BREAK ;','INSTRUCTION',2,'p_instruction','Mparser.py',51),
  ('INSTRUCTION -> CONTINUE ;','INSTRUCTION',2,'p_instruction','Mparser.py',52),
  ('VECTOR -> [ LIST_VALUE ]','VECTOR',3,'p_basic_vector','Mparser.py',64),
  ('VALUE -> INTNUM','VALUE',1,'p_basic_value','Mparser.py',68),
  ('VALUE -> FLOATNUM','VALUE',1,'p_basic_value','Mparser.py',69),
  ('VALUE -> ID','VALUE',1,'p_basic_value','Mparser.py',70),
  ('VALUE -> STRING','VALUE',1,'p_basic_value','Mparser.py',71),
  ('VALUE -> EYE ( ARITHMETIC_EXP )','VALUE',4,'p_basic_value','Mparser.py',72),
  ('VALUE -> ZEROS ( ARITHMETIC_EXP )','VALUE',4,'p_basic_value','Mparser.py',73),
  ('VALUE -> ONES ( ARITHMETIC_EXP )','VALUE',4,'p_basic_value','Mparser.py',74),
  ('VALUE -> VECTOR','VALUE',1,'p_basic_value','Mparser.py',75),
  ('VALUE -> ID VECTOR','VALUE',2,'p_basic_value','Mparser.py',76),
  ("VALUE -> VALUE '",'VALUE',2,'p_basic_value','Mparser.py',77),
  ('LIST_VALUE -> VALUE','LIST_VALUE',1,'p_basic_list_values','Mparser.py',91),
  ('LIST_VALUE -> VALUE , LIST_VALUE','LIST_VALUE',3,'p_basic_list_values','Mparser.py',92),
  ('ARITHMETIC_OP -> +','ARITHMETIC_OP',1,'p_basic_arithmetic_op','Mparser.py',101),
  ('ARITHMETIC_OP -> -','ARITHMETIC_OP',1,'p_basic_arithmetic_op','Mparser.py',102),
  ('ARITHMETIC_OP -> *','ARITHMETIC_OP',1,'p_basic_arithmetic_op','Mparser.py',103),
  ('ARITHMETIC_OP -> /','ARITHMETIC_OP',1,'p_basic_arithmetic_op','Mparser.py',104),
  ('ARITHMETIC_OP -> DOTADD','ARITHMETIC_OP',1,'p_basic_arithmetic_op','Mparser.py',105),
  ('ARITHMETIC_OP -> DOTSUB','ARITHMETIC_OP',1,'p_basic_arithmetic_op','Mparser.py',106),
  ('ARITHMETIC_OP -> DOTMUL','ARITHMETIC_OP',1,'p_basic_arithmetic_op','Mparser.py',107),
  ('ARITHMETIC_OP -> DOTDIV','ARITHMETIC_OP',1,'p_basic_arithmetic_op','Mparser.py',108),
  ('ASSIGN_OP -> ADDASSIGN','ASSIGN_OP',1,'p_basic_assign_op','Mparser.py',112),
  ('ASSIGN_OP -> SUBASSIGN','ASSIGN_OP',1,'p_basic_assign_op','Mparser.py',113),
  ('ASSIGN_OP -> MULASSIGN','ASSIGN_OP',1,'p_basic_assign_op','Mparser.py',114),
  ('ASSIGN_OP -> DIVASSIGN','ASSIGN_OP',1,'p_basic_assign_op','Mparser.py',115),
  ('ASSIGN_OP -> =','ASSIGN_OP',1,'p_basic_assign_op','Mparser.py',116),
  ('RELATION_OP -> GT','RELATION_OP',1,'p_basic_relation_op','Mparser.py',120),
  ('RELATION_OP -> LT','RELATION_OP',1,'p_basic_relation_op','Mparser.py',121),
  ('RELATION_OP -> LE','RELATION_OP',1,'p_basic_relation_op','Mparser.py',122),
  ('RELATION_OP -> GE','RELATION_OP',1,'p_basic_relation_op','Mparser.py',123),
  ('RELATION_OP -> NE','RELATION_OP',1,'p_basic_relation_op','Mparser.py',124),
  ('RELATION_OP -> EQ','RELATION_OP',1,'p_basic_relation_op','Mparser.py',125),
  ('ARITHMETIC_OP_UNARY -> +','ARITHMETIC_OP_UNARY',1,'p_basic_arithmetic_op_unar','Mparser.py',129),
  ('ARITHMETIC_OP_UNARY -> -','ARITHMETIC_OP_UNARY',1,'p_basic_arithmetic_op_unar','Mparser.py',130),
  ('ARITHMETIC_EXP -> ARITHMETIC_EXP ARITHMETIC_OP ARITHMETIC_EXP','ARITHMETIC_EXP',3,'p_exp_arithmetic','Mparser.py',135),
  ('ARITHMETIC_EXP -> ( ARITHMETIC_EXP )','ARITHMETIC_EXP',3,'p_exp_arithmetic','Mparser.py',136),
  ('ARITHMETIC_EXP -> ARITHMETIC_OP_UNARY ARITHMETIC_EXP','ARITHMETIC_EXP',2,'p_exp_arithmetic','Mparser.py',137),
  ('ARITHMETIC_EXP -> VALUE','ARITHMETIC_EXP',1,'p_exp_arithmetic','Mparser.py',138),
  ('RELATION_EXP -> ARITHMETIC_EXP RELATION_OP ARITHMETIC_EXP','RELATION_EXP',3,'p_exp_relation','Mparser.py',149),
  ('RELATION_EXP -> ( RELATION_EXP )','RELATION_EXP',3,'p_exp_relation','Mparser.py',150),
  ('ASSIGN_EXP -> ID ASSIGN_OP ARITHMETIC_EXP ;','ASSIGN_EXP',4,'p_exp_assign','Mparser.py',157),
  ('ASSIGN_EXP -> ID [ LIST_VALUE ] ASSIGN_OP ARITHMETIC_EXP ;','ASSIGN_EXP',7,'p_exp_assign','Mparser.py',158),
  ('IF_INSTRUCTION -> IF ( RELATION_EXP ) INSTRUCTION','IF_INSTRUCTION',5,'p_instruction_if','Mparser.py',165),
  ('IF_INSTRUCTION -> IF ( RELATION_EXP ) INSTRUCTION ELSE INSTRUCTION','IF_INSTRUCTION',7,'p_instruction_if','Mparser.py',166),
  ('WHILE_INSTRUCTION -> WHILE ( RELATION_EXP ) INSTRUCTION','WHILE_INSTRUCTION',5,'p_instruction_while','Mparser.py',170),
  ('FOR_INSTRUCTION -> FOR ID = ARITHMETIC_EXP : ARITHMETIC_EXP INSTRUCTION','FOR_INSTRUCTION',7,'p_instruction_for','Mparser.py',174),
  ('PRINT_FUN -> PRINT LIST_VALUE ;','PRINT_FUN',3,'p_fun_print','Mparser.py',178),
  ('RETURN_FUN -> RETURN LIST_VALUE ;','RETURN_FUN',3,'p_fun_return','Mparser.py',181),
]
