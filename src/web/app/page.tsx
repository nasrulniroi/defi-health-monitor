"use client"
import { useEffect, useState } from "react"
import { ProtocolCard } from "../components/protocol-card"
import { RiskGauge } from "../components/risk-gauge"
import { TVLChart } from "../components/tvl-chart"
import { AlertBanner } from "../components/alert-banner"

interface ProtocolData {
  protocol: string
  health_score: number
  tvl: number
  chain: string
  category: string
  risk_level: string
  risk_factors: string[]
  components: Record<string, number>
}

export default function Dashboard() {
  const [protocols, setProtocols] = useState<ProtocolData[]>([])
  const [loading, setLoading] = useState(true)
  const [riskOverview, setRiskOverview] = useState<Record<string, number>>({})

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch("/api/protocols")
        const data = await res.json()
        setProtocols(data.data || [])
        const dist: Record<string, number> = { low: 0, medium: 0, high: 0, critical: 0 }
        ;(data.data || []).forEach((p: ProtocolData) => { dist[p.risk_level] = (dist[p.risk_level] || 0) + 1 })
        setRiskOverview(dist)
      } catch (e) { console.error("Failed to fetch protocols:", e) }
      finally { setLoading(false) }
    }
    fetchData()
  }, [])

  if (loading) return <div className="flex items-center justify-center h-64"><div className="text-muted-foreground">Loading protocol data...</div></div>

  const criticalAlerts = protocols.filter(p => p.risk_level === "critical")

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-3xl font-bold">Protocol Health Dashboard</h2>
        <span className="text-sm text-muted-foreground">{protocols.length} protocols monitored</span>
      </div>

      {criticalAlerts.length > 0 && <AlertBanner alerts={criticalAlerts} />}

      <div className="grid grid-cols-4 gap-4">
        {Object.entries(riskOverview).map(([level, count]) => (
          <div key={level} className="rounded-lg border border-border bg-card p-4">
            <div className="text-sm text-muted-foreground capitalize">{level} Risk</div>
            <div className="text-2xl font-bold mt-1">{count}</div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-3 gap-2">
        <div className="col-span-2 rounded-lg border border-border bg-card p-4">
          <h3 className="text-lg font-semibold mb-4">TVL Distribution</h3>
          <TVLChart data={protocols} />
        </div>
        <div className="rounded-lg border border-border bg-card p-4">
          <h3 className="text-lg font-semibold mb-4">Health Overview</h3>
          <RiskGauge value={protocols.length > 0 ? protocols.reduce((a, b) => a + b.health_score, 0) / protocols.length : 0} />
        </div>
      </div>

      <div>
        <h3 className="text-lg font-semibold mb-4">Top Protocols</h3>
        <div className="grid grid-cols-3 gap-4">
          {protocols.slice(0, 9).map((p, i) => <ProtocolCard key={i} protocol={p} />)}
        </div>
      </div>
    </div>
  )
}
