import streamlit as st
import openai

# Configuração da chave de API de forma segura
openai.api_key = api_key

# Dicionário de estados e suas sub-regiões
subregioes_por_estado = {
    'Acre': ['Alto Acre', 'Baixo Acre', 'Purus', 'Juruá'],
    'Alagoas': ['Leste Alagoano', 'Agreste Alagoano', 'Sertão Alagoano'],
    'Amapá': ['Macapá', 'Santana', 'Oiapoque', 'Mazagão'],
    'Amazonas': ['Manaus', 'Parintins', 'Itacoatiara', 'Tefé', 'Coari'],
    'Bahia': ['Recôncavo', 'Zona da Mata', 'Agreste', 'Sertão', 'Extremo Oeste'],
    'Ceará': ['Litoral Oeste', 'Litoral Leste', 'Sertão Central', 'Inhamuns', 'Cariri'],
    'Distrito Federal': ['Brasília', 'Taguatinga', 'Ceilândia', 'Planaltina'],
    'Espírito Santo': ['Litoral Norte', 'Central Serrana', 'Central Sul', 'Caparaó'],
    'Goiás': ['Norte Goiano', 'Leste Goiano', 'Sul Goiano', 'Centro Goiano'],
    'Maranhão': ['Norte Maranhense', 'Oeste Maranhense', 'Leste Maranhense', 'Centro Maranhense', 'Sul Maranhense'],
    'Mato Grosso': ['Norte Mato-Grossense', 'Nordeste Mato-Grossense', 'Centro-Sul Mato-Grossense', 'Sudoeste Mato-Grossense'],
    'Mato Grosso do Sul': ['Pantanais Sul-Mato-Grossenses', 'Centro Norte', 'Sudoeste', 'Leste'],
    'Minas Gerais': ['Triângulo Mineiro', 'Zona da Mata', 'Sul/Sudoeste de Minas', 'Central Mineira', 'Norte de Minas', 'Jequitinhonha/Mucuri'],
    'Pará': ['Baixo Amazonas', 'Marajó', 'Metropolitana de Belém', 'Nordeste Paraense', 'Sudeste Paraense', 'Sudoeste Paraense'],
    'Paraíba': ['Mata Paraibana', 'Agreste Paraibano', 'Borborema', 'Sertão Paraibano'],
    'Paraná': ['Norte Pioneiro', 'Campos Gerais', 'Oeste Paranaense', 'Sudoeste Paranaense', 'Região Metropolitana de Curitiba'],
    'Pernambuco': ['Região Metropolitana do Recife', 'Zona da Mata', 'Agreste', 'Sertão Pernambucano'],
    'Piauí': ['Norte Piauiense', 'Centro-Norte Piauiense', 'Sudeste Piauiense', 'Sudoeste Piauiense'],
    'Rio de Janeiro': ['Região Metropolitana', 'Baixada Fluminense', 'Sul Fluminense', 'Norte Fluminense', 'Região dos Lagos', 'Serrana'],
    'Rio Grande do Norte': ['Leste Potiguar', 'Agreste Potiguar', 'Central Potiguar', 'Oeste Potiguar'],
    'Rio Grande do Sul': ['Região Metropolitana de Porto Alegre', 'Serra Gaúcha', 'Norte Gaúcho', 'Sul Gaúcho', 'Campanha Gaúcha', 'Litoral'],
    'Rondônia': ['Madeira-Guaporé', 'Vale do Jamari', 'Zona da Mata', 'Vale do Guaporé'],
    'Roraima': ['Norte de Roraima', 'Sul de Roraima'],
    'Santa Catarina': ['Grande Florianópolis', 'Norte Catarinense', 'Vale do Itajaí', 'Serrana', 'Oeste Catarinense', 'Sul Catarinense'],
    'São Paulo': ['Região Metropolitana de São Paulo', 'Vale do Paraíba', 'Litoral Paulista', 'Campinas', 'Sorocaba', 'Bauru', 'Araçatuba', 'Presidente Prudente', 'Ribeirão Preto', 'São José do Rio Preto'],
    'Sergipe': ['Leste Sergipano', 'Agreste Sergipano', 'Sertão Sergipano'],
    'Tocantins': ['Ocidental do Tocantins', 'Oriental do Tocantins'],
}

