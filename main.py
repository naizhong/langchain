from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv(override=True)

def main():
    information = """
    Elon Musk is a visionary entrepreneur, engineer, and business magnate who has made significant contributions to various industries, particularly in technology, transportation, and space exploration. Born on June 28, 1971, in Pretoria, South Africa, Musk moved to the United States to study at the University of Pennsylvania, where he earned degrees in both economics and physics. His professional journey has been marked by ambitious projects and companies that seek to revolutionize existing industries and push the boundaries of human achievement.

    Musk co-founded Zip2, an online city guide software for newspapers, which was later sold to Compaq for nearly $300 million. He then founded X.com, an online payment company that eventually became PayPal after a merger; PayPal was acquired by eBay for $1.5 billion in stock. With resources from these ventures, Musk embarked on new and daring enterprises that further cemented his reputation as a bold innovator.

    He is the founder, CEO, and chief engineer of SpaceX, which aims to reduce space transportation costs and enable the colonization of Mars. SpaceX has achieved significant milestones, including the first privately funded, liquid-fueled rocket (Falcon 1) to reach orbit, the first private company to dock a spacecraft (Dragon) at the International Space Station, and the development of the reusable Falcon 9 rocket and the Starship spacecraft. Musk’s vision for humanity’s future includes making life multiplanetary to ensure its long-term survival.

    As CEO and product architect of Tesla, Inc., Musk has played a crucial role in the widespread adoption of electric vehicles. Under his leadership, Tesla developed innovative electric cars, energy storage systems, and solar products, pushing the automotive industry toward sustainability. The popularity of Tesla vehicles has demonstrated the viability and appeal of electric vehicles on a global scale.

    Musk is also the founder of The Boring Company, which focuses on tunnel construction and infrastructure, and a co-founder of Neuralink, dedicated to developing brain–computer interface technology. Additionally, he was co-founder and initial funder of OpenAI, an organization focused on artificial intelligence research. In 2022, Musk acquired Twitter, rebranding it as X Corp. with ambitions to transform it into an "everything app."

    Elon Musk’s unconventional ideas, daring business ventures, and charismatic public persona have made him one of the world’s most prominent and influential tech leaders, frequently sparking both admiration and controversy.
    """
    
    summary_template = f"""
    given the infomation {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    
    summary_prompt = ChatPromptTemplate.from_template(summary_template)
    # llm = ChatOllama(model="gemma3:270m", temperature=0)
    llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
    summary_chain = summary_prompt | llm
    
    result = summary_chain.invoke({"information": information})
    # The result is an AIMessage. Format its content nicely for display.
    print(result.content)

if __name__ == "__main__":
    main()
