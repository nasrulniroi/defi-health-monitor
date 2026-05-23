"use client"
import { useEffect, useState } from "react"

export default function AlertsPage() {
  const [alerts, setAlerts] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  useEffect(() => {
    fetch("/api/alerts").then(r => r.json()).then(d => setAlerts(d.data || [])).finally(() => setLoading(false))
  }, [])
  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold">Risk Alerts</h2>
      {loading ? <div>Loading...</div> : alerts.length === 0 ? <div className="text-muted-foreground">No active alerts</div> : (
        <div className="space-y-3">
          {alerts.map((a, i) => (
            <div key={i} className="rounded-lg border border-border bg-card p-4">
              <div className="flex items-center justify-between">
                <span className="font-semibold">{a.protocol}</span>
                <span className={`text-sm ${a.severity === "critical" ? "text-red-400" : "text-orange-400"}`}>{a.severity}</span>
              </div>
              <div className="text-sm text-muted-foreground mt-1">Score: {a.score} | Factors: {a.factors?.join(", ")}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
