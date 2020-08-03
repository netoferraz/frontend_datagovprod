import streamlit as st
import SessionState
from api.response import parse_ementa


def main():
    """ Classificador de normas infraconstitucionais"""
    st.title("🧠 py-classifica-legal 🤖")
    st.subheader("Um classificador para normas infraconstitucionais ⚖️.")
    st.markdown("O *py-classifica-legal* foi treinado com uma base de mais de 30.000 normas legais. O intuito do programa é auxiliar em uma melhor governança de dados públicos, por meio de sugestões de classificações de normas infraconstitucionais a partir de suas respectivas ementas.")
    session_state = SessionState.get(name="", button_sent=False)
    input_ementa = st.text_area("Insira o texto da ementa", "Digite aqui.")
    button_sent = st.button("Classificar")
    if button_sent:
        session_state.button_sent = True
    if session_state.button_sent:
        get_tags = parse_ementa(input_ementa)
        if get_tags:
            st.multiselect('Tags', ['ACORDO INTERNACIONAL', 'ALTERAÇÃO', 'AMBITO', 'APROVAÇÃO',
            'AREA PRIORITARIA', 'ATO', 'AUTORIZAÇÃO', 'BRASIL', 'COMPETENCIA',
            'COMPOSIÇÃO', 'CONCESSÃO', 'CORRELAÇÃO', 'CREDITO SUPLEMENTAR',
            'CRIAÇÃO', 'CRITERIOS', 'DECLARAÇÃO', 'DESAPROPRIAÇÃO', 'DESTINAÇÃO',
            'DISPOSITIVOS', 'DOTAÇÃO ORÇAMENTARIA', 'EMPRESA DE TELECOMUNICAÇÕES',
            'ESTADO DE MINAS GERAIS MG', 'ESTADO DE SÃO PAULO SP',
            'ESTADO DO PARANA PR', 'ESTADO DO RIO GRANDE DO SUL RS', 'EXECUTIVO',
            'EXECUÇÃO', 'FIXAÇÃO', 'FUNCIONAMENTO', 'HIPOTESE', 'IMOVEL RURAL',
            'INSTITUTO NACIONAL DE COLONIZAÇÃO E REFORMA AGRARIA INCRA',
            'INTERESSE SOCIAL', 'MUNICIPIO', 'NORMAS', 'OBJETIVO',
            'ORÇAMENTO DA SEGURIDADE SOCIAL', 'ORÇAMENTO FISCAL',
            'PAIS ESTRANGEIRO', 'RADIODIFUSÃO', 'REFORMA AGRARIA', 'REFORÇO',
            'RENOVAÇÃO', 'SERVIÇO', 'TEXTO', 'UNIÃO FEDERAL', 'UTILIDADE PUBLICA'], 
            default=get_tags)
        else:
            st.multiselect('Tags', ['ACORDO INTERNACIONAL', 'ALTERAÇÃO', 'AMBITO', 'APROVAÇÃO',
            'AREA PRIORITARIA', 'ATO', 'AUTORIZAÇÃO', 'BRASIL', 'COMPETENCIA',
            'COMPOSIÇÃO', 'CONCESSÃO', 'CORRELAÇÃO', 'CREDITO SUPLEMENTAR',
            'CRIAÇÃO', 'CRITERIOS', 'DECLARAÇÃO', 'DESAPROPRIAÇÃO', 'DESTINAÇÃO',
            'DISPOSITIVOS', 'DOTAÇÃO ORÇAMENTARIA', 'EMPRESA DE TELECOMUNICAÇÕES',
            'ESTADO DE MINAS GERAIS MG', 'ESTADO DE SÃO PAULO SP',
            'ESTADO DO PARANA PR', 'ESTADO DO RIO GRANDE DO SUL RS', 'EXECUTIVO',
            'EXECUÇÃO', 'FIXAÇÃO', 'FUNCIONAMENTO', 'HIPOTESE', 'IMOVEL RURAL',
            'INSTITUTO NACIONAL DE COLONIZAÇÃO E REFORMA AGRARIA INCRA',
            'INTERESSE SOCIAL', 'MUNICIPIO', 'NORMAS', 'OBJETIVO',
            'ORÇAMENTO DA SEGURIDADE SOCIAL', 'ORÇAMENTO FISCAL',
            'PAIS ESTRANGEIRO', 'RADIODIFUSÃO', 'REFORMA AGRARIA', 'REFORÇO',
            'RENOVAÇÃO', 'SERVIÇO', 'TEXTO', 'UNIÃO FEDERAL', 'UTILIDADE PUBLICA'])
            st.warning("Não há sugestão de classificação para a ementa consultada.")



if __name__ == "__main__":
    main()