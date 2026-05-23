"use client"

interface Protocol {
  protocol: string
  health_score: number
  tvl: number
  chain: string
  category: string
  risk_level: string
}

export function ProtocolCard({ protocol }: { protocol: Protocol }) {
  const riskColors: Record<string, string> = {
    low: "text-green-400",
    medium: "text-yellow-400",
    high: "text-orange-400",
    critical: "text-red-400",
  }
  return (
    <div className="rounded-lg border border-border bg-card p-4 hover:border-primary transition-colors">
      <div className="flex items-center justify-between mb-2">
        <h4 className="font-semibold">{protocol.protocol}</h4>
        <span className={`text-sm font-medium ${riskColors[protocol.risk_level] || "text-muted-foreground"}`}>
          {protocol.health_score.toFixed(1)}
        </span>
      </div>
      <div className="text-sm text-muted-foreground space-y-1">
        <div>TVL: ${(protocol.tvl / 1e9).toFixed(2)}B</div>
        <div>Chain: {protocol.chain}</div>
        <div>Category: {protocol.category}</div>
      </div>
      <div className="mt-3 h-1.5 rounded-full bg-muted overflow-hidden">
        <div className="h-full rounded-full transition-all" style={{ width: `${protocol.health_score}%`, backgroundColor: protocol.health_score >= 75 ? "#4ade80" : protocol.health_score >= 50 ? "#facc15" : protocol.health_score >= 25 ? "#fb923c" : "#ef4444" }} />
      </div>
    </div>
  )
}
