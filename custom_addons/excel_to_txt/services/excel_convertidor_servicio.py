
import pandas as pd
import math 

class ExcelConvertirdorServicio:
    @staticmethod
    def conversor_excel(ruta_archivo):
        """
        Méotdo para transformar un archivo excel con las columnas: anio, concepto y valor
        Siguiendo las reglas: 
        anio -> Debe ser un valor numérico de cuatro dígitos. Si el valor no tiene cuatro
        dígitos, se debe completar con ceros a la izquierda

        concepto -> Debe ser un valor alfanumérico de máximo diez caracteres. Si el valor
        tiene menos de diez caracteres, se debe completar con "$" a la derecha
        
        valor ->  Debe ser un valor numérico de máximo veinte dígitos. Si el valor tiene menos
        de veinte dígitos, se debe completar con ceros a la izquierda

        Reglas adicionales del archivo
        Si un valor en el archivo Excel no cumple con ninguna de las reglas anteriores o no se
        encuentra relacionada ningún valor del Excel, se debe dejar tal cual está en el archivo
        Excel

        Si un valor numérico en el archivo Excel tiene valor NaN, se debe transformar a una
        cadena de texto vacía
        """

        try:
            data = pd.read_excel(ruta_archivo, dtype={"ANIO": str, "CONCEPTO": str, "VALOR": str})

            data_converter = [] #-> creo lista para almacenar datos convertidos

            for _, row in data.iterrows():
                anio = row["ANIO"]
                concepto = row["CONCEPTO"]
                valor = row["VALOR"]

                # Reglas de negocio
                anio = str(anio).zfill(4) if anio.isdigit() and len(anio) <= 4 else anio
                concepto = str(concepto).ljust(10, "$")[:10] 
                valor = str(valor).zfill(20) if valor.isdigit() and len(valor) <= 20 else valor

                # Manejo de Nan
                if isinstance(anio, float) and math.isnan(anio):
                    anio = ""
                if isinstance(concepto, float) and math.isnan(concepto):
                    concepto = ""
                if isinstance(valor, float) and math.isnan(valor):
                    valor = ""

                transformed_row = f"{anio}{concepto}{valor}" # -> contruyo el string final 
                data_converter.append(transformed_row) 

            return data_converter

        except Exception as e:
            return [f"Error el archivo no se puedo procesar: {str(e)}"]