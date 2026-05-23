"""Main entry point for the risk engine."""
import asyncio
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.engine.risk_scorer import RiskScorer
from src.engine.data.defillama import DefiLlamaClient
from src.engine.data.coingecko import CoinGeckoClient
from src.engine.protocol_registry import ProtocolRegistry
from src.engine.utils.config import load_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="DeFi Health Monitor", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

config = load_config()
scorer = RiskScorer(config)
registry = ProtocolRegistry()
llama = DefiLlamaClient()
coingecko = CoinGeckoClient()

@app.get("/api/protocols")
async def get_protocols():
    protocols = await llama.get_all_protocols()
    scores = []
    for p in protocols[:50]:
        tvl_history = await llama.get_tvl_history(p.get("slug", ""))
        score = scorer.calculate_health_score(p, tvl_history)
        scores.append(score)
    return {"data": scores, "count": len(scores)}

@app.get("/api/protocols/{protocol_id}")
async def get_protocol(protocol_id: str):
    protocol = await llama.get_protocol(protocol_id)
    tvl_history = await llama.get_tvl_history(protocol_id)
    score = scorer.calculate_health_score(protocol, tvl_history)
    return {"data": score}

@app.get("/api/risk/overview")
async def get_risk_overview():
    protocols = await llama.get_all_protocols()
    risk_dist = {"low": 0, "medium": 0, "high": 0, "critical": 0}
    for p in protocols[:100]:
        tvl_history = await llama.get_tvl_history(p.get("slug", ""))
        score = scorer.calculate_health_score(p, tvl_history)
        category = scorer.categorize_risk(score["health_score"])
        risk_dist[category] += 1
    return {"data": risk_dist, "total_protocols": len(protocols[:100])}

@app.get("/api/alerts")
async def get_alerts():
    protocols = await llama.get_all_protocols()
    alerts = []
    for p in protocols[:30]:
        tvl_history = await llama.get_tvl_history(p.get("slug", ""))
        score = scorer.calculate_health_score(p, tvl_history)
        if score["health_score"] < 40:
            alerts.append({
                "protocol": p.get("name", ""),
                "score": score["health_score"],
                "severity": "critical" if score["health_score"] < 20 else "high",
                "factors": score.get("risk_factors", []),
            })
    return {"data": alerts, "count": len(alerts)}

@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
