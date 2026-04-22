import sys 
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pipeline import Pipeline

url = 'https://aplicacoes.mds.gov.br/sagi/servicos/misocial/?fl=codigo_ibge%2C%20anomes_s%20qtde_gestantes_acomp:sicon_qtde_gestantes_acompanhadas_apartir_2023_l%20qtde_gestantes_prenatal_em_dia:sicon_qtde_gestantes_prenatal_em_dia_apartir_2023_l%20perc_gestantes_prenatal_em_dia:sicon_perc_gestantes_prenatal_em_dia_apartir_2023_d%20qtde_criancas_perf_saude_0a7:sicon_qtde_criancas_perfil_saude_apartir_2023_l%20qtde_criancas_acomp:sicon_qtde_criancas_acompanhadas_apartir_2023_l%20perc_criancas_acomp:sicon_perc_criancas_acompanhadas_apartir_2023_d%20qtde_criancas_vacinacao_em_dia:sicon_qtde_criancas_vacinacao_em_dia_apartir_2023_l%20qtde_criancas_dados_nutricionais:sicon_qtde_criancas_dados_nutricionais_apartir_2023_l%20qtde_pess_perfil_saude_0a7_14a44:sicon_qtde_pessoas_perfil_saude_apartir_2023_l%20qtde_pess_acomp_saude:sicon_qtde_acompanhadas_saude_apartir_2023_l%20perc_acomp_saude:sicon_perc_acompanhadas_saude_apartir_2023_d%20qtde_mulheres_perfil_saude_14a44:sicon_qtde_mulheres_perfil_saude_apartir_2023_l%20qtde_mulheres_acomp:sicon_qtde_mulheres_acompanhadas_apartir_2023_l%20perc_mulheres_acomp:sicon_perc_mulheres_acompanhadas_apartir_2023_d%20qtde_pess_perfil_saude_nao_acomp_motiv_inform:sicon_qtde_pess_perfil_saude_nao_acomp_motiv_inform_l%20qtde_pess_perfil_saude_nao_acomp_motiv_n_inform:sicon_qtde_pess_perfil_saude_nao_acomp_motiv_n_infor_l%20qtde_criancas_cumpriram_saude:sicon_qtde_criancas_cumpriram_saude_apartir_2023_l%20perc_criancas_cumpriram_saude:sicon_perc_criancas_cumpriram_saude_apartir_2023_d&fq=sicon_qtde_pessoas_perfil_saude_apartir_2023_l%3A*&q=*%3A*&rows=100000&sort=codigo_ibge%20asc%2Canomes_s%20desc&wt=csv&fq=anomes_s:2025*'

def teste_pipeline():
    dado_saude = Pipeline(url)

    # 1 Teste - Extração
    sucesso_extracao = dado_saude.extrair_url()
    assert sucesso_extracao is True, "Erro: não é possível baixar os dados da URL."
    assert dado_saude.raw_data is not None, "raw_data está vazio após extração."

    # 2 Teste - Transformação
    sucesso_transformacao = dado_saude.transformar_dados()
    assert sucesso_transformacao is True, "Falha na lógiva de tranformação dos dados, favor revisar."

    # 3 Validar conteúdo do DataFrame
    assert dado_saude.dados_tabular is not None, "O atributo dados_tabular não deveria ser None."
    assert not dado_saude.dados_tabular.empty, "O DataFrame resultou vazio."

    # 4 Validar Estatística
    resumo = dado_saude.obter_estatisticas()
    assert isinstance(resumo,dict), "Erro: O retorno das estatísticas deve ser um dicionário."
    assert resumo["total_linhas"] > 0, "Erro: O relatório indica 0 linhas processados."

    # 5 Validar salvar em formato csv
    nome_saida = 'arquivo_csv'
    assert dado_saude.salvar_csv(nome_saida) is True, "Falha ao salvar em arquivo csv, favor revisar."
    print("Pipeline testada!")
    
    # 6 Remover o arquivo criado após o teste
    nome_saida = nome_saida + '.csv'
    if os.path.exists(nome_saida):
        os.remove(nome_saida)

if __name__ == "__main__":
    teste_pipeline()

