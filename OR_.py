import turtle
import time
import os
import time, sys
from operator import pow, truediv, mul, add, sub

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}
def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))

def multi_input():
    try:
        while True:
            data=input("OR_ ")
            if not data : break
            yield data
    except KeyboardInterrupt:
        return
    
def typewriter(speed,string):
    for i in string:       
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(speed)

variables = {}
print(("OR_ Programming Language\n"))
print('Type "version" for version.\nType "syntax" for syntax.\nType "exit" to exit.\nTo execute a program just write the code\nand hit enter 2 times.\n-----------------------------------------')
while True:    
    user_input = list(multi_input())
    code = " ".join(user_input)
    codesplit = code.split(";")
    if 1 == 1:
         for c in user_input:
             if "=" in c:
                 varns = c.find("var(") + len("var(")
                 varne = c.find(")")
                 var_e = c.find("=")
                 value_e = c.find("=") + len("=")
                 var = c[varns:varne]
                 var = var.replace("int:","")
                 var = var.replace("str:","")
                 value = c[value_e:]
                 variables[var] = value
             elif 'print:"' in c:
                if c.replace(' ','')[-1] == ";":
                   print_start = c.find('print:"') + len('print:"')
                   print_end   = c.find('";')
                   print_con   = c[print_start:print_end]
                   print(print_con)
             elif 'print:var(' in c and '"' not in c:
               if c.replace(' ','')[-1] == ";":
                   prt_st = c.find('print:var(') + len('print:var(')
                   prt_en = c.find(')')
                   var_prt = c[prt_st:prt_en]
                   if var_prt in variables:
                       print(variables[var_prt])
                   else:
                       print('Unknown Variable "{}" found'.format(var_prt))
             elif '#' in c:
                global comment
                comment_start = c.find("#") + len("#")
                comment = c[comment_start:]
             elif '(comment)' in c:
                print(comment)
             elif 'typewriter(' in c:
               type_str = c.find('typewriter(') + len('typewriter(')
               type_eee = c.find(',"')
               type_con = c.find(',"') + len(',"')
               type_end = c.find('")')
               speed = float(c[type_str:type_eee])
               typewriter(speed,c[type_con:type_end])
               print()
             elif 'forward(' in c:
               fs = c.find("forward(") + len("forward(")
               fe = c.find(")")
               fd = c[fs:fe]
               fd = int(fd)
               turtle.forward(int(fd))
             elif 'backward(' in c:
               bs = c.find("backward(") + len("backward(")
               be = c.find(")")
               bd = c[bs:be]
               bd = int(bd)
               turtle.backward(int(bd))
             elif 'right(' in c:
               rs = c.find('right(') + len('right(')
               re = c.find(')')
               ri = c[rs:re]
               ri = int(ri)
               turtle.right(int(ri))
             elif 'left(' in c:
               ls = c.find('left(') + len('left(')
               le = c.find(')')
               lt = c[ls:le]
               lt = int(lt)
               turtle.left(int(lt))
             elif 'goto(' in c:
               gtxs = c.find('goto(') + len('goto(')
               gtxe = c.find(',')
               gtys = c.find(',') + len(',')
               gtye = c.find(')')
               gtx  = c[gtxs:gtxe]
               gty  = c[gtys:gtye]
               gtx  = int(gtx)
               gty  = int(gty)
               turtle.goto(int(gtx),int(gty))
             elif 'penup()' in c :
               turtle.up()
             elif 'pendown()' in c :
               turtle.down()
             elif 'bgcolor(' in c :
               bgcs = c.find('bgcolor') + len('bgcolor(')
               bgce = c.find(')')
               bg   = c[bgcs:bgce]
               turtle.bgcolor(bg)
             elif 'pencolor(' in c :
               pcs = c.find('pencolor(') + len('pencolor(')      
               pce = c.find(')')
               pcr = c[pcs:pce]
               turtle.pencolor(pcr)
             elif 'sleep(' in c:
               s_s = c.find("sleep(") + len("sleep(")
               s_e = c.find(")")
               sec = c[s_s:s_e]
               sec = float(sec)
               time.sleep(float(sec))
             elif 'piechart(' in c:
                 pass
             elif c == "version":
               print("////////////////////\n"
                     "// version: 0.8.0 //\n"
                     "////////////////////")
             elif c == "syntax":
               print("--------SYNTAX--------")
               print('')
               print('to print any statement:\n  syntax:\n    print("text here")\n  example:\n    print("hello, OR_!")')
               print('to print any calculation:\n  syntax:\n    print(expression)\n  example:\n    print(1+2)')
               print('to make comments:\n  syntax:\n    #comment\n  example:\n    #blah,blah,blah')
               print('to print with delay in each character:\n  syntax:\n    typewriter(speed-in-seconds,"text goes here")\n  example:\n    typewriter(0.5,"Hello, OR_")')
               print('to wait for some time:\n  syntax:\n    sleep(seconds)\n  example:\n    sleep(1)')
               print("TURTLE WORK:")
               print("forward command:\n    syntax:\n      forward(value)") 
               print('backward:\n    syntax:\n      backward(value)')
               print('right:\n    syntax:\n      right(value)')
               print('left:\n    syntax:\n      left(value)')
               print('goto:\n    syntax:\n      goto(x,y)')
               print('penup:\n    syntax:\n      penup()')
               print('pendown:\n    syntax:\n      pendown() ')
               print('background color:\n    syntax:\n      bgcolor(color)')
               print('pencolor:\n    syntax:\n      pencolor(color)')
             elif "exit" in c:
               sys.exit("...")
             else:
               print(('  NO COMMAND FOUND  '))
