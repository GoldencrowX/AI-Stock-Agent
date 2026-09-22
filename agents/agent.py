# from google.adk.agents.llm_agent import LlmAgent
# from google.adk.agents.sequential_agent import SequentialAgent

# from tools.stock_tools import get_stock_price

# MODEL = "gemini-2.5-flash"


# stock_data_agent = LlmAgent(
#     name="StockDataAgent",
#     model=MODEL,
#     tools=[get_stock_price],
#     instruction="""
# Get stock data.

# If user gives a stock symbol,
# call get_stock_price.
# """,
#     output_key="stock_data"
# )


# analysis_agent = LlmAgent(
#     name="StockAnalysisAgent",
#     model=MODEL,
#     instruction="""
# Analyze this stock data:

# {stock_data}
# """,
#     output_key="analysis"
# )


# recommendation_agent = LlmAgent(
#     name="RecommendationAgent",
#     model=MODEL,
#     instruction="""
# Based on the analysis:

# {analysis}

# Give recommendation:
# BUY / HOLD / SELL
# """,
#     output_key="recommendation"
# )


# pipeline = SequentialAgent(
#     name="StockPipeline",
#     sub_agents=[
#         stock_data_agent,
#         analysis_agent,
#         recommendation_agent
#     ]
# )

# root_agent = pipeline

from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent

from tools.stock_tools import (
    get_stock_price,
    get_stock_news,
    get_stock_fundamentals
)

MODEL = "gemini-2.5-flash"


stock_data_agent = LlmAgent(
    name="StockDataAgent",
    model=MODEL,
    tools=[
        get_stock_price,
        get_stock_news,
        get_stock_fundamentals
    ],
    instruction="""
You are a stock data collector.

User may ask in Thai or English.

If the user gives a stock symbol:

You MUST call these tools:

1. get_stock_price(symbol)
2. get_stock_fundamentals(symbol)
3. get_stock_news(symbol)

Use the same symbol from the user input.

IMPORTANT:
You MUST call the tools.
Do NOT answer without using the tools.

Collect all data and return it.

If the user question is NOT about stocks or investing, reply:

"ขออภัย ระบบนี้ตอบได้เฉพาะคำถามเกี่ยวกับหุ้นเท่านั้น"
""",
    output_key="stock_data"
)


analysis_agent = LlmAgent(
    name="StockAnalysisAgent",
    model=MODEL,
    instruction="""
You are a professional stock analyst.

Analyze the following stock data:

{stock_data}

Your analysis MUST include:

1. ราคาหุ้นปัจจุบันแพงหรือถูก
2. พื้นฐานบริษัท
3. ข่าวล่าสุดมีผลดีหรือผลเสีย
4. แนวโน้มโดยรวม

ตอบเป็นภาษาไทยเท่านั้น
""",
    output_key="analysis"
)


recommendation_agent = LlmAgent(
    name="RecommendationAgent",
    model=MODEL,
    instruction="""
Based on the analysis:

{analysis}

Give investment recommendation.

Format:

คำแนะนำการลงทุน:
BUY / HOLD / SELL

เหตุผล:
อธิบายสั้นๆเป็นภาษาไทย
""",
    output_key="recommendation"
)


pipeline = SequentialAgent(
    name="StockPipeline",
    sub_agents=[
        stock_data_agent,
        analysis_agent,
        recommendation_agent
    ]
)

root_agent = pipeline