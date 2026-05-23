"use client"
import { useEffect, useState } from "react"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from "recharts"

const COLORS = ["#4ade80", "#facc15", "#fb923c", "#ef4444"]

export default function AnalyticsPage() {
  const [data, setData] = useState<any[]>([])
  const [riskDist, setRiskDist] = useState<any[]>([])
  useEffect(() => {
    fetch("/api/protocols").then(r => r.json()).then(d => {
      const protocols = d.data || []
      setData(protocols)
      const dist = { low: 0, medium: 0, high: 0, critical: 0 }
      protocols.forEach((p: any) => { dist[p.risk_level as keyof typeof dist]++ })
      setRiskDist(Object.entries(dist).map(([name, value]) => ({ name, value })))
    })
  }, [])
  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold">Analytics</h2>
      <div className="grid grid-cols-2 gap-6">
        <div className="rounded-lg border border-border bg-card p-4">
          <h3 className="text-lg font-semibold mb-4">Risk Distribution</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie data={riskDist} cx="50%" cy="50%" outerRadius={100} dataKey="value" label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}>
                {riskDist.map((_, i) => <Cell key={i} fill={COLORS[i % COLORS.length]} />)}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
        <div className="rounded-lg border border-border bg-card p-4">
          <h3 className="text-lg font-semibold mb-4">Top Protocols by TVL</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data.slice(0, 10).map(p => ({ name: p.protocol?.substring(0, 10), tvl: Math.round(p.tvl / 1e6) }))}>
              <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--muted))" />
              <XAxis dataKey="name" tick={{ fill: "hsl(var(--muted-foreground))", fontSize: 11 }} />
              <YAxis tick={{ fill: "hsl(var(--muted-foreground))" }} />
              <Tooltip />
              <Bar dataKey="tvl" fill="hsl(var(--primary))" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  )
}
