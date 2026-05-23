"use client"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts"

interface ProtocolData {
  protocol: string
  tvl: number
  health_score: number
}

export function TVLChart({ data }: { data: ProtocolData[] }) {
  const chartData = data.slice(0, 15).map(p => ({
    name: p.protocol.length > 12 ? p.protocol.substring(0, 12) + "..." : p.protocol,
    tvl: Math.round(p.tvl / 1e6),
    score: p.health_score,
  }))
  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={chartData}>
        <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--muted))" />
        <XAxis dataKey="name" tick={{ fill: "hsl(var(--muted-foreground))", fontSize: 11 }} angle={-45} textAnchor="end" height={60} />
        <YAxis tick={{ fill: "hsl(var(--muted-foreground))" }} />
        <Tooltip contentStyle={{ backgroundColor: "hsl(var(--card))", border: "1px solid hsl(var(--border))", borderRadius: "8px", color: "hsl(var(--foreground))" }} />
        <Bar dataKey="tvl" fill="hsl(var(--primary))" radius={[4, 4, 0, 0]} />
      </BarChart>
    </ResponsiveContainer>
  )
}
