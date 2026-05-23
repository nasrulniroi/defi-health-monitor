"use client"

export function RiskGauge({ value }: { value: number }) {
  const color = value >= 75 ? "#4ade80" : value >= 50 ? "#facc15" : value >= 25 ? "#fb923c" : "#ef4444"
  const label = value >= 75 ? "Healthy" : value >= 50 ? "Moderate" : value >= 25 ? "At Risk" : "Critical"
  return (
    <div className="flex flex-col items-center">
      <svg viewBox="0 0 200 120" className="w-48 h-28">
        <path d="M 20 100 A 80 80 0 0 1 180 100" fill="none" stroke="hsl(var(--muted))" strokeWidth="12" strokeLinecap="round" />
        <path d="M 20 100 A 80 80 0 0 1 180 100" fill="none" stroke={color} strokeWidth="12" strokeLinecap="round" strokeDasharray={`${(value / 100) * 251.3} 251.3`} />
        <text x="100" y="90" textAnchor="middle" className="text-2xl font-bold" fill={color}>{value.toFixed(1)}</text>
        <text x="100" y="108" textAnchor="middle" className="text-xs" fill="hsl(var(--muted-foreground))">{label}</text>
      </svg>
      <div className="text-sm text-muted-foreground mt-2">Average Protocol Health Score</div>
    </div>
  )
}
