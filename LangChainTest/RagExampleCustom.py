from operator import itemgetter

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

vectorstore = FAISS.from_texts(
    ["Sparkle is a TIM-owned company that operates in a global context offering connectivity solutions and ICT services to meet the needs of multinational companies, internet service providers, OTTs , Media and Content Player, fixed and mobile phone application providers and carriers. Sparkle owns and operates a proprietary network of over 600,000 km of land and sea cables with a widespread presence in the Mediterranean basin, Europe and America.With a direct presence in 32 countries and commercial coverage on a global scale, Sparkle can count on a workforce practically distributed all over the world.",
     "Sparkle's Bigdata platform is implemented throught a mult-layer architecture. Layers are the follow: Business Intelligence, Datawarehouse, ETL & Data Processing, Datalake, API ",
     "The products used to build BI layer are Oracle Business Intelligence an Tableau. There is also a custom component for Signalling Adavanced Analytics (RA/REM) based on a Java Apps that run on Tomcat AS",
     "The products used to build DWH layer are Oracle DBMS vs 12c, Cloudera Data Services (CDS) vs 1.4.1 and Trino. CDS running on K8s cluster. In order to manage query workload, in CDS is defined a Hive-LLAP autoscaling component",
     "Datalake is implemented using Cloudera Dataplatform Base Private Cloud vs 7.1.7 SP1. Sparkle's datalake is based on Hadoop platform",
     "ETL is implemented using IBM Datastage vs 11.7. Job for Data Processing uses packages included in CDP: Spark, Kafka, Hadoop, Hive, etc.",
     "API layer is buid using Spring framework",
     "CDP Private Cloud cluster has 4 edgenodes; 5 masternodes; 18 datanodes",
     "CDS cluster has masternodes; 9 workernodes",
     "Spark framework is used to implement near real time jobs",
     "Hive is used to implement DWH on hdfs side"
    ]
    , embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

#print(chain.invoke("what sparkle do ?"))
#print(chain.invoke("how many layers has Sparkle's Bigdata Platform ?"))

template = """Answer the question based only on the following context:
{context}

Question: {question}

Answer in the following language: {language}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
        "language": itemgetter("language"),
    }
    | prompt
    | model
    | StrOutputParser()
)

print(chain.invoke({"question": "what sparkle do ?", "language": "italian"}))
print(chain.invoke({"question": "how many layers has Sparkle's Bigdata Platform ?", "language": "italian"}))
print(chain.invoke({"question": "In quale layer viene utilizzato Tableau ?", "language": "italian"}))
print(chain.invoke({"question": "Per cosa viene utilizzato Hive all'interno della piattaforma e come viene gestito il workload delle query?", "language": "italian"}))