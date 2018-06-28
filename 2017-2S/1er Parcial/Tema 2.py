resultado = "Resultado de Laboratorio 'Su Salud' Nombre del Paciente: Jose Aimas E-mail del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundo BGT 180.12 mmol/dl HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/uL TA 1.5 ngdL WBC 123233.23 cel/uL. Los valores de este informe no representan un diagnóstico. Firma médico responsable Dr. Juan Pozo"

datos_resultado = resultado.split(" ")

recomendacion = False
medico = []
informe = "INFORME DE LABORATORIO"
print(informe+"\n"+("*"*len(informe))+"\n")

for pos in range(len(datos_resultado)):
    if datos_resultado[pos].isupper():
        indicador = datos_resultado[pos]
        valor = float(datos_resultado[pos+1])
        unidad = datos_resultado[pos+2]
        if indicador == "BGT" and valor>150:
            recomendacion = True
            unidad+=" **"
        print(indicador,str(valor),unidad)
    elif datos_resultado[pos].lower() == "médico":
        medico=datos_resultado[pos+3:]
print("Médico:"," ".join(medico))
if recomendacion:
    print("**Su nivel de azúcar es alto, se recomienda ir al endocrinólogo.")