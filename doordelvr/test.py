class ProcedureDefinition(object):
    def __init__(self):
        pass

    def get_procedures_def(self, procedure_name):
        return "==="+procedure_name+"=="

    
procedures=['test1', 'test2', 'test3']
proc_obj = ProcedureDefinition()
for proc_name in procedures:
    proc_def = proc_obj.get_procedures_def(proc_name)
    print(proc_def)






