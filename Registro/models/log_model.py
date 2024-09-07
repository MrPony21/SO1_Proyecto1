from pydantic import BaseModel

class LogModel(BaseModel):
    pid: int
    container_id: str
    name: str
    vsz: int
    rss: int
    memory_usage: float
    cpu_usage: float
    action: str
    timestamp: str
