import pandas as pd

def process_file(file_path):
    try:
        # Carreguem el fitxer Excel en un DataFrame sense capçalera
        df = pd.read_excel(file_path, header=None)  # No considerem capçalera per a les columnes

        # Comprovem quantes columnes té el fitxer i extraiem les que ens interessen
        df = df[[0, 2]]  # Agafem la primera columna (Fila) i la tercera columna (Mean)

        # Assignem els noms de les columnes a mà (1a columna "Fila", 3a columna "Mean")
        df.columns = ["Fila", "Mean"]

        # Ens assegurem que la columna "Fila" és de tipus enter (per evitar errors amb % 2)
        df["Fila"] = pd.to_numeric(df["Fila"], errors='coerce')  # Convertim els valors a numèrics, convertint a NaN els errors

        # Creem dues llistes per als valors de les files parelles i senars
        mean_parells = []
        mean_senars = []

        # Iterem a través de les files i separem en funció si la fila és parella o senar
        for index, row in df.iterrows():
            if pd.notna(row["Fila"]) and row["Fila"] % 2 == 0:  # Ens assegurem que "Fila" no sigui NaN
                mean_parells.append(row["Mean"])
                mean_senars.append(None)  # No afegim cap valor per a les senars
            elif pd.notna(row["Fila"]):
                mean_senars.append(row["Mean"])
                mean_parells.append(None)  # No afegim cap valor per a les parelles

        # Eliminem valors NaN de les llistes per parells i senars
        mean_parells = [x for x in mean_parells if x is not None]
        mean_senars = [x for x in mean_senars if x is not None]

        # Creem el DataFrame final amb les llistes resultants
        df_filtered = pd.DataFrame({
            "Numeros": list(range(1, len(mean_parells) + 1)),
            "Mean_Parells": mean_parells,
            "Mean_Senars": mean_senars
        })

        # Generem el nou nom de fitxer afegint "_separat" al final del nom original
        new_file_path = file_path.replace(".xlsx", "_separat.xlsx")

        # Guardem el nou fitxer amb el separador "_separat"
        df_filtered.to_excel(new_file_path, index=False)

        print(f"✅ Fitxer processat i guardat com: {new_file_path}")

    except Exception as e:
        print(f"🚨 Error: {e}")

file_path = "C:/Users/jalegre/Desktop/New folder/A3/A3.xlsx"  # Substitueix per la ruta al teu fitxer Excel
process_file(file_path)
