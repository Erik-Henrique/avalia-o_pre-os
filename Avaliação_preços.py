import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(layout='wide',
                   page_title='IMOVEIS.COM.VC',
                   page_icon='https://cdn-icons-png.flaticon.com/512/6395/6395159.png')


@st.cache_data
def load_data(data):
  return pd.read_csv(data)

df = load_data(r"C:\Users\erikd\OneDrive\Área de Trabalho\Base de dados\Projeto Insights Dados sobre venda de casas\kc_house_data.csv")

page_bg_img = """
  <style>
  [data-testid="stAppViewContainer"] {
  background-image: url("https://c0.wallpaperflare.com/preview/952/929/86/sao-paulo-brazil-predios-centro.jpg");
  background-size: cover;
  }
  [data-testid="stHeader"] {
  background-color: rgba(0,0,0,0);
  }
  </style>
  """
st.markdown(page_bg_img, unsafe_allow_html=True)

df.columns = ['id','data_venda','preco','qtd_quartos','qtd_banheiros','tamanho_casa','tamanho_lote','qtd_andares','vista_mar',
              'visualizacao_casa','condicao','nota','tamanho_alem_do_porao','tamanho_porao','ano_construcao','ano_reforma',
              'codigo_postal','LATITUDE','LONGITUDE','sqft_living15','sqft_lot15']

df.drop(['id', 'tamanho_alem_do_porao', 'sqft_living15', 'sqft_lot15','data_venda','visualizacao_casa'], axis=1, inplace=True)

st.markdown('# Seja bem-vindo')
st.markdown('### Aqui você irá conseguir comparar os valores dos imoveis de acordo com a região e as caracteristicas desejadas.')

col1, col2 = st.columns(2)


with col1:
  cep = st.selectbox('Selecione o Código postal da localidade desejada:',[98001,98002,98003,98004,98005,98006,98007,98008,98010,98011,98014,98019,98022,98023,98024,
                                                                98027,98028,98029,98030,98031,98032,98033,98034,98038,98039,98040,98042,98045,98052,98053,98055,98056,
                                                                98058,98059,98065,98070,98072,98074,98075,98077,98092,98102,98103, 98105, 98106, 98107,98108,98109,
                                                                98112,98115,98116,98117,98118,98119,98122,98125,98126,98133,98136,98144,98146,98148,98155,98166,98168,98177,98178,98188,98198,98199]) 
  filtered_cep = df[df['codigo_postal'] == cep]
  st.map(filtered_cep)


with col2:
   plt.figure(figsize=(10,10))
   var = st.selectbox('Selecione a caracteristica que deseja ver em comparação ao preço na localidade selecionada:',['Quantidade de quartos','Quantidade de banheiros','Tamanho da casa','Tamanho do lote','Quantidade de andares','Vista para o mar',
              'Condição do imóvel','Nota do imóvel','Tamanho do porão','Ano da construção','Ano da reforma'])
   if var == 'Quantidade de quartos':
    var = 'qtd_quartos'
   elif var == 'Quantidade de banheiros':
    var = 'qtd_banheiros'
   elif var == 'Tamanho da casa':
    var = 'tamanho_casa'
   elif var == 'Tamanho do lote':
    var = 'tamanho_lote'
   elif var == 'Quantidade de andares':
    var = 'qtd_andares'
   elif var == 'Vista para o mar':
    var = 'vista_mar'
   elif var == 'Condição do imóvel':
    var = 'condicao'
   elif var == 'Nota do imóvel':
    var = 'nota'
   elif var == 'Tamanho do porão':
    var = 'tamanho_porao'
   elif var == 'Ano da construção':
    var = 'ano_construcao'
   elif var == 'Ano da reforma':
    var = 'ano_reforma'
   st.scatter_chart(
    filtered_cep,
    x='preco',
    y=var,
    width=100,
    height=550)