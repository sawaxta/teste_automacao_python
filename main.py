
import time
import pandas as pd
import pyautogui as pg
import pyperclip as pc

def carregar_cnpjs(arquivo_csv):
    return pd.read_csv(arquivo_csv)

def validar_cnpjs_com_pyautogui(df):
    pg.hotkey('win')
    time.sleep(2)
    pg.write('opera')  # Substitua pelo navegador que estiver utilizando
    pg.press('enter')
    time.sleep(3)

    pg.write('https://www.4devs.com.br/validador_cnpj')
    pg.press('enter')
    time.sleep(5)

    cnpjs_validos = []
    cnpjs_invalidos = []

    for index, row in df.iterrows():
        cnpj = row['cnpj']
        pg.click(x=773, y=430)  # Ajuste conforme sua tela
        pg.hotkey('ctrl', 'a')
        pg.press('backspace')
        pg.typewrite(cnpj)
        pg.press("tab")
        pg.press("enter")
        time.sleep(5)

        pg.doubleClick(x=793, y=616)
        pg.hotkey('ctrl', 'a')
        pg.hotkey('ctrl', 'c')
        resultado = pc.paste()

        if 'Verdadeiro' in resultado:
            print(f"{cnpj} - válido")
            cnpjs_validos.append(cnpj)
            df.at[index, 'status'] = 'válido'
        else:
            print(f"{cnpj} - inválido")
            cnpjs_invalidos.append(cnpj)
            df.at[index, 'status'] = 'inválido'

    return df, cnpjs_validos, cnpjs_invalidos

def salvar_resultados(df, arquivo_csv):
    df.to_csv(arquivo_csv, index=False)

def main():
    arquivo_csv = 'cnpj.csv'
    df = carregar_cnpjs(arquivo_csv)
    df_atualizado, cnpjs_validos, cnpjs_invalidos = validar_cnpjs_com_pyautogui(df)
    salvar_resultados(df_atualizado, arquivo_csv)

    print("\nCNPJs válidos:")
    print(cnpjs_validos)
    print("\nCNPJs inválidos:")
    print(cnpjs_invalidos)

if __name__ == "__main__":
    main()