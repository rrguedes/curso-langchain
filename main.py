from dotenv import load_dotenv
from httpx import Response
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    information = """
        Elon Reeve Musk (Pretória, 28 de junho de 1971) é um empresário e empreendedor sul-africano, naturalizado canadense e estadunidense, que dirige a SpaceX e a Tesla. Suas empresas trabalham com foguetes, veículos elétricos, energia e inteligência artificial. A Forbes o classificava como a pessoa mais rica do mundo em outubro de 2026, com um patrimônio estimado em 908,5 bilhões de dólares.[2]

        Nascido em uma família de boas condições financeiras, Elon mudou-se para o Canadá em 1989 e estudou na Queen's University e na Universidade da Pensilvânia, onde obteve diplomas em física e economia. Em 1995, cofundou a Zip2, que desenvolvia programas para jornais na internet. Com a venda da empresa em 1999, investiu na X.com, que se fundiu à Confinity e adotou o nome PayPal. Tornou-se cidadão dos Estados Unidos em 2002, ano em que fundou a SpaceX para desenvolver foguetes e serviços de transporte espacial.

        Elon investiu na Tesla em 2004 e assumiu sua direção-executiva em 2008. Cofundou a OpenAI em 2015 e deixou seu conselho em 2018, antes de criar a xAI, incorporada pela SpaceX em 2026. Comprou o Twitter em 2022, alterou sua administração e mudou seu nome para X no ano seguinte. Também participou da criação da SolarCity, da empresa de neurotecnologia Neuralink e da construtora de túneis The Boring Company. Seus projetos e declarações defendem a expansão do uso de energias renováveis, a colonização de Marte e o desenvolvimento de inteligência artificial.

        Elon recebeu críticas por divulgar teorias da conspiração e informações falsas sobre a COVID-19 e as eleições estadunidenses, assim como por declarações acusadas de racismo, antissemitismo e transfobia. A redução da moderação do Twitter também foi acompanhada por um aumento do discurso de ódio na plataforma. Ele passou a apoiar figuras e partidos de direita e extrema-direita em diferentes países e foi o maior doador individual da eleição presidencial estadunidense de 2024, na qual apoiou Donald Trump.[3][4][5][6][7][8]

        Entre janeiro e maio de 2025, foi assessor de Donald Trump e dirigiu de facto o Departamento de Eficiência Governamental, o DOGE. As demissões de servidores e os cortes em programas federais, sobretudo na ajuda internacional, provocaram protestos e ações judiciais. Depois de deixar o governo, retomou a administração de suas empresas e entrou em conflito público com o presidente sobre a política orçamentária.
    """
    summary_template = f"""
        Given the information {information} about a person, I want you to create:
        1. A short summary of the person's life.
        2. Two interesting facts about the person.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # llm = ChatOllama(model="gemma3:270m")
    summary_prompt_template = ChatPromptTemplate.from_template(summary_template)
    summary_chain = summary_prompt_template | llm
    response: Response = summary_chain.invoke({"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
