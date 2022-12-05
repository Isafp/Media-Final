import streamlit as st


y=int(input("Digite sua nota MI: "))
f = 120-y

  def main():
  st.title("Média Final")
  st.write("Calculadora simples")
    
  operation = st.selectbox("Selecione uma operação", ["Calcular"])
 if operation == "Calcular":

    print("Você precisa tirar no mínimo "+ str(f))
    
  else:
    st.write("0000")
if __name__ == '__main__':
  main()
