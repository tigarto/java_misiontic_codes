import os
arr = os.listdir()
#print(arr)
files_java = []
for f in arr:    
    if(".java" in f):            
        files_java.append(f)
print(files_java)


def removerNumerosLineas(linea):
    lineaLimpia = ""
    ban = False 
    if len(linea) != 0:
        if linea[0].isdigit() == True:
            lineaLimpia = linea[1:] 
    if len(lineaLimpia) != 0:
        if lineaLimpia[0].isdigit() == True:
            lineaLimpia = lineaLimpia[1:]  
                      
    return lineaLimpia[1:-1]

      
for f in files_java:
    archivo = f
    (nombre,extencion) = archivo.split('.')
    inFile = open(archivo,'r')
    outFile = open(nombre + '2.' + extencion,'w')
    for linea in inFile:
        if len(linea) != 0:        
            lineaLimpia = removerNumerosLineas(linea) 
            #print(lineaLimpia)
            outFile.write(lineaLimpia + '\n')
            #print(linea)  
    inFile.close()
    outFile.close()


