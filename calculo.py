import streamlit as st


def cal(y):
  return 120 - y
  
  def main():
  st.title("Média Final")
  st.write("Calculadora simples")
  y = st.number_input("Digite sua nota MI")
  
  operation = st.selectbox("Selecione uma operação", ["Calcular"])
  if operation == "Calcular":
    st.write(cal(y))
    
  else:
    st.write("0000")
if __name__ == '__main__':
  main()
