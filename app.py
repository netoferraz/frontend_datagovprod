import streamlit as st
import SessionState
from api.response import parse_ementa


def main():
    """ Classificador de normas infraconstitucionais"""
    multi_tags = ['ACORDO INTERNACIONAL', 'ALTERAÇÃO', 'AMBITO', 'APROVAÇÃO',
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
            'RENOVAÇÃO', 'SERVIÇO', 'TEXTO', 'UNIÃO FEDERAL', 'UTILIDADE PUBLICA']
    st.title("🧠 py-classifica-legal 🤖")
    st.subheader("Um classificador para normas infraconstitucionais ⚖️.")
    st.markdown("O *py-classifica-legal* foi treinado com uma base de mais de 30.000 normas legais. O intuito do programa é auxiliar em uma melhor governança de dados públicos, por meio de sugestões de classificações de normas infraconstitucionais a partir de suas respectivas ementas.")
    st.markdown("Você pode consultar alguns exemplos de ementas clicando <a href='http://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/decretos1/2020-decretos' target='_blank' style='color: #f97b6f;'> aqui.</a>", unsafe_allow_html=True)
    session_state = SessionState.get(name="", button_sent=False)
    input_ementa = st.text_area("Insira o texto da ementa", "Digite aqui.")
    button_sent = st.button("Classificar")
    if button_sent:
        session_state.button_sent = True
    if session_state.button_sent:
        get_tags = parse_ementa(input_ementa)
        if get_tags:
            st.multiselect('Tags', multi_tags, default=get_tags)
        else:
            st.multiselect('Tags', multi_tags)
            st.warning("Não há sugestão de classificação para a ementa consultada.")
    st.markdown("<center><blockquote cite='https://netoferraz.github.io/o-eu-analitico/'><p style='color: #bfc5d3;'><i>py-classifica-legal é uma prova de conceito desenvolvida por <a href='https://netoferraz.github.io/o-eu-analitico/' target='_blank' style='color: #f97b6f;'> José Ferraz Neto</a>.</i></p></blockquote></center>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()