# Função para gerar a descrição da persona com foco nos aspectos sociais, antropológicos e psicológicos gerais
def gerar_descricao(estado, subregiao, classe_social, contexto, genero, idade):
    prompt = (
        f"Faça uma análise de uma pessoa do gênero {genero.lower()}, com {int(idade)} anos, pertencente à classe {classe_social}, "
        f"que vive em um contexto {contexto}, na sub-região {subregiao}, no estado de {estado}, no Brasil, com o objetivo de ajudar um terapeuta lacaniano "
        f"a entender essa pessoa. A análise deve focar em influências socioculturais, antropológicas, históricas e psicológicas predominantes da região. "
        f"Considere como o meio social pode impor certos valores e comportamentos e como isso pode influenciar características psicológicas dessa pessoa. "
        f"Destaque aspectos como possíveis desafios sociais, dinâmicas de poder, acesso a recursos e como a colonização e o contexto histórico moldaram a sociedade. "
        f"Não inclua histórias pessoais específicas, mas sim uma análise geral das influências culturais e psicológicas mais comuns para essa persona. "
        f"Evite estereótipos e generalizações excessivas, mantendo o foco em características socioculturais predominantes."
    )

    # Chamada à API da OpenAI para gerar a descrição com base no prompt
    response = openai.chat.completions.create(
        model="gpt-4",  # Altere para gpt-3.5-turbo se necessário
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.7,
    )

    descricao = response.choices[0].message.content.strip()
    return descricao

# Função para simular como a persona reagiria em uma situação específica
def obter_reacao_da_persona(descricao_persona, situacao):
    prompt = (
        f"Com base na seguinte descrição de uma pessoa:\n\n"
        f"{descricao_persona}\n\n"
        f"Descreva como essa pessoa reagiria na seguinte situação:\n\n"
        f"Situação: {situacao}\n\n"
        f"Considere os traços de personalidade, o contexto cultural, histórico e as influências sociais e psicológicas da região. Evite estereótipos."
    )

    # Chamada à API da OpenAI para gerar a reação da persona com base na descrição e situação
    response = openai.chat.completions.create(
        model="gpt-4",  # Altere para gpt-3.5-turbo se necessário
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.7,
    )

    reacao = response.choices[0].message.content.strip()
    return reacao


# Função para atualizar as sub-regiões com base no estado selecionado
def get_subregioes(estado):
    return subregioes_por_estado.get(estado, [])

# Inicializa o estado da sessão para armazenar a descrição
if 'descricao' not in st.session_state:
    st.session_state['descricao'] = ''

# Título da Aplicação
st.title("🧠 Simulador de Persona" )

# Seção de seleção de parâmetros para a criação da persona
st.header("Configuração da Persona")

# Estado (com base em um dicionário de estados já existente)
estado = st.selectbox('Selecione o estado:', list(subregioes_por_estado.keys()))

# Sub-região do estado escolhido
subregiao = st.selectbox('Selecione a sub-região:', get_subregioes(estado))

# Escolha da classe social da persona
classe_social = st.selectbox('Selecione a classe social:', ['baixa', 'média', 'alta'])

# Contexto (urbano ou rural)
contexto = st.selectbox('Selecione o contexto:', ['urbano', 'rural'])

# Gênero da persona
genero = st.selectbox('Selecione o gênero:', ['Masculino', 'Feminino', 'Outro'])

# Idade da persona
idade = st.number_input('Insira a idade da persona:', min_value=1, max_value=120, value=30)

# Geração da descrição da persona ao clicar no botão
if st.button("Gerar Descrição da Persona"):
    with st.spinner('Gerando descrição...'):
        descricao = gerar_descricao(estado, subregiao, classe_social, contexto, genero, idade)
        st.session_state['descricao'] = descricao  # Armazena a descrição na sessão
        st.subheader("Descrição da Persona")
        st.write(descricao)

# Verificação se a descrição já foi gerada para permitir a interação
if st.session_state['descricao']:
    st.header("Interagir com a Persona")

    # Entrada de situação para simulação de como a persona reagiria
    situacao = st.text_input("Descreva uma situação para a persona:")

    # Simulação da reação da persona à situação fornecida
    if st.button('Simular Reação da Persona'):
        if situacao.strip() != '':
            with st.spinner('Gerando reação...'):
                reacao = obter_reacao_da_persona(st.session_state['descricao'], situacao)
                st.subheader("Reação da Persona")
                st.write(reacao)
        else:
            st.warning("Por favor, insira uma situação.")
