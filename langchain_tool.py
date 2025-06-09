# from langchain.agents import Tool, initialize_agent
# from langchain.chat_models import ChatOpenAI
# import requests

# # Tool 정의
# def trigger_mcp_tool(issue_id: str, title: str, command: str):
#     response = requests.post("http://localhost:8000/trigger-mcp", json={
#         "issue_id": issue_id,
#         "issue_title": title,
#         "command": command
#     })
#     return response.json()

# # LangChain Tool로 등록
# mcp_tool = Tool(
#     name="MCP Trigger",
#     func=lambda x: trigger_mcp_tool(**eval(x)),
#     description="트리거 MCP. 입력: {'issue_id': 'ASANA-123', 'title': 'Fix bug', 'command': 'register_issue_and_create_branch'}"
# )

# # LangChain Agent에 등록
# llm = ChatOpenAI(temperature=0)
# agent = initialize_agent(tools=[mcp_tool], llm=llm, agent="zero-shot-react-description", verbose=True)

# # 테스트
# agent.run("ASANA-456 이슈 ID를 포함해서 브랜치 생성과 MR을 요청해줘")
