"use client"

interface Alert {
  protocol: string
  health_score: number
  risk_factors: string[]
}

export function AlertBanner({ alerts }: { alerts: Alert[] }) {
  return (
    <div className="rounded-lg border border-destructive bg-destructive/10 p-4">
      <div className="flex items-center gap-2 mb-2">
        <span className="text-destructive font-semibold">Critical Risk Alert</span>
        <span className="text-xs bg-destructive text-destructive-foreground px-2 py-0.5 rounded-full">{alerts.length}</span>
      </div>
      <div className="space-y-1 text-sm">
        {alerts.map((a, i) => (
          <div key={i} className="flex items-center justify-between">
            <span>{a.protocol}</span>
            <span className="text-muted-foreground">Score: {a.health_score.toFixed(1)} | Factors: {a.risk_factors.join(", ")}</span>
          </div>
        ))}
      </div>
    </div>
  )
}
