from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from asana_gitlab_mcp import trigger_mcp
app = FastAPI()

class MCPRequest(BaseModel):
    asana_issue_id: str

@app.post("/mcp/trigger")
def run_mcp(req: MCPRequest):
    try:
        trigger_mcp(req.asana_issue_id)  # 앞서 작성한 MCP 함수 호출
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))